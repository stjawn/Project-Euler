# Euler discovered the remarkable quadratic formula: n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39
#
# The incredible formula was discovered, n^2 - 79n + 1601
# which produces 80 primes for the consecutive values 0<=n<=79
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form n^2 + an + b, where |a| and |b| < 1000
# Find the product of coefficients a and b that produces the maximum number of primes for consecutive values of n starting with n = 0


def sieveOfEratosthenes(n):
    integers = [i for i in range(3,n+1,2)]
    integers.insert(0,2)
    p = 3
    while p**2 <= n:
        k = integers.index(p)
        for i in integers[k+1:]:
            if i % p == 0:
                integers.remove(i)
        p = integers[k+1]
    return integers


def isPrime(n):
    if n in sieveOfEratosthenes(n):
        return True
    return False


def quadraticPrimes(coefficient_bound):
    Pbest = list()
    for a in range(-coefficient_bound+1,coefficient_bound):
        for b in range(-coefficient_bound+1,coefficient_bound):
            n = 0
            P = list()
            while isPrime(n**2 + a*n + b) == True:
                P.append(n**2 + a*n + b)
                n += 1
            if len(P) > len(Pbest):
                Pbest = P
                best_coefficients = (a,b)
                print('best: ', best_coefficients, len(Pbest), Pbest)
    return best_coefficients


print(quadraticPrimes(1000))
