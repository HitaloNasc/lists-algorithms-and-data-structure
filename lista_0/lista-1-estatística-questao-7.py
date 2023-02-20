import statistics

idades = [29, 27, 25, 39, 29, 27, 41, 31, 25, 33, 27, 25, 25, 23, 27, 27, 32, 26, 24, 36, 32, 26, 28, 24,
          28, 27, 24, 26, 30, 26, 35, 26, 28, 34, 29, 23, 28]

idades.sort()

print(idades)


# Média

print(f'Soma {sum(idades)}')
print(f'Tamanho {len(idades)}')
print(f'Média {sum(idades) / len(idades)}')


# Mod

print(f'Moda {statistics.mode(idades)}')

# Mediana

print(f'Mediana {statistics.median(idades)}')
