meds = 60000
desp = 8000 
edad = None
tramo = None
tramos_validos = ["A","B","C","D"]


while True:
    try:
        edad = int(input("Por favor ingrese su edad para continuar. "))
    except ValueError:
        print("Por favor ingrese una edad en número entero. ")
    if 18 <= edad < 120:        
        break
    else:
        print("Debe tener al menos 18 años para comprar y dudo tengas más de 120 años.")
        continue

while True:
    tramo = input("Ingrese su tramo por favor A, B, C o D. ").upper()
    if tramo in tramos_validos:
        break
    else:
        print("Por favor ingrese un tramo valido")
        continue
    
if 18 <= edad <= 30:
    if tramo == "A" or tramo == "B":
        meds = meds * 0.82
        desp = desp * 0.9
    elif tramo == "C" or tramo == "D":
        meds = meds * 0.88

if 31 <= edad <= 60:
    if tramo == "A" or tramo == "B":
        meds = meds * 0.88
        desp = desp * 0.9
    elif tramo == "C" or tramo == "D":
        meds = meds * 0.92

if edad > 60:
    if tramo == "A" or tramo == "B":
        desp = desp * 0.9
    elif tramo == "C" or tramo == "D":
        pass


if edad >= 55:
    desp -= 8000 * 0.05
    #Usé 8000 porque era el desp original, no sé si ese 5 se hace sobre el original o el ya reducido. 
    #en el ejemplo no se considera.

print(f"El total de los medicamentos es: ${round(meds)}\nEl total del despacho es: ${round(desp)}\nSu edad es {edad} su tramo es {tramo} verifique sus datos y elija su método de pago. ")