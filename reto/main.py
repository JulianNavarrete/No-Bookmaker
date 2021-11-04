import time

with open('lista_chica.txt', 'r', encoding='utf-8') as small_file:
    lista_chica = small_file.readlines()

with open('lista_grande.txt', 'r', encoding='utf-8') as big_file:
    lista_grande = big_file.readlines()

with open('lista_nueva.txt', 'w', encoding='utf-8') as new_file:
    start = time.time()
    for linea in lista_chica:
        if not linea in lista_grande:
            new_file.write(linea)

final = time.time() - start
print(final)
