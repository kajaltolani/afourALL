#yield operator

a=input('enter name')
def userinfo():
    if a=='kajal':
        yield a
    else:
        print('invalid')
b=userinfo()
print(b)