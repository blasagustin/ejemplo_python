import random

word = random.choice(words)
guessed = []
attempts = 6
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        puntaje += 6 
        print(f"tu puntaje final: {puntaje}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")
    if len(letter) != 1 or not letter.isalpha():
        print("entrada no válida")
        continue
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
        print(f"tu puntaje actual: {puntaje}")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje -= 1 
        print("Esa letra no está en la palabra.")
        print(f"tu puntaje actual: {puntaje}")

    print()

else:
    print(f"¡Perdiste! La palabra era: {word}")
    puntaje = 0
    print(f"tu puntaje final: {puntaje}")

 