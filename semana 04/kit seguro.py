#Solucion: Mision Kit seguro

nombre = input("Nombre: ").upper().strip()
Kit = input("Tipo de kit: ").lower().strip()
autorizacion = input("Tiene autorizacion? (si/no): ").strip().lower() == "si"
try:
    cantidad = int(input("Cual es la cantidad de kit?: ")).strip()
except ValueError:
    print("Cantidad de kits invalido,dijite un numero del 0 al 100")
    cantidad = -1
try:
    dias = int(input("Cuantos dias de prestamo?: ")).strip()
except ValueError:
    print ("Canntidad de dias invalidos,ingrese los dias del 0 al 100")
    dias = -1
    
if not nombre or not kit or cantidad < 1 or dias < 1:
    resultado = 'Registro rechazado: revise los datos!'
elif autorizacion and cantida <= 3 and not dias > 7:
    resultado = f"Solicitud aprobada para {nombre}: {cantidad} kits de {kit}"
else:
    resultado = "Solicitud enviada a revision"
    

print("-" * 47"\n")
print(resultado)
print("-" * 47"\n")