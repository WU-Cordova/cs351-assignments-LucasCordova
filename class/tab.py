# Function to solve the 0/1 knapsack problem using tabulation
from typing import List


def knapsack_tabulation(W: int, weights: List[int], values: List[int]) -> int:
    n: int = len(weights)
    
    # Initialize a DP table (n+1) x (W+1) with all zeros
    dp: List[List[int]] = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build the DP table iteratively
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                # Max value of including or excluding the current item
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]
    
    # The maximum value will be in dp[n][W]
    return dp[n][W]

# Example usage
weights: List[int] = [1, 2, 3, 8]
values: List[int] = [20, 30, 50, 100]
W: int = 5

# Calling the tabulation function
max_value: int = knapsack_tabulation(W, weights, values)
print(f"Max value (Tabulation): {max_value}")