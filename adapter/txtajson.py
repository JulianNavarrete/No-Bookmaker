from os import close


class TxtToJson:

    @staticmethod
    def converter(source, destino):
        source = open (f'{source}','r', encoding='utf8')
        destino = open (f'{destino}','w', encoding='utf8')
        lista_json = []
        destino.write("[")
        for line in source:
            j = line.split(';')

            line_json = '{"' + 'nombre' + '"'+ ':"' + j[0] + '",' + '"' + 'apellido' + '"'+ ':"' + j[1].strip(" \n") + '"},'
            lista_json.append(line_json)

        lista_json[-1] = lista_json[-1][0:-1]
        destino.writelines(lista_json)
        destino.write(']')
        destino.close()
        source.close()

if __name__== '__main__':
    TxtToJson.converter('archivo.txt', 'archivo.json')