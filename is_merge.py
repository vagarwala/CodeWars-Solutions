def is_merge(s, part1, part2):
    for i in range(len(s)):
        if part1 == '':
            return part2 == s[i:]
        elif part2 == '':
            return part1 == s[i:]
        elif s[i] == part1[0]:
            part1 = part1[1:]
        elif s[i] == part2[0]:
            part2 = part2[1:]
        else:
            return False
    if part1 == part2 and part1 == '':
        return True
    else:
        return sorted(s) == sorted(part1 + part2)