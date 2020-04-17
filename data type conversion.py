#Explore data type conversion and write simple python program on Data type conversion.

'''
Implicit Type Conversion: In Python, when the data type conversion takes place during compilation
or during the run time, then it’s called an implicit data type conversion.
Python handles the implicit data type conversion.
Python always converts smaller data type into larger data type to prevent the loss of data.
(e.g. in case of int and float, it will convert result into float to save the fractional part)
'''

x = int(10)
print('integer x: ', x)

y = float(20.5)
print('float y:', y)

z=x+y
print('result x+y=z:', z)

print('data type of z: ', type(z))    #command to check data type of variable


'''
Explicit Type Conversion: Explicit type conversion is also known as type casting.
Explicit type conversion takes place when the programmer clearly and explicitly defines the same in the program.
For explicit type conversion, there are some in-built Python functions.
'''

a = 50                #integer a
print('a: ', a)
print(type(a))

b= bin(a)             #explicitly converted to binary
print('binary value of a: ',b)

c = str(a)            #explicitly converted to string b
print(type(c))