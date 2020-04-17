#Error handling

import os
fileObject=open('filename2','w+')
fileObject.write('hello\nwelcome\n')
fileObject.close()          #if this is not present, except part will execute. Otherwise, else part will execute

os.remove('newname2')
try:
    os.rename('filename2','newname2' )
except:
    print('invalid')
else:
    print('success')
finally:
    print('hello again')
