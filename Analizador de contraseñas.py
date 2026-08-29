password = input("Escribí una contraseña ")

print("tu contraseña tiene", len(password), "caracteres")
for char in password:
    if char.isupper():
        print("Tiene mayúsculas")
        break
for char in password:
    if char.islower():
        print("Tiene minúsculas")
        break
caracteres_especiales = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
for char in password:
    if char in caracteres_especiales:
        print("Tiene caracteres especiales")
        break
for char in password:
    if char.isdigit():
        print("Tiene números")
        break
length = len(password)
if length >= 8:
    print("Tiene al menos 8 caracteres")
else:
    print("No tiene al menos 8 caracteres") 
while True:
    if length >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char in caracteres_especiales for char in password) and any(char.isdigit() for char in password):
        print("La contraseña es segura")
        break
    else:
        print("La contraseña no es segura")
        break

score = 0
if len(password) >= 8:
    score += 1
if any(char.isupper() for char in password):
    score += 1
if any(char.islower() for char in password):
    score += 1
if any(char in caracteres_especiales for char in password):
    score += 1
if any(char.isdigit() for char in password):
    score += 1

if score == 5:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")

    if score == 4:
        print("Nivel de seguridad: Alta")
    elif score == 3:
        print("Nivel de seguridad: Media")
    elif score == 2:
        print("Nivel de seguridad: Baja") 
    elif score == 1:
        print("Nivel de seguridad: Muy baja")
print("Puntaje de seguridad:", score, "/ 5")