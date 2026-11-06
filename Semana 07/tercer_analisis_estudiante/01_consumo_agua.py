"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [100, 100, 100, 100, 100]

# TODO: Calcule el consumo total y el promedio diario.
total_consumo = sum(consumos_litros)
promedio_diario = total_consumo / len(consumos_litros)
# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
primer_dia = consumos_litros[0]
ultimo_dia = consumos_litros[-1]
ahorro_litros = primer_dia - ultimo_dia
porcentaje_reduccion = (ahorro_litros / primer_dia) * 100
# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
if porcentaje_reduccion >= 15:
    clasificacion = "Reduccion alta"
elif porcentaje_reduccion > 0:
    clasificacion = "Reduccion moderada"
else:
    clasificacion = "Sin reduccion"
# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
print("\nCONTROL DE CONSUMO DE AGUA")
print(f"El total del consumo es: {total_consumo}")
print(f"El promedio diario es: {promedio_diario}")
print(f"El ahorro de agua es: {ahorro_litros}")
print(f"El porcentaje de reducción es: {porcentaje_reduccion:.2f} %")
print(f"La clasificación es: {clasificacion}")

# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
