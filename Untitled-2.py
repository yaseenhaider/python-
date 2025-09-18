

num = int(input("Enter an integer: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is NOT a Prime number")
            break
    else:
        print(num, "is a Prime number")
else:
    print(num, "is NOT a Prime number")
