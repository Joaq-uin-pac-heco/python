print("bienvenidos a python")
print ("")
print ("calculadora")


def suma (x,y):
 return x + y


def resta(x,y):
 return x - y



def  multiplicacion (x,y):
 return x * y



def   division (x,y):
 return x/y





# ingreso de datos


# primera ronda(suma)

num1 = int (input ("ingrese el primer numero de la sumando: "))
num2 = int (input ("ingrese el otro sumando:"))
print      (input (""))

#resultado de la suma


resultado_sum = suma (num1,num2)
print("el resultado de la suma es: ", resultado_sum)




# segunda ronda(resta)


x=int (input ("ingrese el minuendo: "))
y=int (input ("ingrese el sustraendo:"))
print (input (""))
 
 
 #resultado de la resta

resultado_res = resta (num1,num2)
print("el resultado de la resta es: ", resultado_res)



# tercera ronda (multiplicacion)
n1=int (input ("ingrese el multiplicando: "))
n2=int (input  ("ingrese multiplicador"))
print  (input (""))



#resultado de la multiplicacion

resultado_mul = multiplicacion (num1,num2)
print("el resultado de la suma es: ", resultado_mul)




#cuarta ronda (division)

numero1=int (input ("ingrese el dividendo: "))
numero2=int (input ("ingrese el divisor: "))
print  (input ( ""))



#resultado de la division

resultado_div = division (num1,num2)
print("el resultado de la division es: ", resultado_div)


#validar datos


print("suma UNO:",suma(num1, num2), resultado_sum)
print("suma DOS:",resta(x, y), resultado_res)
print("suma TRES:",multiplicacion(n1, n2), resultado_mul)
print("suma CUATRO:",division (numero1, numero2), resultado_div)


