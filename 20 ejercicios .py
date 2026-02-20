#1.Calcula de area de rectanulo.

base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))
area = base * altura
print(f"El área del rectángulo es: {area}")

#2.Conversor de temperatura.

celsius = float(input("Ingresa la temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print (f"el total en grados fahrenheit son {fahrenheit} ")

#3.Concatenacion de cadenas.

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

print(f"Hola {nombre_completo}, ¡bienvenido al equipo!")

#4.Verificador de numero par o impar.

numero = int(input("Introduce un número entero: "))
if numero % 2 == 0:
    print("Es un número par.")
else:
    print("Es un número impar.")

    #5.Elegibilidad para votar.

    edad = int(input("Ingresa tu edad: "))

if edad < 0 or edad > 120:
    print("Por favor, ingresa una edad válida.")
elif edad >= 18:
    print("eres elegible para votar.")
else:
    print("No eres elegible para votar aún.")

    #6.Conparador de numeros.

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if num1 > num2:
    print("El primer número es mayor") 
    
elif num2 > num1:
    print("El segundo número es mayor")
    
else:
    print("Los números son iguales")

#7.Operadores logicos.

numero = int(input("Ingresa un número: "))

if 10 <= numero <= 20:
    print("El número está entre 10 y 20")
else:
    print("El número no está entre 10 y 20")

#8.Verificacion de contraseña simple.

contrasena_correcta = "one piece"
contrasena = input("Ingresa la contraseña: ").strip()

if contrasena == contrasena_correcta:
    print("acceso concedido. ¡Bienvenido!")
else:
    print("Acceso denegado. Inténtalo de nuevo.")

#9.Calculadora de descuento.

precio = float(input("Ingresa el precio del producto: "))

if precio > 100:
    descuento = precio * 0.15
    precio_final = precio - descuento
    print(f"¡Se aplicó un descuento del 15%! El total es: ${precio_final:.2f}")
else:
    print(f"No aplica descuento. El total es: ${precio:.2f}")

#10.Clasificador de numeros.

numero = int(input("Ingresa un número para clasificar: "))
if numero > 0:
    print("El número es POSITIVO")
elif numero < 0:
    print("El número es NEGATIVO")
else:
    print("El número es CERO")

#11.año bisiesto.

año = int(input("Ingresa un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")

#12.Calculadora de calificaciones.

nota = int(input("Ingresa la calificación (0-100): "))

if nota >= 90:
    print("Resultado: A (Sobresaliente) ")
elif nota >= 80:
    print("Resultado: B (Muy bueno) ")
elif nota >= 70:
    print("Resultado: C (Bueno) ")
elif nota >= 60:
    print("Resultado: D (Suficiente) ")
else:
    print("Resultado: F (Insuficiente) ")

#13.Verificador de vocal o consonante.

caracter = input("Ingresa una sola letra: ").lower()

if len(caracter) != 1 or not caracter.isalpha():
    print(" Por favor, ingresa solo una letra válida.")
else:
    if caracter in "aeiouáéíóú":
        print(f"Es una vocal.")
    else:
        print(f"Es una consonante.")

#14.Seleccion de menu.

print(" MENU DE BIENVENIDA ")
print("1. Saludar")
print("2. Ver estado del sistema")
print("3. Salir")
print("1 or 2 or 3")

opcion = input("Elige una opción (1-3): ")

if opcion == "1":
    print(" ¡Hola! Esperamos que tengas un gran día de programación.")
elif opcion == "2":
    print(" El sistema está funcionando al 100% y sin errores.")
elif opcion == "3":
    print(" Cerrando sesión...")
else:
    print(" Opción no válida. Por favor, elige 1, 2 o 3.")

#15.Tipo de triangulo.

lado1 = float(input("Ingresa el primer lado: "))
lado2 = float(input("Ingresa el segundo lado: "))
lado3 = float(input("Ingresa el tercer lado: "))

if lado1 == lado2 == lado3:
    print(" Es un triángulo EQUILÁTERO (todos los lados iguales).")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print(" Es un triángulo ISÓSCELES (dos lados iguales).")
else:
    print(" Es un triángulo ESCALENO (todos los lados diferentes).")

#16.El mayor de tres numeros.

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c

print(f" El número más grande es: {mayor}")

#17.Calculadora IMC.

peso = float(input("Ingresa tu peso en kg (ej: 75.5): "))
altura = float(input("Ingresa tu altura en metros (ej: 1.75): "))

imc = peso / (altura ** 2)

print(f"\nTu IMC es: {imc:.2f}")

if imc < 18.5:
    print("  Categoría: Bajo peso")
elif 18.5 <= imc <= 24.9:
    print(" Categoría: Peso normal")
elif 25 <= imc <= 29.9:
    print(" Categoría: Sobrepeso")
else:
    print(" Categoría: Obesidad")

#18.Calculadora de costo de envio.

print(" SISTEMA DE ENViOS ")
print("Zonas disponibles: (A) Norte, (B) Sur")
zona = input("Selecciona la zona (A/B): ").upper()
peso = float(input("Ingresa el peso del paquete en kg: "))

costo = 0

if zona == "A":
 
    if peso <= 5:
        costo = 10
    else:
        costo = 15
elif zona == "B":
  
    if peso <= 5:
        costo = 12
    else:
        costo = 20
else:
    print(" Zona no válida.")

if costo > 0:
    if costo > 18:
        print(" descuento de $2 por envío pesado ")
        costo -= 2
    print(f" El costo final de envío es: ${costo}")

#19.Resolucion de ecuacion cuadratica.

print(" SISTEMA DE ENViOS ")
print("Zonas disponibles: (A) Norte, (B) Sur")
zona = input("Selecciona la zona (A/B): ").upper()
peso = float(input("Ingresa el peso del paquete en kg: "))

costo = 0

if zona == "A":
 
    if peso <= 5:
        costo = 10
    else:
        costo = 15
elif zona == "B":
  
    if peso <= 5:
        costo = 12
    else:
        costo = 20
else:
    print(" Zona no válida.")

if costo > 0:
    if costo > 18:
        print(" descuento de $2 por envío pesado ")
        costo -= 2
    print(f" El costo final de envío es: ${costo}")
print(" RESOLUCION DE ECUACIONES CUADRÁTICAS ")
a = int(input("Ingresa el coeficiente a: "))
b = int(input("Ingresa el coeficiente b: "))
c = int(input("Ingresa el coeficiente c: "))

if a == 0:
    print(" Si 'a' es 0, no es una ecuación cuadrática.")
else:

    discriminante = b**2 - 4*a*c
    print(f"El discriminante es: {discriminante}")

    if discriminante > 0:
     
        raiz = discriminante ** 0.5
        x1 = (-b + raiz) / (2*a)
        x2 = (-b - raiz) / (2*a)
        print(f" Hay 2 soluciones reales: x1 = {x1:.2f}, x2 = {x2:.2f}")

    elif discriminante == 0:
        x = -b / (2*a)
        print(f" Hay 1 solución real unica: x = {x:.2f}")

    else:
        print("No hay soluciones reales.")

#20.Juego de piedra , papel o tijera.

print(" PIEDRA, PAPEL O TIJERA ")
jugador1 = input("Jugador 1, elige (piedra, papel o tijera): ").lower()
jugador2 = input("Jugador 2, elige (piedra, papel o tijera): ").lower()

if jugador1 == jugador2:
    print(f" ¡Es un empate! Ambos eligieron {jugador1}.")

else:
    if jugador1 == "piedra":
        if jugador2 == "tijera":
            print(" ¡Jugador 1 gana! La piedra rompe la tijera.")
        else:
            print(" ¡Jugador 2 gana! El papel envuelve la piedra.")
            
    elif jugador1 == "papel":
        if jugador2 == "piedra":
            print(" ¡Jugador 1 gana! El papel envuelve la piedra.")
        else:
            print(" ¡Jugador 2 gana! La tijera corta el papel.")
            
    elif jugador1 == "tijera":
        if jugador2 == "papel":
            print(" ¡Jugador 1 gana! La tijera corta el papel.")
        else:
            print(" ¡Jugador 2 gana! La piedra rompe la tijera.")
            
    else:
        print(" Uno de los jugadadores imgreso una opcion no valida " )