def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
print(fibonacci(10))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(4))
