'''Ejercicio 6: '''

a = int(input("Introduzca el primer número: "))
b = int(input("Introduzaca el segundo número: "))
c = int(input("Introduzca el tercer número: "))

if a > b and a > c and b > c:
	print (a,b,c)
if b < a and b < c and a > c:
	print (a,c,b)
if c < a and c < b and b > a:
	print (b,a,c)
if a < b and a < c and b > c:
	print (b,c,a)
if a > b and a < c and b < c:
	print (c,a,b)
if a < b and a < c and b < c:
	print (c,b,a)
input()
