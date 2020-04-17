#if elif else

'''x=8

if x==1:
    print('x is 1')

elif x==2:
    print('x is 2')

elif x==3:
    print('x is 3')

else:
    print('wrong input')'''


##########################################
#while loop

'''i=1

while i<=5:
    print('Hey there ',end='')

    j=1
    while j<=2:
        print('new ',end='')
        j+=1

    i+=1
    print()
#####################################
counter = 1
while counter<=100:
    if counter%3==0:
        print('number div by 3')
    elif counter%5==0:
        print('number div by 5')
    else:
        print(counter)
    counter+=1

######################################
hash_row = 4
while hash_row >= 1:
    hash_column = 5
    while hash_column >= 1:
        print('# ', end='')
        hash_column-=1
    hash_row-=1
    print()

# for loop

x = ['kajal', 3, 'tolani', 89.903]

for i in x:
    print(i)

for k in range(1,21):
    if k%5!=0:
        print(k)

#print perfect square number between 0 to 500
import math
for i in range(0,501):
    if math.sqrt(i)==math.floor(math.sqrt(i)):
        print(i)

#break, pass, continue

av = 5
x = int(input('How many candies do you want? '))
i = 1
while i<=x:
    if i>av:
        print('out of stock')
        break
    print('candy')
    i+=1
print('see you')

i = 1
while i<10:
    if i==6:
        continue
    else:
        print(i)
    i+=1

for i in range(4,0,-1):
    for j in range(i):
        print('# ', end='')

    print()

for i in range(1, 5):
    print(i, end = " ")
    for j in range(1+i, 5):
        print(j, end = " ")
    print()

#########################################
#for else

list1 = [24,433,4534,4432,302]

for i in list1:
    if i % 5 == 0:
        print(i)
        break
else:
    print('not found')

x = int(input('enter the number : '))
for i in range(2,x):
    if x % i == 0:
        print(x, ' is not a prime number')
        break
else:
    print(x, ' is a prime number')

#user input

from array import *
myarray = array('i',[])

n = int(input('Enter the length of array: '))

for i in range(n):
    x = int(input('Enter the next value: '))
    myarray.append(x)
print('myarray: ', myarray)'''

from numpy import *
arr = array([1,2,3,4])
print(arr)

lin = linspace(1,16,16)
print(lin)

aran = arange(0,16,2)
print(aran)

logs = logspace(1,20,5)
print(logs)
print('%.2f' %logs[1])

zer = zeros(4, int)
print(zer)

ones = ones(5)
print(ones)

tup = (1,3,4,34,21,2,3)
print(tup.count(3))
print(tup.index(34))








