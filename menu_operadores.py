print("Ingrese el numero del ejercicio que desea ejecutar")
exercise=int(input())
if exercise==1:
  print("Ingrese la altura de su triangulo")
  altura=float(input())
  print("Ingrese la base de su triangulo")
  base=float(input())
  area=altura*base/2
  print("El area de su triangulo es de" ,area)
elif exercise==2:
  print("ingrese su primer numero")
  num1=int(input() )
  print("ingrese su segundo numero")
  num2=int(input())
  sum=num1+num2
  print("El resultado de la suma es", sum)
elif exercise==3:
  print("ingrese el numero que desea poner al cuadrado")
  number=int(input())
  empowerment=number**2 
  print("El cuadrado del numero es",empowerment)
elif exercise==4:
  print("El numero que vamos a sumar es 1234")
  num1=1234
  print("El segundo numero que sumaremos es 532")
  num2=532
  sum=num1+num2
  print("El resultado es",sum)
elif exercise==5:
  print("Bienvenido")
  print("El primer numero que vamos a restar es 1234")
  num1=1234
  print("El segundo numero que vamos a restar es 532")
  num2=532
  resta=num1-num2
  print("El resultado de esta resta es", resta)
elif exercise==6:
  print("Bienvenido")
  print("vamos a multiplicar 1234")
  num1=1234
  print("y lo multiplicaremos por 532")
  num2=532
  Multiplicacion=num1*num2
  print("El resultado de esta resta es", Multiplicacion)
elif exercise==7:
  print("Bienvenido")
  print("Dividiremos 1234")
  num1=1234
  print("Entre 532")
  num2=532
  Div=num1/num2
  print("Y el resultado es", Div)
elif exercise==8:
  print("Bienvenido")
  print("Sacaremos el porcentaje de 1234")
  num1=1234
  print("entre 532")
  num2=532
  Porcen=num1%num2
  print("El porcentaje es", Porcen)
elif exercise==9:
  print ("Bienvenido")
  print("ingrese la cantidad de euros que desea convertir a dolares ")
  num1=int(input())
  num2=float(1.10)
  eu=num1*num2
  print("La cantidad de dolares es", eu)
elif exercise==10:
  print("Bienvenido")
  print("Ingrese el largo de su rectangulo")
  num1=float(input())
  print("Ahora ingrese el ancho de su rectangulo")
  num2=float(input())
  Area=num1*num2
  print("El area de su rectangulo es de", Area) 
elif exercise==11:
  print("Bienvenido")
  print("Calcularemos el area de su cuadrado")
  print("Ingrese el valor de un lado de su cuadrado")
  num1=int(input())
  area=num1*num1 
  print("El area de su cuadrado es de",area)
  perimetro=num1+num1+num1+num1
  print("y el perimetro de su cuadrado es de",perimetro)
elif exercise==12:
  print("Bienvenido")
  print("Iniciaremos calculando el area de su cilindro")
  print("Ingrese el radio de su cilindro")
  num1=float(input()) 
  pi=3.1416
  potencia=num1**2
  area2=pi*potencia
  print("El area de su cilindro es de)", area2)
  print("Ahora calcularemos el volumen ")
  print("Ingrese la altura de su cilindro")
  num2=float(input())
  h=area2*num2
  print("el volumen de su cilindro es", h)
  print("Por lo tanto el area de su cilindro es de ", area2)
  print("y el volumen es de", h)
elif exercise==13:
  print("Bienvenido")
  print("Inserte el valor del diametro de su circulo")
  num1=float(input())
  p=num1/2
  pi=3.14
  longitud=pi*p
  l=p**2
  area=l*pi
  print("El valor del radio de su circunferencia es de",p )
  print("El valor de la longitud es de", longitud)
  print("el area de su circulo es de",area)
elif exercise==14:
  print ("Bienvenido")
  print("Digite su primer valor")
  num1=float(input())
  print("Digite su segundo valor")
  num2=float(input())
  print("Digite su tercer valor")
  num3=float(input())
  s=num1+num2+num3
  d=s/3
  print("Su promedio es de",d)