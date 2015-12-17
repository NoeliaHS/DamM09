'''Ejercicio 5: '''

a = int(input("Introduzca el primer número: "))
b = int(input("Introduzaca el segundo número: "))
c = int(input("Introduzca el tercer número: "))
if a > b and a > c and b > c:
	print ("El número más grande es:",a)
if b > a and b > c and a > c:
	print ("El número más grande es:",b)
if c > a and c > b and b > a:
	print ("El número más grande es:",c)
input()
