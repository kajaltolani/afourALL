#file-IO operations

import os

fileObject=open('filename','w+')            #open operation
fileObject.write('hello\nwelcome\n')
fileObject.write('to AFour Tech\n')


fileObject=open('filename','a+')            #append operation
fileObject.write('\nappend statement\n')

fileObject.seek(0)
#fileObject=open('filename','w+')
contents= fileObject.read()                 #read operation
print(contents)

fileObject.readlines()                      #readlines operation
for i in contents:
    print(i)

contents3= fileObject.read(15)              #read till count operation
print(contents3)

print(fileObject.tell())                    #position operation

print(fileObject.seek(21))                  #seek operation
print(fileObject.read())

fileObject.close()                          #close operation

os.rename('filename','newname' )            #rename operation

os.remove('newname')                        #remove operation

#os.remove('filename')
#os.remove('newname2')