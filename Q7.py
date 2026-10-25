n = int(input("Enter an integer: "))
if n <= 1:
    print("Invalid input")
else:
    prime = True
    i = 2
    while i < n:
        if n%i == 0:
            prime = False 
            break
        i += 1

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")