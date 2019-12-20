import libreria
import  os

a= int(os.sys.argv[1])
b= int(os.sys.argv[2])
c= int(os.sys.argv[3])
d= int(os.sys.argv[4])

s= libreria.promedio(a,b,c,d)
num= "La suma de {}, {}, {} y {} sobre 4 resulta de promedio: {}"
print(num.format(a,b,c,d,s))
