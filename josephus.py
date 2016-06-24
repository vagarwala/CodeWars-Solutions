def josephus(items,k):
    l = len(items)
    index = l - 1
    count = l
    alive = list(items)
    dead = []
    while count > 0:
        index = (index + k) % count
        dead.append(alive[index])
        alive.pop(index)
        index -= 1
        count -= 1
    return dead