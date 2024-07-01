#coding=utf-8

import os, sys, platform

os.system('xdg-open https://facebook.com/groups/658593889736993/')

try:

    if sys.argv[1]=='update':

        os.system('rm -rf UMW64.cpython-311.so UUMX.cpython-311.so')

except:

    pass

os.system('rm -rf UMW64.cpython-311.so UUMX.cpython-311.so')

os.system('git pull')

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('UMW64.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/HUA-T3CH/UPDATE-WORKING/blob/main/UMW64.cpython-311.so > UMW64.cpython-311.so') 

        os.system("chmod 777 UMW64*")
        
        import UMW64

    else:

        import UMW64

elif bit == '32bit':

    if not os.path.isfile('UUMX.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/HUA-T3CH/UPDATE-WORKING/blob/main/UUMX.cpython-311.so > UUMX.cpython-311.so')

        os.system("chmod 777 UUMX*")

        import UUMX

    else:

        import UUMX
