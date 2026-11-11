# A pair (i, j) is a mirror pair if i < j and A[i] == reverse(A[j]),
# for example reverse(123) = 321. Count the mirror pairs in an array.

def count_mirror_pairs(arr):
    freq = {}
    count = 0

    for num in arr:
        rev = int(str(num)[::-1])
        if rev in freq:
            count += freq[rev]

        freq[num] = freq.get(num, 0) + 1

    return count


# Input
arr = [12, 21, 30, 3, 45, 54]
print(count_mirror_pairs(arr))

