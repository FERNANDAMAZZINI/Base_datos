import random

def jugar():
    palabras = ["python", "programacion", "desarrollo", "jugando", "aventura"]
    palabra_secreta = random.choice(palabras)
    intentos = 6
    letras_adivinadas = []

    print("¡Bienvenido al juego de Adivina la Palabra!")
    print("Tienes que adivinar la palabra secreta.")
    print("_ " * len(palabra_secreta))

    while intentos > 0:
        letra = input("\nAdivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Prueba otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Correcto!")
        else:
            intentos -= 1
            print(f"Incorrecto. Te quedan {intentos} intentos.")

        # Mostrar el progreso
        progreso = ''.join(letra if letra in letras_adivinadas else '_' for letra in palabra_secreta)
        print("Palabra: ", ' '.join(progreso))

        if '_' not in progreso:
            print("¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            break
    else:
        print("Lo siento, has perdido. La palabra era:", palabra_secreta)

if __name__ == '__main__':
    jugar()
