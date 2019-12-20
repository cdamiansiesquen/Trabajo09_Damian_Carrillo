#ejercicio 1
# funcion que halla la distancia de 2 objetos
def distancia(v,t):
    resultado = v * t
    return resultado


# ejercicio 2
def promedio(a,b,c,d):
    prom= ((a + b + c + d)/ 4)
    return prom

# ejercicio 3
def pedir_año(b):
    if (len(b) == 4 ):
         if ( b.isdigit() == True ):
              res = b , " es valido ( es un numero)"
              return res
         else:
             res = b , " invalido (no es numero)"
             return res
     #fin_if
    else:
         res = b , " es invalido (no tiene 4 digitos)"
         return res

# ejercicio 4
def mayor(a,b):
    if (a > b):
        return a
    else:
        return b

# ejercicio 5
def nombre(x):
     if (x.isdigit() != False ):
         resultado = x , " es invalido ( es un numero)"
         return resultado
     else:
         resultado ="la cadena " , x , "es valido "
         return resultado
     #fin_if

# ejercicio 6
def ruc(a):
    if (len(a) == 11 ):
         if ( a.isdigit() == True ):
              resultado = a , " es valido"
              return resultado
         else:
              resultado = a , " invalido (no es numero)"
              return resultado
    #fin_if
    else:
         resultado = a , " es invalido (no tiene 11 digitos)"
         return resultado

# ejercicio 7
def pedir_dni(b):
    if (len(b) == 8 ):
         if ( b.isdigit() == True ):
              res = b , " es valido ( es un numero)"
              return res
         else:
              res = b , " invalido (no es numero)"
              return res
    #fin_if
    else:
         res = b , " es invalido ( debe tener 8 digitos )"
         return res
# ejercicio 8
def capicua(x):
    if (x.isdigit() == False ):
         res=x + " no es un numero"
         return res
    else:
        invertida = x[::-1]
        if ( x == invertida):
             res = x, " es capicua"
             return res
        else:
             res= x, " no es capicua"
             return res
 #fin_if

# ejercicio 9
# Funcion que devuelve el numero al cuadrado
def cuadrado(a):
    resultado= (a*a)
    return resultado

# ejercicio 10
# Funcion que halla el peso, segun la gravedad y masa
def peso(m,g):
    res= m*g
    return res

# ejercicio 11
# Funcion que valida si el usuario es correcto
def usuario(y):
     if (y.isdigit() != False):
         resultado =y , " no es correcto (solo son letras y mas no numero )"
         return resultado
     else:
         resultado ="el usuario " , y , " es valido "
         return resultado
     #fin_if

# ejercicio 12
# Funcion que valida la contraseña(solo numeros) y con 12 digitos
def contraseña(x):
    if (x.isdigit() == True ):
         if ( len(x) == 12 ):
             res = x , " es valido"
             return res
         else:
             res = x , " invalido (no tiene 12 digitos)"
             return res
    #fin_if
    else:
         res = x , " es invalido ( no es un numero )"
         return res

# ejercicio 13
def semisuma(x,y):
    resultado=(x+y)*0.5
    return resultado

# ejercicio 14
# si el numero se diferencia en 3 mostrar true
def par(num):
    if (num % 2 == 0):
        return num, "Par"
    else:
        return num, "no par"
#fin_def

# ejercicio 15
# esta funcion halla el tiempo
def tiempo(d,v):
    resultado= d/v
    return resultado


# ejercicio 16
# esta funcion halla la siglas de un banco( 3 letras )
def siglas(a):
    if (len(a) == 3 ):
         if ( a.isalpha() == True ):
              res = a , " es valido"
              return res
         else:
             res = a , " invalido (no es un sigla)"
             return res
    #fin_if
    else:
         res = a , " es invalido ( debe tener 3 digitos )"
         return res

# ejercicio 17
# Esta funcion ayuda a hallar el menor numero

def menor(a,b):
    if (a < b):
        return a
    else:
        return b

# ejercicio 18
# esta funcion halla el tiempo de encuentro
def encuentro(d,V,v):
    resultado = (d/(V+v))
    return resultado

# ejercicio 19
# esta funcion halla el gasto total

def gasto(x,y,z):
    res= (x+y+z)
    return res

# ejercicio 20
# esta funcion verifica si es impar
def presion(f,a):
    res= f*a
    return res

# ejercicio 21
def pedir_placa(b):
    if (len(b) == 6 ):
         if ( b.isalnum() == True ):
              res = b , " es valido ( es placa)"
              return res
         else:
             res = b , " invalido (no es placa)"
             return res
    #fin_if
    else:
         res = b , " es invalido ( debe tener 6 digitos )"
         return res

# ejercicio 22
def pedir_telefono(x):
    if (x.isdigit() == True ):
         if ( len(x) == 9 ):
            res = x , " es valido"
            return res
         else:
             res = x , " invalido (no tiene 9 digitos)"
             return res
    #fin_if
    else:
         res = x , " es invalido ( no es un numero )"
         return res

# ejercicio 23
def trabajo(f,d):
    resultado=f*d
    return resultado

# ejercicio 24
# El nombre de la empresa debe tener 6 digitos
def nombre_empresa(b):
    if (len(b) == 6 ):
         if ( b.isalpha() == True ):
              res = b , " es valido"
              return res
         else:
             res = b , " invalido (no son letras)"
             return res
    #fin_if
    else:
         res = b , " es invalido ( debe tener 6 letras )"
         return res

# ejercicio 25
def presion_hidros(m,g,h):
    resultado= m*g*h
    return resultado

