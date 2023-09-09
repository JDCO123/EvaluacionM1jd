notas_estudiantes = {
    'Juan': [3.2, 4.5, 5],
    'Maria': [4.2, 3.5, 4.3],
    'Pedro': [3.9, 2.5, 4.8]
}

def calcular_promedios(notas):
    return sum(notas) / len(notas)

for estudiantes, notas in notas_estudiantes.items():
    promedio = calcular_promedios(notas)
    print(f"El promedio de {estudiantes} es: {promedio} ")
    