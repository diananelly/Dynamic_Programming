def versioned_document_sync(A, B, insert_cost=1, delete_cost=1, replace_cost=1):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # set up the base case where A is empty, so we insert all lines from B
    for j in range(1, n + 1):
        dp[0][j] = j * insert_cost

    # set up the base case where B is empty, so we delete all lines from A
    for i in range(1, m + 1):
        dp[i][0] = i * delete_cost

    # fill out the dp table by considering all edit operations
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:  # if lines are the same, no change needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i][j - 1] + insert_cost,  # insert a line from B
                    dp[i - 1][j] + delete_cost,  # delete a line from A
                    dp[i - 1][j - 1] + replace_cost  # replace A's line with B's
                )

    return dp[m][n]

# test cases

# 1. same version (no edits needed)
A1 = ["line1", "line2", "line3"]
B1 = ["line1", "line2", "line3"]
print(versioned_document_sync(A1, B1))  # expected: 0

# 2. single insertion
A2 = ["line1", "line2"]
B2 = ["line1", "line2", "line3"]
print(versioned_document_sync(A2, B2))  # expected: 1 (insert "line3")

# 3. single deletion
A3 = ["line1", "line2", "line3"]
B3 = ["line1", "line3"]
print(versioned_document_sync(A3, B3))  # expected: 1 (delete "line2")

# 4. single replacement
A4 = ["line1", "line2", "line3"]
B4 = ["line1", "lineX", "line3"]
print(versioned_document_sync(A4, B4))  # expected: 1 (replace "line2" with "lineX")

# 5. completely different versions
A5 = ["apple", "banana", "cherry"]
B5 = ["x", "y", "z"]
print(versioned_document_sync(A5, B5))  # expected: 3 (replace all)

# 6. empty to non-empty
A6 = []
B6 = ["line1", "line2", "line3"]
print(versioned_document_sync(A6, B6))  # expected: 3 (insert all lines)

# 7. non-empty to empty
A7 = ["line1", "line2", "line3"]
B7 = []
print(versioned_document_sync(A7, B7))  # expected: 3 (delete all lines)

# 8. both empty
A8 = []
B8 = []
print(versioned_document_sync(A8, B8))  # expected: 0

# 9. custom cost: high replacement cost
A9 = ["a", "b", "c"]
B9 = ["a", "x", "c"]
print(versioned_document_sync(A9, B9, insert_cost=1, delete_cost=1, replace_cost=5))
# expected: 2 (delete "b" then insert "x" instead of replacing)

# 10. custom cost: cheap replacement
A10 = ["a", "b", "c"]
B10 = ["a", "x", "c"]
print(versioned_document_sync(A10, B10, insert_cost=3, delete_cost=3, replace_cost=1))
# expected: 1 (replace "b" with "x" since replacement is cheapest)
