"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

total = 0
bloques_superan = 0
umbral_70 = capacidad * 0.70

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
for asistencia in asistencias:
    total += asistencia
    if asistencia > umbral_70:
        bloques_superan += 1 
# TODO: Calcule el promedio y su porcentaje de ocupación.
promedio = total / len (asistencias)
porcentaje_ocupacion = (promedio / capacidad) * 100
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if porcentaje_ocupacion >= 80:
    estado = "Ocupación alta"
elif porcentaje_ocupacion >= 50:
    estado = "Ocupación media"
else:
    estado = "Ocupación baja"
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
print("\nANALISIS DE ASISTENCIA POR BLOQUES ")
print(f"El total de asistencia es: {total}")
print(f"El promedio de asistencia es: {promedio}")
print(f"El porcentaje de ocupación es: {porcentaje_ocupacion:.2f} %")
print(f"La cantidad de bloques que superan el 70 % es: {bloques_superan}")
print(f"El estado de ocupación es: {estado}")
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
