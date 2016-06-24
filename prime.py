def prime(n):
    neg = False
    if n < 0:
        neg = True
        n *= -1
    primfac = []
    if n%2 == 0:
        primfac.append(2)
        n /= 2
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return [primfac, neg]