def maximize_profit(capacity, budget, items):
    # Initialize DP table
    dp = [[0] * (capacity + 1) for _ in range(budget + 1)]

    for cost, revenue, weight in items:
        profit = revenue - cost
        for c in range(cost, budget + 1):
            for w in range(weight, capacity + 1):
                dp[c][w] = max(dp[c][w], profit + dp[c - cost][w - weight])

    return dp[budget][capacity]


# Test Case
items = [
    (5, 10, 3),  # (cost, revenue, weight)
    (4, 7, 2),
    (7, 14, 5)
]
capacity = 10
budget = 15

print(maximize_profit(capacity, budget, items))