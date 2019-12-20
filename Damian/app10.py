import libreria
import os

m= int(os.sys.argv[1])
g= int(os.sys.argv[2])

s=libreria.peso(m,g)
num="La multiplicacion de {} y {} resulta el peso de : {}"
print(num.format(m,g,s))
