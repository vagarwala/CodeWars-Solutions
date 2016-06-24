def perimeter(n):
    a = 1
    b = 1
    fibonacci_numbers = [a, b]
    tot = 2
    for i in range(2,n+1):
        a, b = b, a+b
        fibonacci_numbers = [a, b]
        tot += b
    return 4*tot