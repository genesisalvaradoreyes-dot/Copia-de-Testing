# =====================================
# ANALIZADOR DE TEXTO / LOGS
# =====================================

from collections import Counter

# -------------------------------
# FUNCIONES
# -------------------------------

def leer_archivo(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print("❌ Archivo no encontrado")
        return None


def estadisticas_basicas(texto):
    lineas = texto.splitlines()
    palabras = texto.split()
    caracteres = len(texto)

    return {
        "lineas": len(lineas),
        "palabras": len(palabras),
        "caracteres": caracteres
    }


def frecuencia_palabras(texto, top=10):
    palabras = texto.lower().split()
    contador = Counter(palabras)
    return contador.most_common(top)


def buscar_palabra(texto, palabra):
    return texto.lower().count(palabra.lower())


def mostrar_menu():
    print("\n===== ANALIZADOR DE TEXTO =====")
    print("1. Ver estadísticas básicas")
    print("2. Ver palabras más frecuentes")
    print("3. Buscar palabra")
    print("4. Salir")


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------

ruta = input("Ruta del archivo de texto: ")
texto = leer_archivo(ruta)

if texto is None:
    exit()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        stats = estadisticas_basicas(texto)
        print("\n📊 ESTADÍSTICAS")
        print(f"Líneas: {stats['lineas']}")
        print(f"Palabras: {stats['palabras']}")
        print(f"Caracteres: {stats['caracteres']}")

    elif opcion == "2":
        top = int(input("¿Cuántas palabras mostrar?: "))
        frecuentes = frecuencia_palabras(texto, top)
        print("\n🔥 PALABRAS MÁS FRECUENTES")
        for palabra, cantidad in frecuentes:
            print(f"{palabra}: {cantidad}")

    elif opcion == "3":
        palabra = input("Palabra a buscar: ")
        cantidad = buscar_palabra(texto, palabra)
        print(f"🔍 '{palabra}' aparece {cantidad} veces")

    elif opcion == "4":
        print("👋 Saliendo del analizador")
        break

    else:
        print("❌ Opción inválida")
