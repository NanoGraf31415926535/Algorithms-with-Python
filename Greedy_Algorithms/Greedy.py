import heapq  # Still useful for the Huffman Coding heap

def activity_selection_greedy_manual_sort(activities):
    """Selects max non-overlapping activities by manually finding earliest finish."""
    n = len(activities)
    if n == 0:
        return []

    remaining_activities = list(activities)
    selected_activities = []
    last_finish_time = -float('inf')

    while remaining_activities:
        earliest_finish_time = float('inf')
        earliest_finish_index = -1

        for i in range(len(remaining_activities)):
            start, finish = remaining_activities[i]
            if finish < earliest_finish_time:
                earliest_finish_time = finish
                earliest_finish_index = i

        if earliest_finish_index == -1:
            break

        selected_activity = remaining_activities.pop(earliest_finish_index)
        start, finish = selected_activity

        if start >= last_finish_time:
            selected_activities.append(selected_activity)
            last_finish_time = finish

    return selected_activities

def fractional_knapsack_greedy_manual_sort(capacity, items):
    """Fractional knapsack by manually finding highest value-to-weight ratio."""
    n = len(items)
    if n == 0 or capacity == 0:
        return 0, {}

    remaining_items = list(items)
    total_value = 0
    remaining_capacity = capacity
    fractions = {}

    while remaining_items and remaining_capacity > 0:
        best_ratio = -1
        best_item_index = -1

        for i in range(len(remaining_items)):
            weight, value = remaining_items[i]
            if weight > 0:
                ratio = value / weight
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_item_index = i

        if best_item_index == -1:
            break

        best_weight, best_value = remaining_items.pop(best_item_index)

        if best_weight <= remaining_capacity:
            total_value += best_value
            remaining_capacity -= best_weight
            fractions[(best_weight, best_value)] = 1.0
        else:
            fraction = remaining_capacity / best_weight
            total_value += fraction * best_value
            fractions[(best_weight, best_value)] = fraction
            remaining_capacity = 0

    return total_value, fractions

def huffman_coding_greedy_manual_sort(frequencies):
    """Huffman coding by manually finding two smallest frequencies."""
    heap = [[freq, [symbol, ""]] for symbol, freq in frequencies.items()]
    heapq.heapify(heap)  # Using heapq is still efficient for repeated min finding

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def coin_change_greedy_manual_sort(coins, amount):
    """Coin change by manually finding largest denominations."""
    sorted_coins = []
    temp_coins = list(coins)
    while temp_coins:
        largest_coin = -1
        largest_index = -1
        for i in range(len(temp_coins)):
            if temp_coins[i] > largest_coin:
                largest_coin = temp_coins[i]
                largest_index = i
        if largest_index != -1:
            sorted_coins.append(temp_coins.pop(largest_index))

    num_coins = 0
    change = {}

    for coin in sorted_coins:
        while amount >= coin:
            amount -= coin
            num_coins += 1
            change[coin] = change.get(coin, 0) + 1

    if amount == 0:
        return num_coins, change
    else:
        return -1, {}

# Example Usage:
if __name__ == "__main__":
    # Activity Selection
    activities_ms = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    selected_ms = activity_selection_greedy_manual_sort(activities_ms)
    print("Selected Activities (Greedy - Manual Sort):", selected_ms)

    # Fractional Knapsack
    capacity_fk_ms = 50
    items_fk_ms = [(10, 60), (20, 100), (30, 120)]  # (weight, value)
    max_value_fk_ms, fractions_fk_ms = fractional_knapsack_greedy_manual_sort(capacity_fk_ms, items_fk_ms)
    print("Fractional Knapsack Max Value (Manual Sort):", max_value_fk_ms)
    print("Fractions Taken (Manual Sort):", fractions_fk_ms)

    # Huffman Coding (using heapq for efficiency of repeated min finding)
    frequencies_hc_ms = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    codes_hc_ms = huffman_coding_greedy_manual_sort(frequencies_hc_ms)
    print("Huffman Codes (Manual Sort - using heapq):", codes_hc_ms)

    # Coin Change
    coins_cc_ms = [1, 5, 10, 25]
    amount_cc_ms = 49
    num_coins_cc_ms, change_cc_ms = coin_change_greedy_manual_sort(coins_cc_ms, amount_cc_ms)
    print(f"Coin Change for {amount_cc_ms} (Manual Sort): {num_coins_cc_ms} coins, breakdown: {change_cc_ms}")

    coins_cc_fail_ms = [3, 4]
    amount_cc_fail_ms = 6
    num_fail_ms, change_fail_ms = coin_change_greedy_manual_sort(coins_cc_fail_ms, amount_cc_fail_ms)
    print(f"Coin Change for {amount_cc_fail_ms} ({coins_cc_fail_ms}) (Manual Sort): {num_fail_ms} coins, breakdown: {change_fail_ms}")