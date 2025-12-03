import random
import string

def generar_contrasena(longitud=20):
    """
    Genera una contraseña segura y aleatoria con la longitud especificada.

    La contraseña garantiza la inclusión de: mayúsculas, minúsculas, números y símbolos.

    Parámetros:
    - longitud (int): La longitud deseada de la contraseña (por defecto es 12).
    """
    # 1. Definir los conjuntos de caracteres
    minusc = string.ascii_lowercase
    mayusc = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation
    
    # Conjunto total de caracteres disponibles
    caracteres = minusc + mayusc + numeros + simbolos
    
    # Aseguramos que la longitud sea suficiente para al menos un carácter de cada tipo
    if longitud < 4:
        print("Error: La longitud debe ser al menos 4 para incluir un carácter de cada tipo.")
        return None

    # 2. Garantizar la inclusión de al menos un carácter de cada tipo obligatorio
    password = [
        random.choice(minusc),
        random.choice(mayusc),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    # 3. Rellenar el resto de la contraseña
    # La longitud restante es: longitud total - los 4 caracteres ya agregados
    caracteres_restantes = longitud - 4
    
    for _ in range(caracteres_restantes):
        password.append(random.choice(caracteres))
        
    # 4. Mezclar la contraseña para asegurar la aleatoriedad
    random.shuffle(password)
    
    # 5. Unir la lista de caracteres en una cadena y retornar
    return "".join(password)

# Bloque de ejecución principal
if __name__ == "__main__":
    # Usamos la longitud de 20 caracteres que solicitaste
    longitud_solicitada = 20
    contrasena_generada = generar_contrasena(longitud_solicitada)
    
    if contrasena_generada:
        print(f"✅ Contraseña generada (Longitud: {longitud_solicitada}): {contrasena_generada}")