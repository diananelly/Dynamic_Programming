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

# Example graph with a possible negative cycle
graph = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 8],
    [float('inf'), 1, 0, -4],  # Negative weight
    [float('inf'), float('inf'), 2, 0]
]

shortest_paths, negative_cycle = floyd_warshall(graph)

if negative_cycle:
    print("Negative cycle detected!")
else:
    print("Shortest Path Matrix:")
    for row in shortest_paths:
        print(row)