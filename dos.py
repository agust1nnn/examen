from PIL import Image

print("Carga la ruta del archivo de imagen:")
ruta = input()

imagen = Image.open(ruta)
imagen.show()

nuevaimg = "imagenDes.jpg"
imagen.save(nuevaimg)

print(f"el nuevo nombre es :{nuevaimg}")
