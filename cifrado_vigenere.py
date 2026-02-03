ALFA_MAY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFA_MIN = "abcdefghijklmnopqrstuvwxyz"

def normalizar_clave(clave):
    return "".join(ALFA_MAY[ALFA_MIN.index(c)] if c in ALFA_MIN else c for c in clave if c in ALFA_MAY or c in ALFA_MIN)

def vigenere_cifrar(mensaje, clave):
    clave = normalizar_clave(clave)
    if not clave:
        return mensaje
    resultado, idx = "", 0
    for c in mensaje:
        if c in ALFA_MAY:
            resultado += ALFA_MAY[(ALFA_MAY.index(c) + ALFA_MAY.index(clave[idx % len(clave)])) % 26]
            idx += 1
        elif c in ALFA_MIN:
            resultado += ALFA_MIN[(ALFA_MIN.index(c) + ALFA_MAY.index(clave[idx % len(clave)])) % 26]
            idx += 1
        else:
            resultado += c
    return resultado

def vigenere_descifrar(mensaje, clave):
    clave = normalizar_clave(clave)
    if not clave:
        return mensaje
    resultado, idx = "", 0
    for c in mensaje:
        if c in ALFA_MAY:
            resultado += ALFA_MAY[(ALFA_MAY.index(c) - ALFA_MAY.index(clave[idx % len(clave)])) % 26]
            idx += 1
        elif c in ALFA_MIN:
            resultado += ALFA_MIN[(ALFA_MIN.index(c) - ALFA_MAY.index(clave[idx % len(clave)])) % 26]
            idx += 1
        else:
            resultado += c
    return resultado

if __name__ == "__main__":
    msg, clave = "hola como estas", "bryan"
    cifrado = vigenere_cifrar(msg, clave)
    print(f"Original: {msg} | Clave: {clave}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {vigenere_descifrar(cifrado, clave)}")
