class ArchivoSQL:
    def convertir_archivo(self, source, destiny):
        origen = open(source, 'r', encoding='utf-8')
        destino = open(destiny, 'w', encoding='utf-8')
        for linea in origen:
            lineas = linea.strip().split(";")
            linea_sql = f"INSERT INTO usuarios(nombre, apellido) VALUES ('{lineas[0]}', '{lineas[1]}');\n"
            destino.writelines(linea_sql)
            print(linea_sql)
        destino.close()
        origen.close()
