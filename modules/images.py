# Se deben instalar las librería, ya que estas no la traen
# se pueden instalr con los comandos: "pip install opencv-python" en phyton 2
# o "pip3 install opencv-python" Phyton 3
# y "pip install matplotlib"

import cv2
import matplotlib.pyplot as plt
import argparse
import time

# digite 1 si quiere ver la imagen a escala 1:1
# digite 2 si quiere ver la imagen a escala 1:2
# digite 3 si quiere ver la imagen a escala 2:1


# Presentador_de_imagenes


def Presentador_de_imágenes(archivo, escala):

    # se carga la imagen:
    im = cv2.imread(archivo+".jpg")
    # A continuacion se pondran los posibles errores de este metodo
    # Si los números ingresados al método no son entero
    if isinstance(escala, int) is False:
        # revisa que escala sea entero
        return "Error no es un entero"
    if ((escala > 3) | (escala < 1)):
        # revisa que el primer dato este entre 3 y 1
        return "Error dato fuera de rango"
    # en el caso de no existir un error
    if escala == 1:
        # acontinuación se define el tamaño de la imagen
        im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)
        # acontinuación se muestra la imagen con la escala seleccionada
        plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
        plt.show()
    if escala == 2:
        # acontinuación se define el tamaño de la imagen
        im_resized = cv2.resize(im, (224, 448), interpolation=cv2.INTER_LINEAR)
        # acontinuación se muestra la imagen con la escala seleccionada
        plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
        plt.show()
    if escala == 3:
        # acontinuación se define el tamaño de la imagen
        im_resized = cv2.resize(im, (448, 224), interpolation=cv2.INTER_LINEAR)
        # acontinuación se muestra la imagen con la escala seleccionada
        plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
        plt.show()

### Para probar con argparser poner esto como comentario

#Presentador_de_imágenes(r"C:\Users\edghb\Pictures\Saved Pictures\space-walk-nasa-796x457",2)

def main():
    parser = argparse.ArgumentParser(description = 'Presenta una imagen')
    parser.add_argument('escala' , type = int, help = 'Ingrese un entero para la Escala 1: para escala 1:1, 2: para escala 1:2 , 3: para escala 2:1')
    parser.add_argument('archivo', type = str, help = 'Ingrese el Nombre de la imagen')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t', '--time', action= 'store_true', help= 'Muestra tiempo de ejecución')
    args = parser.parse_args()

    t0= time.time()
    Presentador_de_imágenes(args.archivo,args.escala)
    t1= time.time() - t0

    if args.time:
        print ('Tiempo de ejecución: ', round(t1, 6), 'segundos.') 
