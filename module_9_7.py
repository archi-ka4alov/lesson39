def is_prime(func):
    def wrapper(*args):
        k = 0
        for i in range(2, func(*args) // 2 + 1):
            if func(*args) % i == 0:
                k = k + 1
        if k <= 0:
            print("Простое")
            return func(*args)

        else:
            print("Составное")
            return func(*args)
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


# result = sum_three(2, 3, 6)
# print(result)
print(sum_three(2, 3, 6))