from PIL import Image
print("ingrese la ruta de imagen:")
ruta=input(str())
imagen = Image.open(ruta)
imagen.show()
resolucion = imagen.size

cantidadPix = resolucion[0] * resolucion[1]
print(f"{'El tamaño de la imagen es :':<20}: {imagen.size}")
print(f"{'El formato de la imagen es :':<20}: {imagen.format}")
print(f"{'resolucion :':<20}: {resolucion[0] * resolucion[1]}")
print(f"{'cantidad de pixeles :':<20}: {cantidadPix}")
print(f"{'ubicacion de la imagen :':<20}: {ruta}")
