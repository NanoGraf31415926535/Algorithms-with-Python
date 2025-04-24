from collections import deque

class Event:
    def __init__(self, event_id, event_type, room, start_time, end_time):
        self.event_id = event_id
        self.event_type = event_type
        self.room = room
        self.start_time = start_time
        self.end_time = end_time

class Task:
    def __init__(self, task_id, event_id, task_type, start_time, end_time, required_volunteers):
        self.task_id = task_id
        self.event_id = event_id
        self.task_type = task_type
        self.start_time = start_time
        self.end_time = end_time
        self.required_volunteers = required_volunteers

class Volunteer:
    def __init__(self, volunteer_id, available_start_time, available_end_time):
        self.volunteer_id = volunteer_id
        self.available_start_time = available_start_time
        self.available_end_time = available_end_time

def can_volunteer_handle_task(volunteer, task):
    """Checks if a volunteer is available for the entire duration of a task."""
    return volunteer.available_start_time <= task.start_time and volunteer.available_end_time >= task.end_time

def build_network(events, tasks, volunteers):
    """Builds the flow network for the resource allocation problem."""
    capacity = {}
    graph = {}
    source = 'source'
    sink = 'sink'

    # Initialize source and sink nodes in the graph
    graph[source] = []
    graph[sink] = []

    # Create volunteer nodes and edges from source to volunteers
    volunteer_nodes = {v.volunteer_id: v for v in volunteers}
    for vol_id in volunteer_nodes:
        graph.setdefault(source, []).append(vol_id)
        graph.setdefault(vol_id, []).append(source)
        capacity[(source, vol_id)] = 1
        capacity[(vol_id, source)] = 0  # Residual capacity

    # Create task nodes and edges from volunteers to tasks
    task_nodes = {t.task_id: t for t in tasks}
    for task_id, task in task_nodes.items():
        graph.setdefault(task_id, [])
        graph.setdefault(sink, []) # Sink will have incoming edges
        graph.setdefault(task_id, []).append(sink)
        capacity[(task_id, sink)] = task.required_volunteers
        capacity[(sink, task_id)] = 0 # Residual capacity
        for vol_id, volunteer in volunteer_nodes.items():
            if can_volunteer_handle_task(volunteer, task):
                graph.setdefault(vol_id, []).append(task_id)
                graph.setdefault(task_id, []).append(vol_id)
                capacity[(vol_id, task_id)] = 1
                capacity[(task_id, vol_id)] = 0 # Residual capacity

    return graph, capacity, source, sink, volunteer_nodes, task_nodes

def edmonds_karp(graph, capacity, source, sink):
    """Implementation of the Edmonds-Karp algorithm for Max-Flow."""
    flow = 0
    flow_path = {}
    while True:
        parent = {node: None for node in graph}
        queue = deque([source])
        path_found = False

        while queue:
            u = queue.popleft()
            if u == sink:
                path_found = True
                break
            for v in graph.get(u, []):
                if parent[v] is None and capacity.get((u, v), 0) > 0:
                    parent[v] = u
                    queue.append(v)

        if not path_found:
            break

        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[(parent[s], s)])
            s = parent[s]
        flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            capacity[(u, v)] -= path_flow
            capacity[(v, u)] += path_flow
            v = u
            flow_path[(u,v)] = flow_path.get((u,v), 0) + path_flow

    return flow, flow_path

# Example Usage:
events = [
    Event("E1", "Workshop", "Room A", 9.0, 10.5),
    Event("E2", "Keynote", "Hall B", 11.0, 12.0)
]

tasks = [
    Task("T1", "E1", "Workshop Setup", 8.75, 9.0, 2), # Needs 2 volunteers from 8:45 to 9:00
    Task("T2", "E1", "Workshop Assistance", 9.0, 10.5, 1), # Needs 1 volunteer from 9:00 to 10:30
    Task("T3", "E2", "AV Support", 10.75, 12.0, 1) # Needs 1 volunteer from 10:45 to 12:00
]

volunteers = [
    Volunteer("V1", 8.5, 12.5),
    Volunteer("V2", 8.5, 12.5),
    Volunteer("V3", 9.0, 11.0)
]

graph, capacity, source, sink, volunteer_nodes, task_nodes = build_network(events, tasks, volunteers)
max_flow, assignments = edmonds_karp(graph, capacity, source, sink)

print(f"Maximum number of volunteer assignments: {max_flow}")

assigned_volunteers = {}
for (u, v), flow in assignments.items():
    if u in volunteer_nodes and v in task_nodes and flow > 0:
        if v not in assigned_volunteers:
            assigned_volunteers[v] = []
        assigned_volunteers[v].append(u)

print("\nVolunteer Assignments:")
for task_id, assigned_vols in assigned_volunteers.items():
    task = task_nodes[task_id]
    print(f"Task {task_id} ({task.task_type} for Event {task.event_id}): Assigned {len(assigned_vols)}/{task.required_volunteers} volunteers - {assigned_vols}")

print("\nUnderstaffed Tasks:")
for task_id, task in task_nodes.items():
    assigned_count = len(assigned_volunteers.get(task_id, []))
    if assigned_count < task.required_volunteers:
        print(f"Task {task_id} ({task.task_type} for Event {task.event_id}) is understaffed by {task.required_volunteers - assigned_count} volunteers.")