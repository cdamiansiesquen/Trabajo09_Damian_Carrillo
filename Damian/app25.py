import libreria
import  os

m=int(os.sys.argv[1])
g=int(os.sys.argv[2])
h=int(os.sys.argv[3])

s=libreria.presion_hidros(m,g,h)
num="La multiplicacion de {}, {} y {} resulta la distancia: {}"
print(num.format(m,g,h,s))
