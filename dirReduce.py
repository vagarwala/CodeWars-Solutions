def dirReduce(L):
    def remov(L, direct1, direct2):
        for i in range(len(L) - 1):
            if L[i] == direct1 and L[i+1] == direct2:
                L.pop(i)
                L.pop(i)
        return L
    while len(L) > 4:
        remov(L, 'NORTH', 'SOUTH')
        remov(L, 'SOUTH', 'NORTH')
        remov(L, 'EAST', 'WEST')
        remov(L, 'WEST', 'EAST')
    return L