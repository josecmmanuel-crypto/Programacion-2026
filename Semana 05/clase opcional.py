#listas
#

mi_lista = ["manzana","sandia","fresa"]
cantidad = len(mi_lista)
print ("cantidad de elementos: ", cantidad)
mi_lista[1] = "mango"

print (mi_lista)
print (type(mi_lista))

temporada = ["pera","kiwi"]
mi_lista = mi_lista + temporada
print (mi_lista)

mi_lista.sort()
print(mi_lista)

fruta_nueva = input ("Ingrese su fruta favorita: ")
mi_lista.append(fruta_nueva)
print(mi_lista)

mi_lista.insert (1,"melon")

try:
    eliminar = input("ingrese la fruta a eliminar: ").strip()
    mi_lista.remove("eliminar")
except ValueError:
    print ("La fruta no existe en la lista")
print (mi_lista)

minimo = min (mi_lista)
maximo = max (mi_lista)

print (minimo,maximo)