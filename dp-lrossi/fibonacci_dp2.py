def fibonacci(n):
    previous = 1
    current = 1
    for i in range(n - 2):
        next = current + previous
        previous, current = current, next
    return current

print(fibonacci(6))
print(fibonacci(10))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(4))
