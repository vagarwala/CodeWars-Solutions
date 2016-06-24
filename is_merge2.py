def is_merge2(s, part1, part2):
    s = list(s)
    part1 = list(part1)
    part2 = list(part2)
    if not sorted(s) == sorted(part1 + part2):
        return False
    for i in range(len(part1) - 1):
        if s.index(part1[i]) < s.index(part1[i+1]):
            s.remove(part1[i])
        else: return False
    s.remove(part1[len(part1)-1])
    return s == part2
