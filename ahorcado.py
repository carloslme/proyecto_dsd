import random, time
superHeroes = ['hawkeye', 'robin', 'Galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman', 'aquaman']
userGuesslist = []
userGuesses = []

print("¡Hola! Vamos a comenzar el juego")
time.sleep(0.5)
print("El objetivo del juego es adivinar la palabra secreta elegida por la computadora.")
time.sleep(0.5)
print("Puedes adivinar una letra en un intento o ingresar la frase completa.")
time.sleep(0.5)
print("¡Comencemos!")
time.sleep(1)


#Choosing the Secret word

secretWord = random.choice(superHeroes)
secretWordList = list(secretWord)
attempts = (10)

#Utility function to print User Guess List
def printGuessedLetter():
    print("Tu palabra secreta es: " + ''.join(userGuesslist))


#Adding blank lines to userGuesslist to create the blank secret word
for n in secretWordList:
    userGuesslist.append(' _ ')
printGuessedLetter()

print("Tienes :", attempts, 'intentos')


#starting the game
while True:

    print("Adivina una letra o escribe la frase:")
    letter = input()

    if letter in userGuesses:
        print("Ya has adivinado esta letra o frase, prueba de nuevo.")

    else:
        attempts -= 1
        userGuesses.append(letter)
        if len(letter) == 1:
            if letter in secretWordList:
                print("¡Acertaste!")
                if attempts > 0:
                    print("¡Te quedan ", attempts, 'intentos!')
                for i in range(len(secretWordList)):
                    if letter == secretWordList[i]:
                        letterIndex = i
                        userGuesslist[letterIndex] = letter.upper()
                printGuessedLetter()
    
            else:
                print("¡Ups! Intentalo de nuevo.")
                if attempts > 0:
                    print("¡Te quedan ", attempts, 'intentos!')
                printGuessedLetter()
        elif letter.upper() == secretWord.upper():
            print('¡Acertaste! La palabra secreta es: ', secretWord.upper())
            print()
            print("¡Has ganado!")
            break
        else:
            print("¡Ups! Intentalo de nuevo.")
            if attempts > 0:
                print("¡Te quedan ", attempts, 'intentos!')
            printGuessedLetter()

    #Win/loss logic for the game
    joinedList = ''.join(userGuesslist)
    if joinedList.upper() == secretWord.upper():
        print('¡Bien hecho!')
        print()
        print("¡Has ganado!")
        break
    elif attempts == 0:
        print("Too many Guesses!, Sorry better luck next time.")
        print("The secret word was: "+ secretWord.upper())
        print('¡Adiós!')
        break

    
 