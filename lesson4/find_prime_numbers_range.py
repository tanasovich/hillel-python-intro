a, b = map(int, input("Write numbers A and B (A < B) separated by space: ").split())

prime_numbers: list = []

for number in range(a, b + 1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime_numbers.append(number)

print(' '.join(map(str, prime_numbers)))
