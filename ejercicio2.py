num1 = None
num2 = None

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
        continue
    if num2 > num1:
        break
    else:
        print("El segundo número debe ser mayor al primero")

from random import randint
numero = randint(num1,num2)

if numero%2 != 0:
    if numero + 1 <= num2:
        numero = numero + 1
    elif numero + 1 > num2:
        numero = numero - 1

intentos = []

for i in range(1, 4):
    while True:
        try:
            intento = int(input(f"Intento {i} - Ingrese su número: "))
        except ValueError:
            print("Debe ingresar números enteros.")
            continue
        
        if num1 <= intento <= num2:
            break
            
        print(f"Debe ingresar un número dentro del rango ({num1},{num2})")
    
    intentos.append(intento)

    if intento == numero:
        print("¡FELICITACIONES ADIVINASTE!")
        break

    if i < 3:
        if intento < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")
            
        if i == 2:
            dist1 = abs(numero - intentos[0])
            dist2 = abs(numero - intentos[1])
            
            if dist1 > dist2:
                print(f"Pista: El número está más cerca de {intentos[1]} que de {intentos[0]}.")
            elif dist2 > dist1:
                print(f"Pista: El número está más cerca de {intentos[0]} que de {intentos[1]}.")
            else:
                print("Pista: Ambos intentos están a la misma distancia del número.")
    else:
        print(f"Lo siento, perdiste. \nEl Número era {numero}.")
