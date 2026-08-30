VERDE = "\033[92m"
AMARILLO = "\033[93m"
ROJO = "\033[91m"
RESTABLECER = "\033[0m"


def analizar_contraseña(password):
    print(f"Tu contraseña tiene {len(password)} caracteres")

    caracteres_especiales = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(char in caracteres_especiales for char in password)
    has_number = any(char.isdigit() for char in password)
    length = len(password)

    if has_upper:
        print("Tiene mayúsculas:", VERDE + "✅" + RESTABLECER)
    else:
        print("No tiene mayúsculas:", ROJO + "❌" + RESTABLECER)

    if has_lower:
        print("Tiene minúsculas:", VERDE + "✅" + RESTABLECER)
    else:
        print("No tiene minúsculas:", ROJO + "❌" + RESTABLECER)

    if has_special:
        print("Tiene caracteres especiales:", VERDE + "✅" + RESTABLECER)
    else:
        print("No tiene caracteres especiales:", ROJO + "❌" + RESTABLECER)

    if has_number:
        print("Tiene números:", VERDE + "✅" + RESTABLECER)
    else:
        print("No tiene números:", ROJO + "❌" + RESTABLECER)

    if length >= 8:
        print("Tiene al menos 8 caracteres:", VERDE + "✅" + RESTABLECER)
    else:
        print("Tiene al menos 8 caracteres:", ROJO + "❌" + RESTABLECER)

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_special:
        score += 1
    if has_number:
        score += 1

    if score == 5:
        nivel = "Muy alta"
    elif score == 4:
        nivel = "Alta"
    elif score == 3:
        nivel = "Media"
    elif score == 2:
        nivel = "Baja"
    else:
        nivel = "Muy baja"

    print("Nivel de seguridad:", nivel)
    if score <= 2:
        color_puntaje = ROJO
    elif score <= 4:
        color_puntaje = AMARILLO
    else:
        color_puntaje = VERDE
    print("Puntaje de seguridad:", color_puntaje + str(score) + "/ 5" + RESTABLECER)


while True:
    password = input("Escribí una contraseña: ")
    analizar_contraseña(password)

    otra_vez = input("\n¿Queres analizar otra contraseña? (si/no): ")
    if otra_vez.lower() != "si":
        break

    print("\n----- NUEVA CONTRASEÑA -----")

print("\n" + VERDE + "Gracias por usar el analizador de contraseñas" + RESTABLECER)
