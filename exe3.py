print("Manipulação de Listas")
print("Criando e manipulando uma lista de números.")

# Inicializa uma lista vazia
lista_numeros = []

# Adiciona números à lista
lista_numeros.append(10)
lista_numeros.append(20)
lista_numeros.append(30)

# Imprime a lista atual
print("Lista inicial:", lista_numeros)

# Remove um elemento da lista
elemento_removido = lista_numeros.pop(1)
print(f"Elemento removido: {elemento_removido}")
print("Lista após remoção:", lista_numeros)

# Adiciona mais números à lista
lista_numeros.append(40)
lista_numeros.append(50)

# Imprime a lista atualizada
print("Lista atualizada:", lista_numeros)
