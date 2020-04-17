'''Write a function filter_long_words() that takes a list of words
and an integer n and returns the list of words that are longer than n.'''
from pip._vendor.distlib.compat import raw_input

def filter_long_words():
    total=int(input('enter number of words in the list: '))
    print('List length: ',total)
    list1 = []

    for i in range(total):
        word = raw_input('enter the word: ')
        list1.append(word)
    print('List by user: ',list1)

    n = int(input('Enter a number for word limit: '))
    print('n: ', n)
    list2 = []

    for i in range(total):
        if n< list1[i].__len__():
            list2.append(list1.__getitem__(i))
    print('Desired list: ', list2)
    return list2

filter_long_words()







