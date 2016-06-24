from fractions import Fraction
def game(n):
    total = sum([(i + 0.5) for i in range(n)])
    res = str(Fraction(total).limit_denominator()).split('/')
    return [int(x) for x in res]