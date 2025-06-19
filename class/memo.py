from typing import List


def knapsack_memo(
    W: int, weights: List[int], values: List[int], n: int, memo: List[List[int]]) -> int:
    # Base case: If no items left or capacity is 0
    if n == 0 or W == 0:
        return 0
    
    # If the value is already computed, return it from memo table
    if memo[n][W] != -1:
        return memo[n][W]

    # If the current item's weight is more than the remaining capacity, exclude the item
    if weights[n - 1] > W:
        memo[n][W] = knapsack_memo(W, weights, values, n - 1, memo)
    else:
        # Otherwise, find the maximum value by either including or excluding the current item
        include_item = values[n - 1] + knapsack_memo(W - weights[n - 1], weights, values, n - 1, memo)
        exclude_item = knapsack_memo(W, weights, values, n - 1, memo)
        memo[n][W] = max(include_item, exclude_item)
    
    return memo[n][W]

# Driver function to initialize the memoization table and call the recursive function
def knapsack_memo_driver(W: int, weights: List[int], values: List[int]) -> int:
    n = len(weights)
    # Initialize a memoization table with -1, representing uncomputed subproblems
    memo: List[List[int]] = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
    return knapsack_memo(W, weights, values, n, memo)

weights: List[int] = [1, 2, 3, 8]
values: List[int] = [20, 30, 50, 100]
W: int = 5

max_value: int = knapsack_memo_driver(W, weights, values)
print(f"Max value (Memoization): {max_value}") # 80