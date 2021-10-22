from txt_to_sql import ArchivoSQL

if __name__ == '__main__':
    try:
        source = input("Ingrese el nombre del archivo de origen(txt):")
        destiny = input("Ingrese el nombre del archivo de destino(sql):")
        file_sql = ArchivoSQL().convertir_archivo(source, destiny)
    except:
        print("Ingrese el nombre del archivo .txt y .sql")
