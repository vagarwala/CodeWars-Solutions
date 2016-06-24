def pattern16(n):
    if n <= 0:
        return ''
    else:
        nums = [i % 10 for i in range(1, n+1)][::-1]
        lines = ''
        for i in range(n):
            for j in range(i):
                lines += str(nums[j])
            lines += (n-i)*str(nums[i])
            lines += '\n'
        return lines[:-1]