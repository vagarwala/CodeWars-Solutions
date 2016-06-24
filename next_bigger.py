def next_bigger(n):
    s = list(str(n))[::-1]
    for i in range(len(s) - 1):
        if int(s[i+1]) < int (s[i]):
            temp = s[i+1]
            s[i+1] = s[i]
            s[i] = temp
            return int(''.join(s)[::-1])
    return -1