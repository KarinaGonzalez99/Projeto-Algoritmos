def is_palindrome_recursive(word, low_index, high_index):
    # Verifica se a string é vazia
    if len(word) == 0:
        return False

    # Verifica se os índices se cruzaram (caso base)
    if low_index > high_index:
        return True

    # Verifica se os caracteres nos índices baixo e alto são diferentes
    if word[low_index] != word[high_index]:
        return False

    # Chamada recursiva da função com os índices atualizados
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    raise NotImplementedError
