n = int(input("Enter the number: "))
f = 1
i = 1

while i <= n:
    f *= i
    i += 1

print(f"The factorial of {n} is {f}")
