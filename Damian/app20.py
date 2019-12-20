import libreria
import os

f=int(os.sys.argv[1])
a=int(os.sys.argv[2])

s=libreria.presion(f,a)
num="La multiplicacion de {} y {} resulta la presion: {}"
print(num.format(f,a,s))
