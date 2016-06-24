def pattern15(n,x=1,y=1,*args):
    if n == 1:
        return '1' + '\n' * (y-1)
    l = []
    for i in range(0,n):
        q = n - i
        s = " " * (q - 1)
        s += str((n - i) % 10)
        s += " " * (n - q)
        s = s + s[:-1][::-1]
        j = s[1:]
        for i in range(1,x):
            s += j
        l += [s]
    l = l[1:][::-1] + l
    z = l[1:]
    for i in range(1,y):
        l += z
    return "\n".join(l)