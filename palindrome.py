'''Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
For example, is_palindrome("radar") should return True.'''


input_str=input('Enter a string: ')
reversed_str=input_str[::-1]            #to reverse string

def is_palindrome(str):
    if input_str==reversed_str:         #check if input string equals reversed string
        print('It is a palindrome')
    else:
        print('It is not a palindrome')
is_palindrome(str)
