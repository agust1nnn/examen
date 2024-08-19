from PIL import Image
import os
import sys

print('Ingrese la ruta de la imagen:')
ruta = input()
img = Image.open(ruta)
print(f'La resolución de la imagen es: {img.size}')
print('Ingrese la coordenada X inicial')
coordenadax = int(input())
print('Ingrese la coordenada Y inicial')
coordenaday = int(input())
print('Ingrese el valor de ancho a recortar')
ancho = int(input())
print('Ingrese el valor de altura a recortar')
altura = int(input())

if (img.width - coordenadax ) < ancho or (img.height - coordenaday) < altura :
    sys.exit('Valores a recortar incorrectos')
else:
    cortarcoord = (coordenadax , coordenaday, coordenadax  + ancho, coordenaday + altura )
    print(f'Coordenadas de recorte: {cortarcoord}')
    imgcortada = img.crop(cortarcoord)
    imgcortada.show()

folder = "recortes"
os.makedirs(folder, exist_ok=True)
x = 1
while True:
    recortepath = os.path.join(folder, f'recorte{x}.png')
    if not os.path.exists(recortepath):
        break
    x += 1

imgcortada.save(recortepath)
print(f'El recorte ha sido guardado como {recortepath}')
