import os
import shutil

def obtener_carpetas_cache_en_sistema():
    carpetas_cache = []

    # Cambia la ruta base según tus necesidades
    ruta_base = "./"  # Puedes cambiarlo según tu preferencia

    for directorio_actual, carpetas, archivos in os.walk(ruta_base):
        for carpeta in carpetas:
            # Puedes ajustar los criterios de búsqueda según tu necesidad
            if "cache" in carpeta.lower():
                ruta_completa = os.path.join(directorio_actual, carpeta)
                carpetas_cache.append(ruta_completa)

    return carpetas_cache

def mostrar_opciones_carpetas(carpetas):
    print("Opciones de carpetas con caché encontrada:")
    for i, carpeta in enumerate(carpetas, 1):
        print(f"{i}. {carpeta}")

def eliminar_cache(opcion_seleccionada):
    try:
        # Lista de carpetas de caché en el sistema
        carpetas_cache_en_sistema = obtener_carpetas_cache_en_sistema()

        if not carpetas_cache_en_sistema:
            print("No se encontraron carpetas de caché en el sistema.")
            return

        try:
            opcion_seleccionada = int(opcion_seleccionada)
            if 1 <= opcion_seleccionada <= len(carpetas_cache_en_sistema):
                carpeta_seleccionada = carpetas_cache_en_sistema[opcion_seleccionada - 1]
                # Mostrar la carpeta seleccionada
                print(f"Carpeta seleccionada: {carpeta_seleccionada}")
                # Confirmar con el usuario si desea proceder
                respuesta = input(f"¿Desea eliminar los archivos de la carpeta de caché seleccionada? (s/n): ").lower()
                if respuesta == "s":
                    # Eliminar archivos de caché
                    shutil.rmtree(carpeta_seleccionada)
                    print(f"Carpeta eliminada: {carpeta_seleccionada}")
                else:
                    print("Operación cancelada.")
            else:
                print("Opción no válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    except Exception as e:
        print(f"Error al eliminar la caché: {e}")

# Obtener carpetas de caché en el sistema
carpetas_cache_en_sistema = obtener_carpetas_cache_en_sistema()

# Mostrar opciones de carpetas y permitir al usuario seleccionar una
mostrar_opciones_carpetas(carpetas_cache_en_sistema)
opcion_seleccionada = input("Seleccione el número de la carpeta que desea eliminar (o '0' para cancelar): ")

if opcion_seleccionada != '0':
    eliminar_cache(opcion_seleccionada)
