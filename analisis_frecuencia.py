ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

FREQ_ESPANOL = {
    'A': 12.53, 'B': 1.42, 'C': 4.68, 'D': 5.86, 'E': 13.68, 'F': 0.69,
    'G': 1.01, 'H': 0.70, 'I': 6.25, 'J': 0.44, 'K': 0.02, 'L': 4.97,
    'M': 3.15, 'N': 6.71, 'O': 8.68, 'P': 2.51, 'Q': 0.88, 'R': 6.87,
    'S': 7.98, 'T': 4.63, 'U': 3.93, 'V': 0.90, 'W': 0.01, 'X': 0.22,
    'Y': 0.90, 'Z': 0.52
}

def analisis_frecuencia(mensaje):
    contadores = {letra: 0 for letra in ALFABETO}
    total = 0
    for c in mensaje.upper():
        if c in ALFABETO:
            contadores[c] += 1
            total += 1
    return {letra: (contadores[letra] / total * 100) if total > 0 else 0 for letra in ALFABETO}

def mostrar_tabla(frecuencias):
    ordenado = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    print(f"{'Letra':<6}{'Freq %':<10}Barra")
    print("-" * 35)
    for letra, freq in ordenado:
        if freq > 0:
            print(f"  {letra}    {freq:5.2f}%   {'█' * int(freq / 2)}")

if __name__ == "__main__":
    texto = "La criptografia es el arte de proteger mensajes"
    print(f"Texto: {texto}\n")
    freq = analisis_frecuencia(texto)
    mostrar_tabla(freq)
