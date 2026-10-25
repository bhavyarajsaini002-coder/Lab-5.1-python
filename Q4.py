N = int(input("Enter a positive integer: "))
if N < 0:
    print("Invalid input")
else:
    fact = 1
    i = 1
    while i <= N:
        fact = fact*i
        i= i+1
    print("factorial=",fact)