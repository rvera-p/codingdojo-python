import csv

archivo = "alumnos.csv"
with open(archivo) as f:
    leer_archivo = csv.DictReader(f)

    mejore_alumnos = []
    mejor_nota = 0
    count = 0
    for alumno in leer_archivo:
        nombre = alumno["nombre"]
        nota1 = float(alumno ["nota1"])
        nota2 = float(alumno ["nota2"])
        nota3 = float(alumno ["nota3"])
        asistencia = float(alumno["asistencia"])

        #3 Calculando el promedio
        nota_promedio = (nota1 + nota2 + nota3) / 3.0

        #4 Comparar si el alumno cumple con las condiciones (mayor nota y asistencia > 80)
        if nota_promedio > mejor_nota and asistencia > 80:
            mejores_alumnos = [[nombre, nota_promedio, asistencia]]
            mejor_nota = nota_promedio
        elif nota_promedio == mejor_nota and asistencia > 80:
            mejores_alumnos.insert(count, [nombre, nota_promedio, asistencia])
            count += 1
print("Los mejores alumnos son: ")
for alumno in mejores_alumnos:
    #srt_format = f'Nombre: {mejores_alumnos[alumno]}
    print(alumno)

        
