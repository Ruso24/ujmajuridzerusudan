def generator (number):
    for n in range (2, number):
        for i in range(2, n):
            if n % i ==0:
                break
        else:
            yield n
prime_g = generator(100)
print(next(prime_g))
print(next(prime_g))
print(next(prime_g))
print(next(prime_g))
print(next(prime_g))
print(next(prime_g))
print(next(prime_g))
print(next(prime_g))
print(next(prime_g))