import time

with open('lista_chica.txt', 'r', encoding='utf-8') as small_file:
    lista_chica = small_file.readlines()

with open('lista_grande.txt', 'r', encoding='utf-8') as big_file:
    lista_grande = big_file.readlines()

start = time.time()

with open('lista_nueva.txt', 'w', encoding='utf-8') as new_file:
    lista_nueva = set(lista_grande).difference(set(lista_chica))
    new_file.write(str(lista_nueva))

final = time.time() - start
print(final)
