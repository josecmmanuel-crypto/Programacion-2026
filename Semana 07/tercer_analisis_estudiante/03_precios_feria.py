"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo 
# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
i = 0
superan_promedio = 0
while i < len(precios):
    if precios[i] > promedio:
        superan_promedio += 1 
        i += 1 
# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
    variacion = "Variacion alta"
elif rango >= 150:
    variacion = "Variacion moderada"
else:
    variacion = "Variacion baja"
# TODO: Muestre producto y todos los resultados.
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.
print("\nAnalisis de los precios de la feria")
print(f"Producto: {producto}")
print(f"Promedio: {promedio}")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
print(f"Rango: {rango}")
print(f"Precios que superan el promedio: {superan_promedio}")
print(f"Variación: {variacion}")
