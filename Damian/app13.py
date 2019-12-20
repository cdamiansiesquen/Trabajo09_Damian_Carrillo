import libreria
import os
x= int(os.sys.argv[1])
y= int(os.sys.argv[2])

s=libreria.semisuma(x,y)
num="La multiplicacion de {} y {} sobre 2 resulta: {}"
print(num.format(x,y,s))
