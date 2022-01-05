import random
import os
import time

def read():
    words = []
    with open("./archivos/data.txt","r", encoding="utf-8") as f:
        [words.append(line) for line in f]
    return words


def randword(words):
    word_random= random.choice(words)
    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b)
    word_random = word_random.translate(trans)
    word_random= word_random.upper()
    return word_random


def initialize(word_random):
    size = len(word_random)
    size = size - 1
    sep_word_random = {i:word_random[i] for i in range(size)}
    missing_letters = {i: "_" for i in range(size)}
    return sep_word_random, missing_letters


def process(initialize_dict):
    sep_word_random = initialize_dict[0]
    missing_letters = initialize_dict[1]
    error = 0

    while missing_letters != sep_word_random and error==0:
        os.system("cls")
        print('¡Adivina la palabra!')

        for values in missing_letters.values():
            print(values + " ", end = "")

        print('\n')
        
        letter = input('Ingresa una letra: ')
        try:
            if letter.isnumeric():
                raise ValueError("¡Sólo se aceptan letras!")
                time.sleep(5)
            else: 
                letter = letter.upper()

                for key, value in sep_word_random.items():
                    if letter == value:
                        missing_letters[key] = letter
        except ValueError as ve:
            print(ve)
            time.sleep(3)

    return missing_letters


   
    
def end(word_random):

    os.system("cls")
    print('¡Felicidades! Has ganado el juego, la palabra era: ', word_random )         

    

def run():

    words = read()
    word_random = randword(words)
    initialize_dict = initialize(word_random)
    process(initialize_dict)
    end(word_random)


if __name__ == '__main__':
    run()