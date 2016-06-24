def order_weight(strng):
    if strng == '':
        return ''
    nums = strng.split(' ')
    nums = [int(x) for x in nums]
    def digitsum(x):
        return sum(map(int,str(x)))
    weight_num = [[digitsum(x), str(x)] for x in nums]
    weight_num.sort()
    res = [x[1] for x in weight_num]
    return ' '.join(res)