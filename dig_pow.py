def dig_pow(n, p):
    num = list(str(n))
    res = sum([int(num[i])** (p + i) for i in range(len(num))])
    if res % n == 0:
        return res/n
    else:
        return -1