#Program to find the factorial of a number provided by user.

num1 = int(input('Enter a number: '))

factorial = 1

for num2 in range(1, num1+1):       #for loop, give upper limit +1 because it excludes the last one
    factorial=factorial*num2

print(f'Factorial of {num1} is: {factorial}')