def f(n, m):
    if m < n:
        return (m * (m-1)) / 2 + f(n - m, m)
    if m == n:
        return (n * (n-1)) / 2
    if m > n:
        return (n * (n+1)) / 2