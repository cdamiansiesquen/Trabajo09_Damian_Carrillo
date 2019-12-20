import libreria
import os

a=int(os.sys.argv[1])

s=libreria.cuadrado(a)
num="el numero {} al cuadrado es: {}"
print(num.format(a,s))

