# 🔐 Generador de Contraseñas Seguras

Un generador de contraseñas seguro y aleatorio desarrollado en Python que garantiza la creación de contraseñas robustas con una combinación balanceada de diferentes tipos de caracteres.

## ✨ Características

- 🎲 **Generación aleatoria**: Utiliza el módulo `random` de Python para máxima aleatoriedad
- 🔒 **Seguridad garantizada**: Incluye obligatoriamente:
  - Letras mayúsculas (A-Z)
  - Letras minúsculas (a-z)
  - Números (0-9)
  - Símbolos especiales (!@#$%^&\*, etc.)
- ⚙️ **Longitud personalizable**: Define la longitud de tu contraseña (mínimo 4 caracteres)
- 🔀 **Distribución aleatoria**: Los caracteres se mezclan aleatoriamente para evitar patrones predecibles
- 🐍 **Simple y ligero**: Sin dependencias externas, solo la biblioteca estándar de Python

## 📋 Requisitos

- Python 3.6 o superior
- No requiere dependencias externas

## 🚀 Instalación

1. Clona este repositorio:

```bash
git clone <url-del-repositorio>
cd generador_contraseñas
```

2. (Opcional - Si usas Linux o Mac este paso es obligatorio) Crea y activa un entorno virtual:

```bash
python -m venv venv

# En Linux/Mac:
source venv/bin/activate

# En Windows:
venv\Scripts\activate
```

## 💻 Uso

### Uso Básico

Ejecuta el script directamente para generar una contraseña de 20 caracteres:

```bash
python generador.py
```

Salida esperada:

```
✅ Contraseña generada (Longitud: 20): aB3!xYz9@mNpQr7#sT2u
```

### Uso como Módulo

Puedes importar la función en tus propios scripts:

```python
from generador import generar_contrasena

# Generar una contraseña de longitud predeterminada (20 caracteres)
password = generar_contrasena()
print(password)

# Generar una contraseña con longitud personalizada
password_corta = generar_contrasena(12)
print(password_corta)

password_larga = generar_contrasena(32)
print(password_larga)
```

## 📖 Documentación de la API

### `generar_contrasena(longitud=20)`

Genera una contraseña segura y aleatoria.

**Parámetros:**

- `longitud` (int, opcional): La longitud deseada de la contraseña. Por defecto es 20.
  - Valor mínimo: 4 (para incluir al menos un carácter de cada tipo)

**Retorna:**

- `str`: Una contraseña aleatoria con la longitud especificada
- `None`: Si la longitud es menor a 4

**Ejemplo:**

```python
# Genera una contraseña de 16 caracteres
password = generar_contrasena(16)

# Manejo de errores
password = generar_contrasena(3)  # Retorna None y muestra error
```

## 🔍 Cómo Funciona

El generador sigue estos pasos para crear una contraseña segura:

1. **Define conjuntos de caracteres**: Minúsculas, mayúsculas, números y símbolos
2. **Garantiza diversidad**: Selecciona al menos un carácter de cada tipo
3. **Completa la longitud**: Añade caracteres aleatorios hasta alcanzar la longitud deseada
4. **Mezcla aleatoriamente**: Reorganiza todos los caracteres para evitar patrones
5. **Retorna el resultado**: Convierte la lista en una cadena de texto

## 🛡️ Consideraciones de Seguridad

- Las contraseñas generadas son **criptográficamente seguras** para uso general
- Para aplicaciones de máxima seguridad, considera usar `secrets` en lugar de `random`:
  ```python
  import secrets
  # Modifica random.choice() por secrets.choice() en el código
  ```
- **No reutilices contraseñas** entre diferentes servicios
- Almacena las contraseñas en un **gestor de contraseñas** seguro
- Considera implementar una longitud mínima de **16 caracteres** para mayor seguridad

## 📁 Estructura del Proyecto

```
generador_contraseñas/
│
├── generador.py      # Script principal del generador
├── README.md         # Documentación del proyecto
├── .gitignore        # Archivos ignorados por Git
└── venv/             # Entorno virtual (no incluido en el repositorio)
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`)
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📝 Ideas para Mejoras Futuras

- [ ] Interfaz gráfica (GUI) con Tkinter o PyQt
- [ ] Opción para excluir caracteres ambiguos (0, O, l, 1, etc.)
- [ ] Generación de múltiples contraseñas a la vez
- [ ] Exportación de contraseñas a archivo seguro
- [ ] Evaluador de fuerza de contraseñas
- [ ] Versión CLI con argumentos personalizables
- [ ] Modo de generación de frases contraseña (passphrase)

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso libre.

## 👤 Autor

- alexgrt5

Creado con ❤️ para la práctica de Python y seguridad informática.

---

**⚠️ Nota**: Este generador está diseñado con fines educativos y de uso personal. Para aplicaciones empresariales o de misión crítica, considera usar soluciones profesionales de gestión de contraseñas.
