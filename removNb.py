def removNb(n):
    res = []
    tot = (n*(n+1))/2
    facts = factors(tot + 1)
    for [x, y] in facts:
        if (x-1 < n and y - 1 < n):
            res.append((x-1, y-1))
            if x != y:
                res.append((y-1, x-1))
    return sorted(res)