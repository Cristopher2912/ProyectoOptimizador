import os
import shutil

def obtener_carpetas_cache(ruta_directorio):
    carpetas_cache = []

    # Lista todos los archivos y carpetas en la ruta proporcionada
    for elemento in os.listdir(ruta_directorio):
        ruta_completa = os.path.join(ruta_directorio, elemento)

        # Verifica si es un directorio y si contiene la palabra "cache"
        if os.path.isdir(ruta_completa) and "cache" in elemento.lower():
            carpetas_cache.append(ruta_completa)

    return carpetas_cache

def eliminar_cache(ruta_directorio):
    try:
        # Lista de carpetas de caché
        carpetas_cache = obtener_carpetas_cache(ruta_directorio)

        if not carpetas_cache:
            print("No se encontraron carpetas de caché en la ruta proporcionada.")
            return

        # Mostrar carpetas de caché al usuario
        print("Carpetas de caché encontradas:")
        for carpeta in carpetas_cache:
            print(f"- {carpeta}")

        # Confirmar con el usuario si desea proceder
        respuesta = input("¿Desea eliminar los archivos de estas carpetas de caché? (s/n): ").lower()
        if respuesta != "s":
            print("Operación cancelada.")
            return

        # Eliminar archivos de caché
        for carpeta in carpetas_cache:
            shutil.rmtree(carpeta)
            print(f"Carpetas eliminadas: {carpeta}")

    except Exception as e:
        print(f"Error al eliminar la caché: {e}")

# Solicitar al usuario la ruta del directorio
directorio_a_limpiar = input("Ingrese la ruta del directorio donde desea buscar carpetas de caché: ")

# Verificar si la ruta es válida
if os.path.exists(directorio_a_limpiar):
    eliminar_cache(directorio_a_limpiar)
else:
    print("La ruta ingresada no es válida.")
