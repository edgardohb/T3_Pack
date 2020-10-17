
#requiere librerías que no vienen instaladas
#para intalarlas se utilizan los siguientes comandos:
#pip install playsound


from playsound import playsound
import argparse 
import time

# Presentador_de_imagenes
def Presentador_de_sonido(archivo, reproducciones):
    #aisgna el audio a NOMBRE_ARCHIVO
    NOMBRE_ARCHIVO = archivo+".mp3"
    # A continuacion se pondran los posibles errores de este metodo
    # Si los números ingresados al método no son entero
    if isinstance(reproducciones, int) is False:
        # revisa que escala sea entero
        return "Error no es un entero"
    # en el caso de no existir un error
    for i in range(reproducciones):
        #reproduce el audio
        playsound(NOMBRE_ARCHIVO)


def main(): 
    parser = argparse.ArgumentParser(description = 'Esta funcion reproduce un audio en formato mp3. El usuario elige el archivo de audio que desea escuchar y cuantas veces desea escucharlo')
    parser.add_argument('veces', type = int, help = 'Cantidad de veces que el usuario desea escuchar el audio. La cantidad minima de veces disponible es 1 y la maxima es 10')
    parser.add_argument('archivo', type = str, help = 'Nombre del archivo de audio que se desea escuchar. No es necesario que el usuario escriba la extension .mp3 del archivo')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t','--time',action= 'store_true',help= 'Muestra tiempo de ejecucion del programa')
    args = parser.parse_args()

    t0= time.time()
    Presentador_de_sonido(args.archivo,args.veces)
    t1= time.time() - t0

    if args.time:
        print ('Tiempo de ejecución: ' , round(t1, 6), 'segundos.')
