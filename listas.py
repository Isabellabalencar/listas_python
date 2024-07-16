# Criação de uma lista
frutas = ['maçã', 'banana', 'laranja']

# Adicionando um item ao final da lista
frutas.append('uva')

# Estendendo a lista com outro iterável
frutas.extend(['abacaxi', 'melancia'])

# Inserindo um item em uma posição específica
frutas.insert(1, 'morango')

# Removendo um item
frutas.remove('banana')

# Removendo e retornando o último item
ultima_fruta = frutas.pop()

# Limpando a lista
frutas.clear()

# Obtendo o índice de um item
indice = frutas.index('laranja')

# Contando a ocorrência de um item
contagem = frutas.count('maçã')

# Ordenando a lista
frutas.sort()

# Invertendo a lista
frutas.reverse()

# Fazendo uma cópia da lista
frutas_copia = frutas.copy()

print(frutas)
print(frutas_copia)
