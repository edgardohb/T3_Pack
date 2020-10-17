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


#M Argparser function
def main():
    parser = argparse.ArgumentParser(description = 'Esta funcion escala una imagen y la muestra, el usuario elige el archivo de imagen a escalar y la escala deseada')
    parser.add_argument('escala' , type = int, help = 'Escala a utilizar para modificar la imagen. El usuario ingresa un numero del 1 al 3, a continuación se presentan las escalas disponibles y su respectivo numero: 1 para escala 1:1, 2 para escala 1:2, 3 para escala 2:1')
    parser.add_argument('archivo', type = str, help = 'Nombre del archivo de la imagen que se desea escalar. No es necesario ingresar la extension .jpg del archivo')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t', '--time', action= 'store_true', help= 'Muestra tiempo de ejecución del programa')
    args = parser.parse_args()

    t0= time.time()
    Presentador_de_imágenes(args.archivo,args.escala)
    t1= time.time() - t0

    if args.time:
        print ('Tiempo de ejecución: ', round(t1, 6), 'segundos.')
        