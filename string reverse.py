'''Define a function reverse() that computes the reversal of a string.
For example, reverse("I am testing") should return the string "gnitset ma I"'''

#using slicing operator

input_str1=input('Enter user string. ')
print(f'Input string is: {input_str1}')

def rev_func1(n):
    reversed_str1=input_str1[::-1]
    print(f'Reversed string is: {reversed_str1}')

rev_func1(input_str1)

#using for loop
def rev_func2(input_str2):
    reversed_str2= ""
    for i in input_str2:
        reversed_str2=i+reversed_str2
    print(f'Reversed string is: {reversed_str2}')

input_str2=input('Enter user string. ')
print(f'Input string is: {input_str2}')
rev_func2(input_str2)