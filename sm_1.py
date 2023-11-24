def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

fibonacci_numbers = list(fibonacci(200))
print(fibonacci_numbers[-1])