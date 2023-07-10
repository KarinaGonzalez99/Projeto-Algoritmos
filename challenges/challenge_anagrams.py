# Esta função implementa o algoritmo de ordenação 'merge sort'
def merge_sort(numbers):
    # Se a lista de números tiver tamanho 0 ou 1, ela já está ordenada
    if len(numbers) <= 1:
        return numbers

    # Encontra o meio da lista
    mid = len(numbers) // 2

    # Divide a lista em duas metades e ordena cada uma delas recursivamente
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    # Lista para armazenar os números ordenados
    merged = []
    left_index = right_index = 0

    # Enquanto houver elementos em ambas as listas
    while left_index < len(left) and right_index < len(right):
        # Se o elemento da esquerda for menor, adiciona ele na lista ordenada
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        # Senão, adiciona o elemento da direita na lista ordenada
        else:
            merged.append(right[right_index])
            right_index += 1

    # Adiciona os elementos restantes da lista da esquerda, se houver
    merged.extend(left[left_index:])
    # Adiciona os elementos restantes da lista da direita, se houver
    merged.extend(right[right_index:])

    # Retorna a lista de números ordenados
    return merged


# Esta função verifica se duas strings são anagramas
def is_anagram(first_string, second_string):
    # Se ambas as strings forem vazias, elas não são consideradas anagramas
    if first_string == "" and second_string == "":
        return "", "", False

    # Ordena as strings usando a função de ordenação definida anteriormente
    sorted_first = "".join(merge_sort(list(first_string.lower())))
    sorted_second = "".join(merge_sort(list(second_string.lower())))

    # Retorna as strings ordenadas e se são anagramas ou não
    return sorted_first, sorted_second, sorted_first == sorted_second
