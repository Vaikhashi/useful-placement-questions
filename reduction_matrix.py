# Given a 3x3 matrix of positive integers. For value 1, then 2, then 3 and so on:
# find the cell with that value and decrease its up, down, left and right
# neighbours by 1. If a neighbour would go negative, it is not possible.
# Decide whether the whole matrix can be reduced to zeros this way.

def reduce_matrix(mat):
    n = 3

    # find maximum value in matrix
    max_val = 0
    for row in mat:
        for x in row:
            if x > max_val:
                max_val = x

    # process values from 1 to max_val
    for k in range(1, max_val + 1):
        for i in range(n):
            for j in range(n):
                if mat[i][j] == k:

                    # check all 4 directions
                    if i > 0:
                        if mat[i-1][j] == 0:
                            return "NOT POSSIBLE"
                        mat[i-1][j] -= 1

                    if i < n-1:
                        if mat[i+1][j] == 0:
                            return "NOT POSSIBLE"
                        mat[i+1][j] -= 1

                    if j > 0:
                        if mat[i][j-1] == 0:
                            return "NOT POSSIBLE"
                        mat[i][j-1] -= 1

                    if j < n-1:
                        if mat[i][j+1] == 0:
                            return "NOT POSSIBLE"
                        mat[i][j+1] -= 1

    # check if all elements are zero
    for row in mat:
        for x in row:
            if x != 0:
                return "NOT POSSIBLE"

    return "POSSIBLE"


print(reduce_matrix([[1, 1, 0], [1, 0, 0], [0, 0, 0]]))
