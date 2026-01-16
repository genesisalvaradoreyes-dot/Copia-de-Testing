# =====================================
# GESTOR DE TAREAS (TODO APP)
# =====================================

import json
import os
from datetime import datetime

ARCHIVO = "tareas.json"

# -------------------------------
# UTILIDADES
# -------------------------------

def cargar_tareas():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)


def mostrar_menu():
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar como completada")
    print("4. Eliminar tarea")
    print("5. Filtrar (pendientes/completadas)")
    print("6. Salir")


def mostrar_tareas(tareas):
    if not tareas:
        print("📭 No hay tareas")
        return

    for i, t in enumerate(tareas, start=1):
        estado = "✅" if t["completada"] else "⏳"
        print(f"{i}. {estado} {t['titulo']} | creada: {t['creada']}")


# -------------------------------
# OPERACIONES
# -------------------------------

def agregar_tarea(tareas):
    titulo = input("Título de la tarea: ").strip()
    if not titulo:
        print("❌ El título no puede estar vacío")
        return

    tarea = {
        "titulo": titulo,
        "completada": False,
        "creada": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tareas.append(tarea)
    guardar_tareas(tareas)
    print("✅ Tarea agregada")


def completar_tarea(tareas):
    mostrar_tareas(tareas)
    if not tareas:
        return

    try:
        idx = int(input("Número de tarea: ")) - 1
        tareas[idx]["completada"] = True
        guardar_tareas(tareas)
        print("🎉 Tarea completada")
    except (ValueError, IndexError):
        print("❌ Selección inválida")


def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    if not tareas:
        return

    try:
        idx = int(input("Número de tarea a eliminar: ")) - 1
        eliminado = tareas.pop(idx)
        guardar_tareas(tareas)
        print(f"🗑️ Tarea eliminada: {eliminado['titulo']}")
    except (ValueError, IndexError):
        print("❌ Selección inválida")


def filtrar_tareas(tareas):
    opcion = input("Ver (p)endientes o (c)ompletadas?: ").lower()
    if opcion == "p":
        filtradas = [t for t in tareas if not t["completada"]]
    elif opcion == "c":
        filtradas = [t for t in tareas if t["completada"]]
    else:
        print("❌ Opción inválida")
        return

    mostrar_tareas(filtradas)


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------

tareas = cargar_tareas()

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_tareas(tareas)
    elif opcion == "2":
        agregar_tarea(tareas)
    elif opcion == "3":
        completar_tarea(tareas)
    elif opcion == "4":
        eliminar_tarea(tareas)
    elif opcion == "5":
        filtrar_tareas(tareas)
    elif opcion == "6":
        print("👋 Saliendo del gestor")
        break
    else:
        print("❌ Opción inválida")
