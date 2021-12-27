fibonacci_cache = {}
def fibonacci(n):
    if n <= 2:
        return 1
    if n not in fibonacci_cache:
        fibonacci_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci_cache[n]

print(fibonacci(6))
print(fibonacci(10))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(4))

