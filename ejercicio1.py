
#Evaluamos que el ingreso de clases sea un número entero y mayor a cero
flag_cantidad_clases = True
while flag_cantidad_clases == True:
    try:
        cantidad_clases = int(input("Ingrese la cantidad de clases: "))
        if cantidad_clases <= 0:
            print("El número de clases debe ser mayor a cero")
        else:
            flag_cantidad_clases = False
    except:
        print("Debe ingresar un número entero")    


#Evaluamos que el valor para estudiante regular sea S o N
flag_alumno_regular = True
while flag_alumno_regular == True:
    estudiante_regular = input("Ingrese si es estudiante regular (S/N): ").upper()
    if estudiante_regular == "S" or estudiante_regular == "N":
        flag_alumno_regular = False
    else:
        print("Debe ingresar una 'S' para si y una 'N' para NO")

#Valores fijos
valor_mensualidad = 25000
valor_botella     = 8000

#Valores variables
valor_final_mensualidad = 0
valor_final_botella     = 0
descuento               = 0.0
descuento_botella       = 0
total                   = 0

#Evaluamos cada caso
#Primero revisamos la cantidad de clasezs
if cantidad_clases >= 20:
    if estudiante_regular == "S":
        descuento = 0.3
    else:
        descuento = 0.2
elif cantidad_clases >= 10 and cantidad_clases <= 19:
    if estudiante_regular == "S":
        descuento = 0.15
    else:
        descuento = 0.1  

#Segundo, revisamos el descuento para la botella
if estudiante_regular == "S":
    descuento_botella = 0.1
    if cantidad_clases >= 15:
        descuento_botella = 0.15

#Calculamos los valores finales
valor_final_mensualidad = int(valor_mensualidad - (valor_mensualidad*descuento))
valor_final_botella     = int(valor_botella - (valor_botella*descuento_botella))
total                   = valor_final_mensualidad + valor_final_botella

#Imprimimos los datos de salida...
print(f"Valor final mensualidad: ${valor_final_mensualidad}")
print(f"Valor dinal botella: ${valor_final_botella}")
print(f"Total general: ${total}")