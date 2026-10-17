"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

total_centro = sum(ventas_centro)
cantidad_centro = len(ventas_centro)

menor_centro = min(ventas_centro)
mayor_centro = max(ventas_centro)
promedio_centro = total_centro / cantidad_centro

porcentaje_centro = total_centro * 100 / meta_centro

#print(porcentaje_centro)

total_norte = sum(ventas_norte)
cantidad_norte = len(ventas_norte)

menor_norte = min(ventas_norte)
mayor_norte = max(ventas_norte)
promedio_norte = total_norte / cantidad_norte

porcentaje_norte = total_norte * 100 / meta_norte 
#print(porcentaje_norte)

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.

if total_centro > meta_centro:
    estado_centro = "Meta superada"
elif total_centro == meta_centro:
    estado_centro == "meta alcanzada exactamente"
else:
    estado_centro = "Meta NO alcanzada"


if total_norte > meta_norte:
    estado_norte = "Meta superada"
elif total_norte == meta_norte:
    estado_norte == "meta alcanzada exactamente"
else:
    estado_norte = "Meta NO alcanzada"

# TODO: compara los totales y los rangos.
if total_centro > total_norte:
    tienda_gano = "Tienda centro"
elif total_norte > total_centro:
    tienda_gano = "Tienda del norte"
else:
    tienda_gano = "Ambas tiendas tiene el mismo total"
#TODO: presenta un reporte con etiquetas claras y f-strings.
# TODO: escribe las tres conclusiones solicitadas en la guía.
print ("					COMPARACION SEMANAL DE TIENDAS")
print ("-"*100,"\n")
print (f"Centro | Total ₡{total_centro:,.2f} | Meta ₡{meta_centro:,.2f} | Cumplimiento {porcentaje_centro:.0f}%")
print (f"Centro logro: {estado_centro}")

print ("-"*100,"\n")
print (f"norte | Total ₡{total_norte:,.2f} | Meta ₡{meta_norte:,.2f} | Cumplimiento {porcentaje_norte:.0f}%")
print (f"norte logro: {estado_norte}")
