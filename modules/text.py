# Importa la librería tabulate para generar la tabla de palabras y frecuencia
from tabulate import tabulate
import argparse
import time

# Metódo de Analizador de Texto
# Función: Lee la cantidad de palabras repetidas en txt, separadas por "_"
# Input: Dirección de archivo de texto a leer
# Output: Archivo de txt con una tabla de las palabras y su frecuencia
def text_analyzer(adress):
    # Descarga el contenido de archivo de texto en una variable
    f = open (adress,'r')
    text = f.read()
    f.close()
    #Saca el largo del texto por caracter
    #Recorre el texto identificando palabras y _
    final_tab=[] #Array de lista con formato [palabra, frecuencia]
    words = text.split("_")
    for i in range(len(words)):
        words[i] = words[i].lower()
        found = False #Bandera que indica si la palabra fue encontrada
        # Busca si la palabra ya fue encontrada
        for j in range(len(final_tab)):
            #Si fue encontrada antes, suma 1 a la frecuencia
            if (final_tab[j][0] == words[i]):
                final_tab[j][1] = final_tab[j][1] + 1
                found = True # Sube bandera de palabra encontrada
                break
        # Si la palabra no ha sido encontrada, se añade a la lista
        if (found == False):
            final_tab.append([words[i],1])
    # Crea un archivo de texto llamado found_words.txt, donde tabula el resultado
    g = open ('found_words.txt','w') 
    g.write("Diferentes palabras en el texto y su frecuencia: \n")
    g.write(tabulate(final_tab))
    g.close()   

def main():
    parser = argparse.ArgumentParser(description = 'Presenta una tabla de cantidades de palabras ')
    parser.add_argument('texto', type = str , metavar = '', help = 'Ingrese el Nombre del archivo de texto')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-t','--time',action= 'store_true',help= 'Muestra tiempo de ejecución')
    args = parser.parse_args()

    t0= time.time()   
    text_analyzer(args.texto)
    t1= time.time() - t0

    if args.time:
        print ('Tiempo de ejecución: ', round(t1,6), 'segundos.')
