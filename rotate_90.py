# Rotate an N x N matrix 90 degrees clockwise, in place, without a second matrix.

def rotate_90_clockwise(matrix):
    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse rows
    for row in matrix:
        row.reverse()



n = int(input("Enter the matrix size: "))

matrix = []
print("Enter the matrix elements row-wise:")

for i in range(n):
    while True:
        row = list(map(int, input().split()))
        if len(row) == n:
            matrix.append(row)
            break
        else:
            print(f"Please enter exactly {n} elements for row {i+1}")

# -------- PROCESS --------
rotate_90_clockwise(matrix)

# -------- OUTPUT --------
print("After matrix:")
for row in matrix:
    print(*row)
