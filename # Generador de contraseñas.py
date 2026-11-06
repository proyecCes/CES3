# Generador de contraseñas
# Combina letras, números y símbolos usando el módulo secrets.

import secrets
import string


def generar_contrasena(longitud=12):
    if longitud < 4:
        raise ValueError("La longitud debe ser de al menos 4 caracteres.")

    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = "!@#$%&*+-_?"

    # Garantiza al menos un carácter de cada tipo.
    caracteres = [
        secrets.choice(minusculas),
        secrets.choice(mayusculas),
        secrets.choice(numeros),
        secrets.choice(simbolos),
    ]

    todos = minusculas + mayusculas + numeros + simbolos

    for _ in range(longitud - 4):
        caracteres.append(secrets.choice(todos))

    secrets.SystemRandom().shuffle(caracteres)
    return "".join(caracteres)


def main():
    print("=== GENERADOR DE CONTRASEÑAS ===")

    try:
        longitud = int(input("¿Cuántos caracteres deseas? "))
        contrasena = generar_contrasena(longitud)
        print("\nContraseña generada:", contrasena)

    except ValueError as error:
        print("\nDato no válido:", error)

    finally:
        # Evita que la ventana se cierre inmediatamente al ejecutar
        # el archivo con doble clic.
        input("\nPresiona ENTER para cerrar el programa...")


if __name__ == "__main__":
    main()
