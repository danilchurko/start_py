def shift(s, n):
    n = -n % len(s)
    return s[n:] + s[:n]


tupl = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print(shift(tupl, -3))
