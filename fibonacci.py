#Program to display the Fibonacci sequence up to n-th term where n is provided by user

#Fn = Fn-1 + Fn-2

n=int(input('Enter number of terms required: '))
print('n: ', n)
a=0
b=1
if n<0:
    print('Invalid input')
elif n==0 or n==1:
    print('Fibonacci sequence: ')
    print(a)
else:
    print('Fibonacci sequence: ')
    print(a)
    print(b)

    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)