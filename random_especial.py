from clase_diseño import Alumno


if __name__=='__main__':
    alumnos = []

    alumnos.append(Alumno('Julian', 'Navarrete', 3))
    alumnos.append(Alumno('Delfina', 'Quinteros', 3))
    alumnos.append(Alumno('Gastón', 'Fenske', 2))
    alumnos.append(Alumno('Enzo', 'Fernandez', 1))
    alumnos.append(Alumno('Gabriel', 'Almonacid', 3))
    alumnos.append(Alumno('Douglas', 'Arenas', 1))
    alumnos.append(Alumno('Lucas', 'Galdame', 1))
    alumnos.append(Alumno('Santiago', 'Moyano', 1))
    alumnos.append(Alumno('José', 'Ruti', 2))
    alumnos.append(Alumno('Bruno', 'Romero', 1))
    alumnos.append(Alumno('Danilo', 'Cerna', 2))
    alumnos.append(Alumno('Daniel', 'Beato', 3))
    alumnos.append(Alumno('Lucas', 'Ollarce', 4))
   
    for a in sorted(alumnos):
        print(a)

    """alumnos.sort(key=lambda x: x.puntaje)
    for a in alumnos:
        print(a)
    """
