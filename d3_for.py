lista=[]

for n in range(5):
    a = int(input("Ingrese un número: "))
    lista.append(a)
    lista.sort()

#print (lista) para ver la lista ordenada de menor a mayor
print("El elemento mayor es: ", lista[4])