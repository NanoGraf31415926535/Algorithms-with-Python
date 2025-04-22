def fibonacci_dp_memoization(n, memo={}):
    """Calculates the nth Fibonacci number using memoization (top-down DP)."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_dp_memoization(n - 1, memo) + fibonacci_dp_memoization(n - 2, memo)
    return memo[n]

def fibonacci_dp_tabulation(n):
    """Calculates the nth Fibonacci number using tabulation (bottom-up DP)."""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def knapsack_01_dp(capacity, weights, values):
    """Solves the 0/1 Knapsack problem using dynamic programming."""
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def longest_common_subsequence_dp(s1, s2):
    """Finds the length of the Longest Common Subsequence (LCS) using DP."""
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def edit_distance_dp(s1, s2):
    """Calculates the Edit Distance between two strings using DP."""
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i  # Cost to transform s1[0..i-1] to empty string
    for j in range(n + 1):
        dp[0][j] = j  # Cost to transform empty string to s2[0..j-1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # Deletion
                                   dp[i][j - 1],      # Insertion
                                   dp[i - 1][j - 1])  # Substitution

    return dp[m][n]

# Example Usage:
if __name__ == "__main__":
    # Fibonacci
    n_fibonacci = 10
    print(f"Fibonacci({n_fibonacci}) (Memoization):", fibonacci_dp_memoization(n_fibonacci))
    print(f"Fibonacci({n_fibonacci}) (Tabulation):", fibonacci_dp_tabulation(n_fibonacci))

    # Knapsack 0/1
    capacity_knapsack = 50
    weights_knapsack = [10, 20, 30]
    values_knapsack = [60, 100, 120]
    max_value = knapsack_01_dp(capacity_knapsack, weights_knapsack, values_knapsack)
    print("Knapsack 0/1 Max Value:", max_value)

    # Longest Common Subsequence
    s1_lcs = "AGGTAB"
    s2_lcs = "GXTXAYB"
    lcs_length = longest_common_subsequence_dp(s1_lcs, s2_lcs)
    print(f"Length of LCS of '{s1_lcs}' and '{s2_lcs}':", lcs_length)

    # Edit Distance
    s1_edit = "kitten"
    s2_edit = "sitting"
    edit_dist = edit_distance_dp(s1_edit, s2_edit)
    print(f"Edit Distance between '{s1_edit}' and '{s2_edit}':", edit_dist)