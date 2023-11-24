def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_numbers = list(fib(200))

with open("fib.txt", "w") as file:
    for num in fib_numbers:
        file.write(str(num) + "\n")

print(fib_numbers[-1])