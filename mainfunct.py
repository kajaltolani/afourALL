
def is_palindrome(user_input):
    if user_input==user_input[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_palindrome('radar'))
    print( is_palindrome('abc'))