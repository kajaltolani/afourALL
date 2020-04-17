#Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
from pip._vendor.distlib.compat import raw_input

mylist = []

def get_list(list1):
    #returns list of strings provided by user
    n=int(input('How many words in list?: '))

    for i in range(n):
        word = raw_input('Enter the word: ')
        mylist.append(word)
    return mylist

print(get_list(mylist))

def max_word_length(user_len):
    #returns length of longest word in the list
    temp_len=0
    for i in range(len(mylist)):
        if len(mylist[i])>temp_len:
            temp_len=len(mylist[i])
            i+=1
        else:
            i+=1
    return temp_len

print(f'Length of longest word in list: {max_word_length(len(mylist))}')