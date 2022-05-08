a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mensaje=str(input("Ingrese un mensaje: "))
clave=2
cifrado=""
for x in mensaje.upper():
    if x in a:
        indice= a.find(x)
        indice+=clave
        if indice>=26:
            indice-=26
        cifrado += a[indice]
    else:
        cifrado+=x
print(cifrado)
