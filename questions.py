 import random

# Diccionario de palabras por categoría
categorias = {
    "Animales": ["gato", "perro", "elefante", "pajaro", "serpiente", "tigre"],
    "Frutas": ["manzana", "naranja", "platano", "sandia", "uva", "limon"],
    "Países": ["argentina", "brasil", "peru", "chile", "mexico", "españa"],
    "Programación": ["python", "variable", "funcion", "bucle", "lista", "diccionario"],
}

# Llevar registro de palabras usadas en todas las rondas
palabras_usadas_global = set()

def obtener_categoria():
    """Permite al usuario elegir una categoría"""
    print("\n" + "="*50)
    print("CATEGORÍAS DISPONIBLES:")
    print("="*50)
    lista_categorias = list(categorias.keys())
    for i, cat in enumerate(lista_categorias, 1):
        print(f"{i}. {cat}")
    
    while True:
        try:
            opcion = input("\nSelecciona una categoría (número): ").strip()
            if not opcion or len(opcion) != 1 or not opcion.isdigit():
                print("Entrada no válida")
                continue
            opcion = int(opcion)
            if 1 <= opcion <= len(lista_categorias):
                return lista_categorias[opcion - 1]
            else:
                print("Opción no válida")
        except ValueError:
            print("Entrada no válida")

def seleccionar_palabra(categoria):
    """Selecciona una palabra de la categoría que no haya sido usada"""
    palabras_disponibles = [p for p in categorias[categoria] if p not in palabras_usadas_global]
    
    if not palabras_disponibles:
        return None
    
    palabra = random.choice(palabras_disponibles)
    palabras_usadas_global.add(palabra)
    return palabra

def validar_entrada(entrada):
    """Valida que la entrada sea una sola letra válida"""
    if len(entrada) == 1 and entrada.isalpha():
        return True
    return False

def calcular_puntuacion(adivinada, intentos_restantes, intentos_iniciales):
    """Calcula la puntuación según las reglas"""
    if intentos_restantes == 0:  # Perdió
        return 0
    else:  # Ganó
        errores = intentos_iniciales - intentos_restantes
        return 6 - errores

def jugar_ronda():
    """Juega una ronda del Ahorcado"""
    global palabras_usadas_global
    
    # Obtener categoría y palabra
    categoria = obtener_categoria()
    word = seleccionar_palabra(categoria)
    
    if word is None:
        print("\n" + "="*50)
        print(f"No hay más palabras disponibles en {categoria}")
        print("="*50)
        return None
    
    guessed = []
    attempts = 6
    intentos_iniciales = attempts
    adivinada = False
    
    print(f"\n¡Comenzó una nueva ronda! Categoría: {categoria}")
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
            print("¡Ganaste! ¡Correcta!")
            adivinada = True
            break
        
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(sorted(guessed))}")
        
        letter = input("Ingresá una letra: ").strip().lower()
        
        # Validar entrada
        if not validar_entrada(letter):
            print("Entrada no válida")
            print()
            continue
        
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no está en la palabra.")
        
        print()
    
    else:
        print(f"¡Perdiste! La palabra era: {word}")
    
    # Calcular y mostrar puntuación
    puntuacion = calcular_puntuacion(adivinada, attempts, intentos_iniciales)
    print("\n" + "="*50)
    if adivinada:
        print(f"¡GANASTE LA RONDA! Puntaje: {puntuacion}")
    else:
        print(f"PERDISTE LA RONDA. Puntaje: {puntuacion}")
    print("="*50)
    
    return puntuacion

# Programa principal
print("="*50)
print("¡BIENVENIDO AL AHORCADO!")
print("="*50)

puntaje_total = 0
jugar = True

while jugar:
    puntuacion_ronda = jugar_ronda()
    
    if puntuacion_ronda is not None:
        puntaje_total += puntuacion_ronda
        print(f"\nPuntaje acumulado: {puntaje_total}")
    
    print()
    continuar = input("¿Deseas jugar otra ronda? (s/n): ").strip().lower()
    if continuar != "s":
        jugar = False

print("\n" + "="*50)
print(f"JUEGO FINALIZADO")
print(f"Puntaje final: {puntaje_total}")
print("="*50)