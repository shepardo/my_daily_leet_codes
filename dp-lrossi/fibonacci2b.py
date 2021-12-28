import inspect
def stack_depth():
    return len(inspect.getouterframes(inspect.currentframe()))

def fibonacci(n):
    print("{indent}fibonacci({n}) called".format(indent=" " * stack_depth(), n=n))
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(6)

