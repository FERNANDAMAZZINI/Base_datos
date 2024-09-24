import calendar


def mostrar_calendario(año, mes):
    # Mostrar el calendario del mes
    print(calendar.month(año, mes))


def main():
    print("Bienvenido al programa de calendario")

    while True:
        try:
            año = int(input("Introduce el año (o 0 para salir): "))
            if año == 0:
                print("Saliendo...")
                break

            mes = int(input("Introduce el mes (1-12): "))

            if 1 <= mes <= 12:
                mostrar_calendario(año, mes)
            else:
                print("Por favor, introduce un mes válido (1-12).")
        except ValueError:
            print("Entrada no válida. Asegúrate de introducir un número.")


if __name__ == '__main__':
    main()
