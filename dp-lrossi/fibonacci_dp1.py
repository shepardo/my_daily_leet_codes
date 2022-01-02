# dynamic programming, bottom up
def fibonacci(n):
    series = [1, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    return series[-1]

print(fibonacci(6))
print(fibonacci(10))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(4))
