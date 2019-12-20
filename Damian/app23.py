import libreria
import os

f=int(os.sys.argv[1])
d=int(os.sys.argv[2])

s=libreria.trabajo(f,d)
num="La multiplicacion de {} y {} resulta el trabajo: {}"
print(num.format(f,d,s))
