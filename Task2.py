number = [1,2,3,4,5,6,7,8,9]
even_sum = 0
odd_sum = 0
for num in number:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
