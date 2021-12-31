def cached(f):
    cache = {}

    def worker(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    
    return worker

@cached
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
print(fibonacci(10))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(4))
    