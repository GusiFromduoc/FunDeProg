num1 = None
num2 = None
intento1 = None
intento2 = None
intento3 = None
while True:
    try:
        num1 = int(input("Ingrese el límite inferior: "))
        break
    except ValueError:
        print("Ingrese un número válido por favor.")

while True:
    try:
        num2 = int(input("Ingrese el límite superior: "))
    except ValueError:
        print("Ingrese un número válido por favor.")
    if num2 > num1:
        break
    else:
        print("El segundo número debe ser mayor al primero")
        continue

from random import randint
numero = randint(num1,num2)

if numero%2 != 0:
    if numero + 1 <= num2:
        numero = numero + 1
    elif numero + 1 > num2:
        numero = numero - 1

while True:
    try:
        intento1 = int(input("Intente adivinar el num: "))
    except ValueError:
        print("Debe ingresar numeros enteros.")
    if num1 <= intento1 <= num2:
        break
    else:
        print(f"Debe ingresar un número dentro del rango ({num1},{num2})")
        continue

if intento1 == numero:
    print("¡FELICITACIONES ADIVINASTE!")
elif intento1 < numero:
    print("El numero es mayor")
elif intento1 > numero:
    print("El numero es menor")


while intento1 != numero:
    try:
        intento2 = int(input("Intente adivinar el num: "))
    except ValueError:
        print("Debe ingresar numeros enteros.")
    if num1 <= intento2 <= num2:
        break
    else:
        print(f"Debe ingresar un número dentro del rango ({num1},{num2})")
        continue

if intento1 != numero:
    if intento2 == numero:
        print("¡FELICITACIONES ADIVINASTE!")
    elif intento2 < numero:
        print("El numero es mayor")
    elif intento2 > numero:
        print("El numero es menor")

if intento2 != numero and intento1 != numero:
    dist1 = abs(numero-intento1)
    dist2 = abs(numero-intento2)
#Esto lo cree para saber la distancia, usé valor absoluto para saber a qué distancia están  del numero en numeros positivos.
    if dist1 > dist2:
        print(f"Pista el número está más cerca de {intento2} que de {intento1}")
    elif dist2 > dist1:
        print(f"Pista el número está más cerca de {intento1} que de {intento2}")
    else:
        print("Pista: ambos intentos están a la misma distancia del numero.")



while intento1 != numero and intento2 != numero:
    try:
        intento3 = int(input("Intente adivinar el num: "))
    except ValueError:
        print("Debe ingresar numeros enteros.")
    if num1 <= intento3 <= num2:
        break
    else:
        print(f"Debe ingresar un número dentro del rango ({num1},{num2})")
        continue

if intento3 == numero:
    print("¡FELICITACIONES ADIVINASTE!")
elif intento1 != numero and intento2 != numero and intento3 != numero:
    print(f"Lo siento, perdiste. El Número era {numero}. ")
