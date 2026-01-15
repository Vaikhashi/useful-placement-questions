def rotate_180(matrix):
    # Reverse the matrix (top to bottom)
    matrix.reverse()
    # Reverse each row (left to right)
    for row in matrix:
        row.reverse()


# -------- INPUT --------
n = int(input("Enter matrix size: "))
print("Enter matrix elements row-wise:")

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# -------- PROCESS --------
rotate_180(matrix)

# -------- OUTPUT --------
print("Matrix after 180 degree rotation:")
for row in matrix:
    print(*row)
