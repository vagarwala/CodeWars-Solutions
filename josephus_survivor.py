def josephus_survivor(n,k):
    soldiers = range(1, n+1)
    index = n - 1
    count = n
    while count > 1:
        index = (index + k) % count
        soldiers.pop(index)
        index -= 1
        count -= 1
    return soldiers[0]