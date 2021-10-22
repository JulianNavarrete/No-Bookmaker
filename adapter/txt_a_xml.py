from os import close


class XmlFormatter():
    def __init__(self, arch1, arch2):
        self.arch1 = arch1
        self.arch2 = arch2

    def format(self):
        source = open (self.arch1,'r', encoding='utf8')
        destino = open (self.arch2,'w', encoding='utf8')
        destino.writelines('<?xml version="1.0" encoding="UTF-8"?>')
        destino.writelines('\n<listado>')
        for line in source:
           j = line.split('; ')
           destino.writelines('\n\t<usuario>')
           line_xml =f"\n\t\t<nombre>{j[0]}</nombre>"
           destino.writelines(line_xml)
           line_xml ="\n\t\t<apellido>"+j[1].strip(' \n')+"</apellido>"
           destino.write(line_xml)
           destino.writelines('\n\t</usuario>')
           print(line_xml)
        destino.writelines('\n</listado>')
        destino.writelines('\n</xml>')
        destino.close()
        source.close()


if __name__== '__main__':
    x = XmlFormatter('archivo.txt', 'archivo.xml')
    x.format()
