def last_digit(num1, num2):
    if num2 == 0: return 1
    if num2 == 1: return num1 % 10
    if num1 % 10 == 0: return 0
    if num1 % 10 == 1: return 1
    if num1 % 10 == 6: return 6

    num1 = num1 % 10
    
    def last_digit_help(n1, n2):
        nums = [1]
        i = 1
        while True:
            if (nums[i-1] * n1) % 10 not in nums:
                nums.append((nums[i-1] * n1) % 10)
                i += 1
            else:
                start = (nums[i-1] * n1) % 10
                ind = nums.index(start)
                nums = nums[ind:]
                break
        return nums[(n2-ind) % len(nums)]
    
    return last_digit_help(num1, num2)