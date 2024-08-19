from PIL import Image
print("ingrese la ruta de la imagen:")
ruta = input(str())
rotar = float(input("ingrese cuanto quiere rotar la imagen en grados :"))
img = Image.open(ruta)
imgrotada = img.rotate(rotar,expand = True)
imgrotada.show()
nombreinicial = ruta.split("/")[-1]
nombre, extension = nombreinicial.rsplit(".", 1)
nombrefinal= f"{nombre}Rot.{extension}"
imgrotada.save(nombrefinal)
print(f"Imagen guardada como {nombrefinal}")

