import statistics

# Dados
numbers = [4, 5, 3, 4, 2, 6, 4, 1, 6, 5, 3, 4, 4, 5,
           2, 3, 6, 5, 4, 2, 2, 3, 4, 3, 3, 2, 1, 1, 5, 2]

numbers.sort()

print(f'A: {numbers}')


# Média
print(sum(numbers))
print(len(numbers))
print(sum(numbers)/len(numbers))
print(f'Média {statistics.mean(numbers):.2f}')

# Moda
print(f'Moda {statistics.mode(numbers)}')

# Mediana
print(f'Mediana {statistics.median(numbers)}')

# Variância
print(f'Variância {statistics.variance(numbers):.2f}')

# Desvio padrão
print(f'Desvio padrão {statistics.stdev(numbers):.2f}')
