def sum_for_list(lst):
    primes = []
    for item in lst:
        primes += (prime(item)[0])
    primes = list(set(primes))
    res = []
    for p in primes:
        res.append([p, sum([x for x in lst if x%p == 0])])
    return sorted(res)