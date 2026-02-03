ALFA_MAY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFA_MIN = "abcdefghijklmnopqrstuvwxyz"

def cesar_cifrar(mensaje, desplazamiento):
    resultado = ""
    for c in mensaje:
        if c in ALFA_MAY:
            resultado += ALFA_MAY[(ALFA_MAY.index(c) + desplazamiento) % 26]
        elif c in ALFA_MIN:
            resultado += ALFA_MIN[(ALFA_MIN.index(c) + desplazamiento) % 26]
        else:
            resultado += c
    return resultado

def cesar_descifrar(mensaje, desplazamiento):
    return cesar_cifrar(mensaje, -desplazamiento)

if __name__ == "__main__":
    msg = "hola como estas"
    cifrado = cesar_cifrar(msg, 3)
    print(f"Original: {msg}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {cesar_descifrar(cifrado, 3)}")
