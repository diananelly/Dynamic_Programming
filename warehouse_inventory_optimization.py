def maximize_profit(capacity, budget, items):
    dp = [[0] * (capacity + 1) for _ in range(budget + 1)]

    for cost, revenue, weight in items:
        profit = revenue - cost
        for c in range(cost, budget + 1):
            for w in range(weight, capacity + 1):
                dp[c][w] = max(dp[c][w], dp[c - cost][w - weight] + profit)

    return dp[budget][capacity]

# test cases
# (cost, revenue, weight)
items = [
    (5, 10, 3), #profit = 5
    (4, 7, 2), #profit = 3
    (7, 14, 5) #profit = 7
]
capacity = 10
budget = 15
print("Max Profit(Test 1): Expected 15")
print(maximize_profit(capacity, budget, items))  # Expected: Maximum profit achievable
print()

# Valid Test Case
items1 = [
    (3, 8, 2),  # (cost, revenue, weight) -> profit = 5
    (6, 12, 4), # profit = 6
    (2, 5, 1)   # profit = 3
]
capacity1 = 7
budget1 = 10
print("Max Profit(Test 2): Expected 16")
print(maximize_profit(capacity1, budget1, items1))  # expected:max profit achievable == 16
print()
# impossible test case
items2 = [
    (5, 6, 3),
    (7, 9, 4)
]
capacity2 = 2  # too low
budget2 = 3  # too low
print("Max Profit(Test 3): Expected 0 because its impossible")
print(maximize_profit(capacity2, budget2, items2))  # expected: 0
print()