'''from filecmp import cmp
import math

def addition(x,y=8):
    'return x plus y'
    print('x: ', x)
    print('y: ', y)
    return x+y

print('x+y: ',addition(4,5))

print(addition.__doc__)

def add(a, b, c=0, d=0):
	return (a-b)+(c-d)

print (add(4,2,6,5))
print (add(4,2,d=18,c=12))

def abc(m,n):
    return str (m)+str (n)

print(abc.__doc__)

print(abc('kajal', 'tolani'))

newtup=('hi','hello',5,6,90.34,)
tup=(7,3,8)
print(newtup+tup[1:2])
cmp(newtup,tup)
print(cmp)

print(round(94.8056,2))

str1='hello-world'
print(str1.find('wo'))

str2='kajol'
print(str1[0], str2[-1])
print(str1[0:5])

print(str2.replace('k','K'))
print(str2.replace('t','T'))

str3= 'abc,def,ghi,jkl'
print(str3.split(','))

print(str2.count('a'))

print(min(str2))


#tuple
tup1=('a', 'b', 'c', 1,2,3)
print(tup1)
#print(type(tup1))

tup2=('kajal','tolani',27)
print(tup2)
print(tup1+tup2)

list1=[1,2,3,4,5]
print(type(list1))

list1.extend([6,7,8])
print(list1)

list1.append([9,10,11,12])
print(list1)

list1.remove([9,10,11,12])
print(list1)

dict1={'a':'apple','b':'ball' }
print(type(dict1))
dict1.update({'c':'camel'})
print(dict1)

#loops
a=0
while a<=10:
    print(f'a{a}= {a}')
    a+=1
else:
    print('bye')

a=['a','b','c']
for m in a:
    print(m)
print(len(a))

a = ['afour', 'tech', 'bavdhan']
b = a.__getitem__(1)
print(b)

def filter_long_word(words, n):
    return [word for word in words if len(word) > n]


if __name__ == '__main__':
    print(filter_long_word(['a','ExtraHop','python'],902))'''
from filecmp import cmp

dict1={"name":"kajal", "surname":"tolani", "age": 27, "address": "bavdhan"}
print(dict1)

dict2=dict1.copy()
print(dict2)

'''dict2.clear()
print(dict2)'''

dict2.update({"work":"AFour"})
print(dict2)

print(dict2['surname'])

del dict2['age']
print(dict2)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Students Name: %s" % Dict.items())

Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in Dict.keys():
    if key in Boys.keys():
        print(True)
    else:
        print(False)

students=Dict.keys()

a=dict2.sort()
print(a)