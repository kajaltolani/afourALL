#Python program to calculate Simple and Compound interest, Amount provided by the user.

'''SI = P*t*r
P = Principal amount
t = time in years
r = rate of interest in %

CI = P(1+r/n)**nt
P = Principal amount
t = time in years
r = rate of interest in %
n = number of times interest is compounded per unit time'''

P = int (input('Enter principal amount in Rupees P: '))
print('P: ', P)

t= int (input('Enter time in years t: '))
print('t: ', t)

r= int (input('Enter % rate of interest r: '))
print('r: ', int(r)/100)

n= int (input('Enter number of times interest is compounded per unit time n:  '))
print('n: ', n)

SI = P*t*r/100
print('Simple Interest: ', SI)

CI = P*((1+(r/(n*100)))**(n*t))
print('Compound Interest: ', CI)