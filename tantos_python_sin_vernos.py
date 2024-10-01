#funcion para mostrar el menu de opciones
def mostrar_menu():
 print("")
 print("opciones de numero de personajes que iran al show: ")
print ("1. 3 personajes")
print ("2. 4 personajes")
print ("3. 5 personajes")
#funcion para seleccionar el numero de personajes con validacion
def seleccion_num_personajes():
   mostrar_menu
 
 
 
 #validacion con la opcion menu sea 
    while true:
    try:
    opcion = int(input("elige una opcion (1-4): "))
    if opcion not in [1,2,3,4]
    print("opcion no valida por favor, eliga una opcion entre 1 y 4: ")
     else:
      break
     except valueerror:
     print("entrada no valida por favor coloca un numero entero entre 1 y 4")

#seleccionar numero de personajes con validacion adicional si es necesario

 if opcion == 1:
  return 3
 elif opcion == 2:
  return 4
 elif opcion == 3:
  return 5
  elif opcion == 4



#validar que el numero ingresado manualmente sea positivo
while true:
  try
  N = int(input("ingresa el numero de personajes wue deseas" ))
  if N > 0
   return 0
   else:
    print ("porfavor ingrese un numero mayor que 0.")
    except valueerror:
      print("entrada no valida porfavor ingrese un numero mayor que 0")

 
 
  print("opcion invalida, eligiendo por defecto 3")
 return 3

#funcion principal para ingresar N de personajes

def ingresar_personajes():

 i = int(input("ingrese el numero de personajes que deseas(debe ser mayor a 0)"))

personajes = []


#ingreso de los personajes con N valido
for i in range (N):
 personaje = input("ingrese nombre del personaje {i + 1}: ") 
 print ("N los personajes ingresados para la pampilla son: ")
    personajes.append(personaje)
 


for i in range (i):
  enumerate(personajes, 1)
  print (f"{i}.{personaje}")
 
 
  #llamada a la funcion principal 
  
 ingresar_personajes()
 
 