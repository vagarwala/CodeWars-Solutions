def sol_equa(n):
    facts = factors(n)
    res = []
    for [i, j] in facts:
        if math.fabs(i-j) % 4 == 0:
            y = (max(i, j) - min(i, j)) / 4
            x = max(i, j) - 2*y
            res.append([x, y])            
    return res