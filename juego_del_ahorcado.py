import random
import os
import time

#This function triggers a welcome screen, it does not change until the user press enter.
def welcome_screen():
    os.system("cls")
    input("""

    ******************************************************************************************************
    ******************************************************************************************************
                            
                        ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
                        ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
                        ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
                        ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
                        ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
                        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝

    ******************************************************************************************************
    * Welcome player!                                                                                    *
    * You're about to play the hangman game and you may be wonder "How does it work?"                    *
    * Don´t worry it´s very simple, just type some letters and try to guess the hidden word.             *
    *                                                                                                    *
    *                                                                                                    *       
    *                                   Press ENTER to start!                                            *
    *                                                                                                    * 
    *                                                                                                    * 
    * Developer: Bruno Guillaume Hernández Villamil                                  Date: 2022/02/01    *
    ****************************************************************************************************** 
    """)


#This function opens a file and return its content in a list.
def read():
    words = []
    with open("./archivos/data.txt","r", encoding="utf-8") as f:
        [words.append(line) for line in f]
    return words

#This function takes a random word from the list obtained in the read function,
#changes all special characters, puts everything in capital letters and then returns the word.
def randword(words):
    word_random= random.choice(words)
    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b)
    word_random = word_random.translate(trans)
    word_random= word_random.upper()
    return word_random

#This function makes two dictionaries. The first cointains the random word selected but separated in letters.
#The second its the same as the first but with the letters hiden using "_" .
def initialize(word_random):
    size = len(word_random)
    size = size - 1
    sep_word_random = {i:word_random[i] for i in range(size)}
    missing_letters = {i: "_" for i in range(size)}
    return sep_word_random, missing_letters

#This function separates the dictionaries, while the two ditionaries are different the function keeps asking 
#For a letter. When a correct letter is introduced, it´s appended to the dictionary in it´s corresponding position.
#If a number is introduced, it triggers an error message and goes back to ask for a letter.
#When the two dictionaries become exactly the same this function returns the dictionary.
def process(initialize_dict):
    sep_word_random = initialize_dict[0]
    missing_letters = initialize_dict[1]


    while missing_letters != sep_word_random:
        os.system("cls")
        print('Guess the word!')

        for values in missing_letters.values():
            print(values + " ", end = "")

        print('\n')
        
        letter = input('Introduce a letter: ')
        try:
            if letter.isnumeric():
                raise ValueError("Letter only!")
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


   
#This functios triggers a winnig screen and gives the user the option to play again or exit.   
def end(word_random):

    option_error = 0

    os.system("cls")
    print('Congratulations! You won, the word was: ' + word_random)
    print('\n')

    while option_error == 0:
        try:
            play_again = int(input('If you want to play again press 1, if you want to exit press 2: '))
            option_error = 1

        except ValueError as ve:
            os.system("cls")
            print('Only numbers!')
            option_error = 0
            time.sleep(3)


    return play_again

#This function contains the program flow, it executes all the functions needed to make the game work.
def run():

    play_again = 1

    welcome_screen()
    
#This while function is used to give the user the option to play again or exit the game.
    while play_again == 1:
        words = read()
        word_random = randword(words)
        initialize_dict = initialize(word_random)
        process(initialize_dict)
        play_again = end(word_random)



if __name__ == '__main__':
    run()