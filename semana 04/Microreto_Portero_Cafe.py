"""Microreto: el portero del café."""

nombre = input("Cual es su nombre?").upper().strip()
Energia = int(input("Cuanta energia tiene ahorita de 0 a 100: "))
trae_cafe = inpup(Traes cafe(si/no)?: ).lower().strip() == "si"

mensaje = ""
#si menos de 50% y no tengo cafe: -> Descansar
if energia < 50 and not(trae_cafe):
    mensaje = "Acceso denegado: necesita dormir"
#si 50% 0 mas o tenga cafe: -> puede ingresar a la clase
elif energia >= 50 or trae_cafe:
    mensaje = "Acceso permitido: pasa con gusto"
#cualquier otro ecenario: portero cofundido
else:
    mensaje = "Portero confundido: revisar respuesta"
print(trae_cafe)
print(type(trae_cafe))
if trae_cafe:
    print("viene con buen cafe")
print(f"{nombre}:{mensaje}")
