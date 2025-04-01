import numpy as np

def floyd_warshall(graph):
    V = len(graph)
    dp = np.copy(graph)  # Initialize distance matrix

    for k in range(V):  # Intermediate node
        for i in range(V):  # Source node
            for j in range(V):  # Destination node
                if dp[i][k] != float('inf') and dp[k][j] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    # Detect negative cycles
    for i in range(V):
        if dp[i][i] < 0:
            return None, True  # Indicating a negative cycle exists

    return dp, False  # Return shortest paths and no negative cycle

# Test case 1: a standard graph with no negative cycle
graph1 = [
    [0, 3, float('inf'), 5],
    [float('inf'), 0, 2, 8],
    [float('inf'), float('inf'), 0, 2],
    [float('inf'), float('inf'), float('inf'), 0]
]

shortest_paths, negative_cycle = floyd_warshall(graph1)
print("\nTest Case 1: No Negative Cycles")
if negative_cycle:
    print("Negative cycle detected!")
else:
    for row in shortest_paths:
        print(row)

# Test case 2: graph with a possible negative cycle
graph2 = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 8],
    [float('inf'), 1, 0, -4],  # Negative weight
    [float('inf'), float('inf'), 2, 0]
]

shortest_paths, negative_cycle = floyd_warshall(graph2)
print("\nTest Case 2: Graph with Negative Cycle")
if negative_cycle:
    print("Negative cycle detected!")
else:
    for row in shortest_paths:
        print(row)

#Test case 3: a fully connected graph
graph3 = [
    [0, 2, 3, float('inf')],
    [2, 0, float('inf'), 4],
    [3, float('inf'), 0, 1],
    [float('inf'), 4, 1, 0]
]

shortest_paths, negative_cycle = floyd_warshall(graph3)
print("\nTest Case 3: Fully Connected Graph")
if negative_cycle:
    print("Negative cycle detected!")
else:
    for row in shortest_paths:
        print(row)