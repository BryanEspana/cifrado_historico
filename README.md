# 🔐 Cifrados Históricos

<a id="readme-top"></a>

## 📜 Descripción

Este repositorio contiene implementaciones en Python de algoritmos de cifrado clásicos/históricos, incluyendo el cifrado César, ROT13, Vigenère y herramientas de análisis de frecuencia.

## 📁 Estructura del Proyecto

```
cifrado_historico/
├── cifrado_cesar.py      # Implementación del cifrado César
├── cifrado_rot13.py      # Implementación del cifrado ROT13
├── cifrado_vigenere.py   # Implementación del cifrado Vigenère
├── analisis_frecuencia.py # Herramienta de análisis de frecuencia
└── README.md
```

## ✨ Algoritmos Implementados

### 1. Cifrado César (`cifrado_cesar.py`)
Cifrado por sustitución donde cada letra se desplaza un número fijo de posiciones en el alfabeto.

**Funciones:**
- `cesar_cifrar(mensaje, desplazamiento)` - Cifra un mensaje
- `cesar_descifrar(mensaje, desplazamiento)` - Descifra un mensaje

**Ejemplo:**
```python
from cifrado_cesar import cesar_cifrar, cesar_descifrar

cifrado = cesar_cifrar("hola como estas", 3)
# Resultado: "krod frpr hvwdv"
```

### 2. ROT13 (`cifrado_rot13.py`)
Caso especial del cifrado César con desplazamiento fijo de 13 posiciones. Al aplicarlo dos veces se obtiene el mensaje original.

**Funciones:**
- `rot13(mensaje)` - Aplica ROT13 al mensaje

**Ejemplo:**
```python
from cifrado_rot13 import rot13

cifrado = rot13("hola como estas")
# Resultado: "ubyn pbzb rfgnf"
```

### 3. Cifrado Vigenère (`cifrado_vigenere.py`)
Cifrado polialfabético que utiliza una palabra clave para cifrar, aplicando diferentes desplazamientos según cada letra de la clave.

**Funciones:**
- `vigenere_cifrar(mensaje, clave)` - Cifra con una clave
- `vigenere_descifrar(mensaje, clave)` - Descifra con una clave

**Ejemplo:**
```python
from cifrado_vigenere import vigenere_cifrar, vigenere_descifrar

cifrado = vigenere_cifrar("hola como estas", "bryan")
# Descifrar con la misma clave para recuperar el mensaje
```

### 4. Análisis de Frecuencia (`analisis_frecuencia.py`)
Herramienta para analizar la frecuencia de aparición de letras en un texto, útil para criptoanálisis de cifrados por sustitución.

**Funciones:**
- `analisis_frecuencia(mensaje)` - Retorna diccionario con frecuencias
- `mostrar_tabla(frecuencias)` - Muestra tabla visual de frecuencias

**Ejemplo:**
```python
from analisis_frecuencia import analisis_frecuencia, mostrar_tabla

freq = analisis_frecuencia("La criptografia es el arte de proteger mensajes")
mostrar_tabla(freq)
```

## 🚀 Instalación y Ejecución

1. Clona este repositorio:

    ```bash
    git clone https://github.com/BryanEspana/cifrado_historico.git
    cd cifrado_historico
    ```

2. Ejecuta cualquier script directamente con Python:

    ```bash
    python cifrado_cesar.py
    python cifrado_rot13.py
    python cifrado_vigenere.py
    python analisis_frecuencia.py
    ```

## 📋 Requisitos

- Python 3.x
- No requiere dependencias externas

## 👤 Autor

**Bryan España**

[![Linkedin](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)](https://www.linkedin.com/in/bryan-españa-62094a212)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BryanEspana)
