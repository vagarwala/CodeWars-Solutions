import math

def factors(n):
    return [[i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]