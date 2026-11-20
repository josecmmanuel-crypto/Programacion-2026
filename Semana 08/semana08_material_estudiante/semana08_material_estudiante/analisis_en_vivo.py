"""Semana 8: informe de atenciones hospitalarias ficticias.

Complete las fases con el docente. La lectura de datos ya está preparada.
"""

# FASE 0: CONSUMIR LA CONEXIÓN PREPARADA
# conexion_api.py se encuentra junto a este archivo.
from conexion_api import cargar_datos

registros = cargar_datos()
print("Fuente: JSON público de GitHub")
print("Atenciones recibidas:", len(registros))

# La muestra solicitada usa range(3): deben existir las posiciones 0, 1 y 2.
if len(registros) < 3:
    raise SystemExit("Se necesitan al menos 3 registros. Publique la etapa 3.")


# FASE 1: MOSTRAR Y CONTAR LOS MEDICAMENTOS DE TRES ATENCIONES
total_medicamento = 0
conteo_medicamento = {}
print ("Analisis Fase 1 Muestra #3")
for indice in range(3):
    registro = registros [indice] 
print("\n Paciente : {registro[paciente_nombre]}")
print("\n Cedula: {registro[paciente_cedula]}")
print("\n Diagnostico: {registro[diagnostico]}")
print("\n Medicamento: {registro[medicamentos]}")

for medicamento in registro['medicamentos']:
        print(medicamento)
        total_medicamento += 1
        
# FASE 2: CONTAR LOS MEDICAMENTOS DE TODAS LAS ATENCIONES
print("\nAnalisis Fase 2 Medicaciones y Atenciones")
for registro in registros:
    print(registro['paciente_nombre'])

# FASE 3: CONTAR ATENCIONES POR HOSPITAL

# FASE 4: CONTAR ATENCIONES POR ENFERMEDAD DIAGNOSTICADA

