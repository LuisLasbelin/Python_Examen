import math
from operator import add, contains
from random import random
from select import select

def choose_secret(filename):
    """Dado un nombre de fichero, esta funcionn devuelve una palabra aleatoria de este fichero transformada a mayÃºsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayusculas. Ej. "CREMA"
    """
    f = open(filename + ".txt", mode="r", encoding="utf-8")

    archivo = ""
    texto = f.readline()
    archivo += texto;
    while texto != "":
        texto = f.readline()
        archivo += texto;
    f.close();

    palabras = archivo.split()
    rand = math.floor(random() * len(palabras))
    secret = palabras[rand].upper()
    return secret

def compare_words(word, secret):
    """Dadas dos palabras en mayÃºsculas (word y secret), esta funcion calcula las posiciones de las letras de word que aparecen en la misma posiciÃ³n en secret, y las posiciones de las letras de word que aparecen en secret pero en una posiciÃ³n distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posiciÃ³n en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras estÃ¡n en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    same_position = []
    same_letter = []

    for i in range(len(word)):
        # Si la letra esta en esa posicion
        if(word[i].upper() == secret[i]):
            same_position.append(i)

    for i in range(len(word)):
        # Si la letra no esta en esa posicion pero la contiene
        if(contains(secret, word[i].upper())):
            same_letter.append(i)

    return same_position, same_letter
def print_word(word, same_letter_position, same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta funciÃ³n crearÃ¡ un string donde aparezcan en mayÃºsculas las letras de la palabra que ocupen las posiciones de same_position, en minÃºsculas las letras de la palabra que ocupen las posiciones de same_letter y un guiÃ³n (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    transformed = []
    for i in range(len(word)):
        transformed.append("-")
    for i in same_letter:
        transformed[i] = word[i].lower()
    for i in same_position:
        transformed[i] = word[i].upper()
    # String
    result = ""
    for l in transformed:
        result += l
    return result
def choose_secret_advanced(filename):
    """Dado un nombre de fichero, esta funciÃ³n filtra solo las palabras de 5 letras que no tienen acentos (Ã¡,Ã©,Ã­,Ã³,Ãº). De estas palabras, la funciÃ³n devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayÃºsculas
    """
    f = open(filename + ".txt", mode="r", encoding="utf-8")

    archivo = ""
    texto = f.readline()
    archivo += texto;
    while texto != "":
        texto = f.readline()
        archivo += texto;
    f.close();
    palabras = archivo.split()

    selected = []
    filtradas = []
    # Se filtran
    for i in range(len(palabras)):
        # Sin acentos
        if(palabras[i].isascii()):
            # De 5 letras
            if(len(palabras[i]) == 5):
                filtradas.append(palabras[i])
    # Si hay menos de 15 palabras el archivo no es valido
    if 
    # Elige 15 palabras al azar, puede hacerse de otra forma pero esta es rapida de escribir
    while len(selected) < 15:
        rand = math.floor(random() * len(filtradas))
        # No esta en la lista
        if not (contains(selected, palabras[rand])):
            selected.append(palabras[rand].upper())

    rand = math.floor(random() * len(selected))
    secret = selected[rand]
    return selected, secret


def check_valid_word():
    """Dada una lista de palabras, esta funciÃ³n pregunta al usuario que introduzca una palabra hasta que introduzca una que estÃ© en la lista. Esta palabra es la que devolverÃ¡ la funciÃ³n.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que estÃ¡ en la lista.
    """
    

if __name__ == "__main__":
    archivo = input("Archivo de palabras: ")
    selected, secret=choose_secret_advanced(archivo)
    print("Lista de palabras seleccionadas: ")
    print(selected) #Debug: para ver que selecciona solo palabras sin acentos
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words(word, secret)
        resultado=print_word(word, same_position, same_letter)
        print(resultado)
        if resultado == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   
