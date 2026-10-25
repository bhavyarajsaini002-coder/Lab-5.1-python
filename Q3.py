N = int(input("Enter N: "))

divisible = 0
not_divisible = 0

while True:
    num = int(input("Enter a number: "))
    if num == -999:
        break

    if num%N == 0:
        divisible += 1
    else:
        not_divisible += 1

print("Divisible:",divisible)
print("Not_divisible:",not_divisible)