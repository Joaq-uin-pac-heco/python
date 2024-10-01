#realizar un programa que de solucion a los sgts.:
#ingresar 5 alumnos (nombre,apellido y 3 notas)
# nota 1 vale 20%
# nota 2 vale 30%
# nota 3 vale 50%
# calcular el promedio por alumno
# calcular el promedio total del curso
# (compuesto por estos 5 alumnos)
# calcular la mejor nota por alumno
# calcular el mejor promedio







def promedio_curso (n1, n2, n3,n4,n5):
 prom = 0
 prom = ( n1 + n2 + n3 +n4+ n5)/5
 return prom

def promedio_nota (n1, n2, n3, n4, n5,p1,p2,p3):
 prom = 0
 prom = (n1 *  + p2 * n2 + p3 * n3)/100
 return prom

#nota 1 vale 20%
#nota 2 vale 30%
#nota 3 vale 50%
 
#inicilizacion de arreglos
notas = [0,0,0]
alumnos = [0,0,0,0,0]

#ponderados que en este caso son CONSTANTES
p = [20,30,50]
prom = [0,0,0,0,0]


for i in range (5):
 nombre_apellido = input("ingrese el nombre del alumno  {i+1}: ")

 print("lista de alumnos ingresados: ")
 alumnos.append(nombre_apellido)

for alumno in alumnos:
print(alumno)