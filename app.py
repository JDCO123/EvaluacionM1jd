notas_estudiantes = {
    'Juan': [3.2, 4.5, 5],
    'Maria': [4.2, 3.5, 4.3],
    'Pedro': [3.9, 2.5, 4.8]
}

def calcular_prom(notas):
    return sum(notas) / len(notas)

for est, notas in notas_estudiantes.items():
    prom = calcular_prom(notas)
    print(f"El promedio de {est} es: {prom} ")
    