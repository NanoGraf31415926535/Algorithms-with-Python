def orientation(p, q, r):
    """
    Determines the orientation of an ordered triplet of points (p, q, r).
    Returns 0 if collinear, 1 if clockwise, 2 if counter-clockwise.
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    elif val > 0:
        return 1  # Clockwise
    else:
        return 2  # Counter-clockwise

# Example Usage:
if __name__ == "__main__":
    p1 = (0, 0)
    q1 = (1, 1)
    r1 = (2, 2)
    print(f"Orientation of {p1}, {q1}, {r1}: {orientation(p1, q1, r1)}")  # Output: 0

    p2 = (0, 0)
    q2 = (1, 0)
    r2 = (1, 1)
    print(f"Orientation of {p2}, {q2}, {r2}: {orientation(p2, q2, r2)}")  # Output: 2

    p3 = (0, 0)
    q3 = (1, 0)
    r3 = (0, -1)
    print(f"Orientation of {p3}, {q3}, {r3}: {orientation(p3, q3, r3)}")  # Output: 1

def on_segment(p, q, r):
    """
    Checks if point q lies on line segment pr.
    Assumes that points p, q, and r are collinear.
    """
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

# Example Usage (assuming collinearity from previous example):
if __name__ == "__main__":
    p1 = (0, 0)
    q1 = (1, 1)
    r1 = (2, 2)
    print(f"Is {q1} on segment {p1}-{r1}? {on_segment(p1, q1, r1)}")  # Output: True

    p4 = (0, 0)
    q4 = (3, 3)
    r4 = (2, 2)
    print(f"Is {q4} on segment {p4}-{r4}? {on_segment(p4, q4, r4)}")  # Output: False

def do_intersect(p1, q1, p2, q2):
    """
    Checks if line segment p1q1 and p2q2 intersect.
    """
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases for collinear points
    # p1, q1, p2 are collinear and p2 lies on segment p1q1
    if o1 == 0 and on_segment(p1, p2, q1): return True

    # p1, q1, q2 are collinear and q2 lies on segment p1q1
    if o2 == 0 and on_segment(p1, q2, q1): return True

    # p2, q2, p1 are collinear and p1 lies on segment p2q2
    if o3 == 0 and on_segment(p2, p1, q2): return True

    # p2, q2, q1 are collinear and q1 lies on segment p2q2
    if o4 == 0 and on_segment(p2, q1, q2): return True

    return False  # Doesn't fall in any of the above cases

# Example Usage:
if __name__ == "__main__":
    p1 = (1, 1)
    q1 = (10, 1)
    p2 = (1, 2)
    q2 = (10, 2)
    print(f"Do ({p1}, {q1}) and ({p2}, {q2}) intersect? {do_intersect(p1, q1, p2, q2)}")  # Output: False

    p3 = (1, 1)
    q3 = (10, 1)
    p4 = (5, 0)
    q4 = (5, 5)
    print(f"Do ({p3}, {q3}) and ({p4}, {q4}) intersect? {do_intersect(p3, q3, p4, q4)}")  # Output: True

    p5 = (0, 0)
    q5 = (2, 0)
    p6 = (1, 0)
    q6 = (3, 0)
    print(f"Do ({p5}, {q5}) and ({p6}, {q6}) intersect? {do_intersect(p5, q5, p6, q6)}")  # Output: True (collinear overlap)