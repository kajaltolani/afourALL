#Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

user_char=input('Enter a character: ')
vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def demo(user_char):
    if user_char in vowels_list:
        print(f'{user_char} IS a vowel')
    else:
        print(f'{user_char} is NOT a vowel')
if len(user_char)==1:
    demo(user_char)
else:
    print('Enter single character')