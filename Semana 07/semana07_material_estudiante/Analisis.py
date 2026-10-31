from sedes import sedes

print ("Ventas de la primera sede:", sedes[0]["ventas"])


print ("\nAnalisis semanal de emprendimienetos de Costa Rica")

for sede in sedes:
    print ("Emprendimiento:", sede["nombre"])