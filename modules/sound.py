pi#requiere librerías que no vienen instaladas
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

### Para probar con argparser poner esto como comentario
#Presentador_de_sonido(r"C:\Users\edghb\Downloads\cintas-de-prueba-_1",1)

    
parser = argparse.ArgumentParser(description = 'Reproduce un audio')
parser.add_argument('veces', type = int, help = 'Ingrese un entero del rango de Veces [1 - 10] que desea escuchar el audio')
parser.add_argument('archivo', type = str, help = 'Ingrese el Nombre del audio')
group = parser.add_mutually_exclusive_group()
group.add_argument('-t','--time',action= 'store_true',help= 'Muestra tiempo de ejecución')
args = parser.parse_args()

t0= time.time()
Presentador_de_sonido(args.archivo,args.veces)
t1= time.time() - t0

if args.time:
    print ('Tiempo de ejecución: ' , round(t1, 6), 'segundos.')
