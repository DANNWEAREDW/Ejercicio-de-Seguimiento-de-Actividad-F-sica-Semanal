# Lista de ejemplo de minutos diarios de actividad física
actividad_fisica = [45, 30, 60, 20, 50, 40, 35]

# Función para calcular el tiempo promedio de actividad física diaria
def promedio_actividad_fisica(tiempos):
    if len(tiempos) == 0:  # Si la lista está vacía
        return 0
    return sum(tiempos) / len(tiempos)

# Llamada a la función
promedio_minutos = promedio_actividad_fisica(actividad_fisica)

# Imprimir el resultado
print(f"✉️ El tiempo promedio diario de actividad física es de {promedio_minutos:.2f} minutos.")

# Función lambda para convertir minutos a horas
minutos_a_horas = lambda minutos: minutos / 60

# Calcular el tiempo promedio en horas
promedio_horas = minutos_a_horas(promedio_minutos)

# Imprimir el resultado en horas
print(f"✉️ El tiempo promedio diario de actividad física es de {promedio_horas:.2f} horas por día.")

# Segundos a minutos
segundos_a_minutos = lambda segundos: segundos / 60

# Segundos a horas
segundos_a_horas = lambda segundos: segundos / 3600

# Lista de listas: tiempos de actividad física de diferentes usuarios
usuarios_actividad = [
    [45, 30, 60, 20, 50, 40, 35],  # Usuario 1
    [50, 25, 40, 45, 30, 60, 55],  # Usuario 2
    [60, 20, 30, 40, 35, 50, 45]   # Usuario 3
]

# Función para calcular el promedio por usuario
def promedio_por_usuario(usuarios_tiempos):
    for i, tiempos in enumerate(usuarios_tiempos, start=1):
        promedio_minutos = promedio_actividad_fisica(tiempos)
        promedio_horas = minutos_a_horas(promedio_minutos)
        print(f"✉️ El tiempo promedio diario de actividad física para el Usuario {{i}} es de {{promedio_minutos:.2f}} minutos ({{promedio_horas:.2f}} horas por día).")

# Llamar a la función con la lista de usuarios
promedio_por_usuario(usuarios_actividad)
