def rotate_270(matrix):
    n = len(matrix)

    # Step 1: Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse columns
    for j in range(n):
        for i in range(n // 2):
            matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]


# -------- INPUT --------
n = int(input("Enter matrix size: "))
print("Enter matrix elements row-wise:")

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# -------- PROCESS --------
rotate_270(matrix)

# -------- OUTPUT --------
print("Matrix after 270 degree rotation:")
for row in matrix:
    print(*row)
