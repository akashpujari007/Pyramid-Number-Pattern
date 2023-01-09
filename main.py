n = int(input())
i = 1
while i <= n:
    spaces = n - i
    while spaces > 0:
        print(' ', end='')
        spaces -= 1
    value = i
    while value > 0:
        print(value, end='')
        value = value - 1
    value += 2
    while value <= i:
        print(value, end='')
        value += 1
    print()
    i += 1