def to_minutes(h, m):
    # adjust minutes overflow / underflow
    h = h + m // 60
    m = m % 60
    return h * 60 + m


n = int(input())
total = 0

for _ in range(n):
    start, end = input().split()

    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))

    start_time = to_minutes(sh, sm)
    end_time = to_minutes(eh, em)

    if start_time < end_time:
        total += end_time - start_time

print(total)
