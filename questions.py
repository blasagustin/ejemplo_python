
import random

categorias = {
    "Programacion": ["python", "programa", "variable", "funcion","bucle"],
    "variable": ["cadena","entero","lista"]
}

print("Categorías disponibles:")
for cat in categorias:
    print(f"- {cat}")

eleccion = input("Elegí una categoría: ")
while eleccion not in categorias:
    eleccion = input("Categoría no válida. Elegí una respetando mayúsculas: ")

words = random.sample(categorias[eleccion], len(categorias[eleccion]))

while True:
    if len(words) == 0:
        print("¡Ya jugaste todas las palabras de esta categoría!")
        break
        
    import random

    word = random.choice(words)
    guessed = []
    attempts = 6
    puntaje = 0

    print("¡Bienvenido al Ahorcado!")
    print()

    while attempts > 0:
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

       
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
        
  
    words.remove(word)
    
    jugar_nuevo = input("¿Querés jugar otra ronda? (si/no): ")
    if jugar_nuevo.lower() != 'si':
        break
    

 