"""Caso 4: analice los registros de soporte sin crear funciones propias."""

from incidencias import incidencias

# Cada incidencia es un diccionario: id, provincia, categoria,
# minutos_atencion y resuelto (True o False).

# TODO: Prepare un acumulador de minutos, un diccionario para contar
#       "Acceso", "Equipo" y "Red", un contador de casos pendientes,
#       un set de provincias con pendientes, una lista de tuplas de casos
#       urgentes y una tupla para el caso con más minutos de atención.
total_minutos = 0
conteo_categorias = {"Acceso": 0, "Equipo": 0, "Red": 0}
cantidad_pendientes = 0
provincias_pendientes = set()
casos_urgentes = []
caso_mas_largo = ("", 0)
# TODO: Recorra incidencias una sola vez. Actualice los acumuladores y el
#       conteo de la categoría de cada registro.
# TODO: Si un caso NO está resuelto, cuéntelo y agregue su provincia al set.
#       Si, además, tiene 60 minutos o más, agregue (id, minutos) a la lista
#       de casos urgentes. Actualice la tupla del caso más largo si corresponde.
total_casos = len(incidencias)

for inc in incidencias:
    minutos = inc["minutos_atencion"]
    cat = inc["categoria"]
    inc_id = inc["id"]
    provincia = inc["provincia"]
    resuelto = inc["resuelto"]
    
    # Actualizar acumulador y conteo por categoría general
    total_minutos += minutos
    if cat in conteo_categorias:
        conteo_categorias[cat] += 1

    # Actualizar el caso con más minutos de atención (aplica para todos los registros)
    if minutos > caso_mas_largo[1]:
        caso_mas_largo = (inc_id, minutos)

    # Validar si el caso NO está resuelto
    if not resuelto:
        cantidad_pendientes += 1
        provincias_pendientes.add(provincia)

        # Si además tiene 60 minutos o más, es urgente
        if minutos >= 60:
            casos_urgentes.append((inc_id, minutos))

# Calcular el promedio de minutos
promedio_minutos = total_minutos / total_casos if total_casos > 0 else 0

# TODO: Muestre total y promedio de minutos, conteo por categoría, cantidad
#       de pendientes, provincias con pendientes, casos urgentes y caso más
#       largo. Compruebe también si "San Jose" pertenece al set.
print("--- REPORTE DE SOPORTE TÉCNICO ---")
print(f"Total de minutos de atención: {total_minutos}")
print(f"Promedio de minutos: {promedio_minutos}")
print(f"Conteo por categoría: {conteo_categorias}")
print(f"Cantidad de casos pendientes: {cantidad_pendientes}")
print(f"Provincias con casos pendientes: {provincias_pendientes}")
print(f"Casos urgentes (pendientes con >= 60 min): {casos_urgentes}")
print(f"Caso más largo: ID '{caso_mas_largo[0]}' con {caso_mas_largo[1]} minutos")

# Comprobación de membresía en el set
tiene_san_jose = "San Jose" in provincias_pendientes
print(f"¿Hay pendientes en San Jose?: {'Sí' if tiene_san_jose else 'No'}")

# Control: 10 casos; 500 minutos; promedio 50; Acceso 4, Equipo 3, Red 3;
# 4 pendientes en 4 provincias; urgentes INC-02, INC-05 e INC-07;
# más largo INC-07 con 95 minutos; hay pendientes en San Jose.
# Prueba: cambie temporalmente INC-07 a resuelto=True. Debe salir de la
# lista de urgentes, del conteo de pendientes y del set de provincias
# pendientes, pero seguir como caso más largo. Restaure incidencias.py.
