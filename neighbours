def simulate(arr, K):
    n = len(arr)

    for _ in range(K):
        new_arr = arr[:]   # copy to preserve simultaneity

        for i in range(n):
            left = arr[(i - 1) % n]
            right = arr[(i + 1) % n]

            if arr[i] > left and arr[i] > right:
                new_arr[i] -= 2
                new_arr[(i - 1) % n] += 1
                new_arr[(i + 1) % n] += 1

            elif arr[i] < left and arr[i] < right:
                new_arr[i] += 2
                new_arr[(i - 1) % n] -= 1
                new_arr[(i + 1) % n] -= 1

        arr = new_arr   # move to next round

    return arr


# Input
arr = [4, 1, 7, 3, 5]
K = 3

# Output
print(*simulate(arr, K))
