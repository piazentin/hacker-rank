# https://www.hackerrank.com/challenges/staircase

n = int(input().strip())

for i in range(1, n + 1):
    print(' ' * (n - i) + '#' * i)
