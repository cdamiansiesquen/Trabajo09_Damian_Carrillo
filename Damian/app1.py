import libreria
import os

v= int(os.sys.argv[1])
t= int(os.sys.argv[2])

s=libreria.distancia(v,t)
num="La multiplicacion de {} y {} resulta la distancia: {}"
print(num.format(v,t,s))
