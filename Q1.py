X = int(input("Enter X: "))
Y = int(input("Enter Y: "))
n = int(input("Enter n: "))
for i in range(X+1,Y+1):
    if i%n == 0:
        print(i)