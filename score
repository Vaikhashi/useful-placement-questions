def max_score(arr, K):
    score = 0

    for _ in range(K):
        mx = max(arr)          # choose largest
        i = arr.index(mx)

        take = mx // 2         # guaranteed part
        remain = mx - take    # opponent keeps this

        score += take
        arr[i] = remain       # put back into array

    return score


# Input
arr = [10, 7, 4, 9]
K = 5

print(max_score(arr, K))  # 16
