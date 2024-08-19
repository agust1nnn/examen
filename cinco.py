from PIL import Image
import os
url = input("ingrese la ruta de  la imagen:")
rutaagua=input("ingrese el nombre de la ruta de la marca de agua:")
marcaagua=input("elije la ubicacion{superior izquierda,superior derecha,inferior izquierda,inferior derecha}")
foto = Image.open(url)
agua = Image.open(rutaagua)
margen = 50
print('Escriba 1, 2, 3 o 4')
print('\t1_Superior izquierda')
print('\t2_Superior derecha')
print('\t3_Inferior izquierda')
print('\t4_Inferior derecha')
ubicacion = input()

if ubicacion not in ['1', '2', '3', '4']:
    sys.exit('++Error: Usted debía ingresar 1, 2, 3 o 4++')
else:
    imagenew = Image.copy()

    if marcaagua.mode != 'RGBA':
        marcaagua = marcaagua.convert('RGBA')

    alphamask = marcaagua.split()[3]

    if ubicacion == '1':
        imagenew.paste(marcaagua, (margen, margen), mask=alphamask)
    elif ubicacion == '2':
        posx = Image.width - marcaagua.width - margen
        imagenew.paste(marcaagua, (posx, margen), mask=alphamask)
    elif ubicacion == '3':
        posy = Image.height - marcaagua.height - margen
        imagenew.paste(marcaagua, (margen, posy), mask=alphamask)
    else:
        posx = Image.width - marcaagua.width - margen
        posy = Image.height - marcaagua.height - margen
        imagenew.paste(marcaagua, (posx, posy), mask=alphamask)

    rutasalida = 'Manipulacion de imagenes/imagenes-recortes/imagenconmarcadeagua.png'
    imagenew.save(rutasalida)
    print(f'La imagen con marca de agua ha sido guardada como {rutasalida}')

    imagenew.show()
    