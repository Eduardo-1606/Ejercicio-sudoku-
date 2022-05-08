inicio=100
final=1200
capicuas=[]
for x in range(inicio,final+1):
    cadena=str(x)
    reverso=cadena[::-1]
    if cadena==reverso:
        capicuas.append(x)

print(capicuas)