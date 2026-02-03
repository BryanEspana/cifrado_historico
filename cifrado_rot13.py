from cifrado_cesar import cesar_cifrar

def rot13(mensaje):
    return cesar_cifrar(mensaje, 13)

if __name__ == "__main__":
    msg = "hola como estas"
    cifrado = rot13(msg)
    print(f"Original: {msg}")
    print(f"ROT13: {cifrado}")
    print(f"ROT13 x2: {rot13(cifrado)}")
