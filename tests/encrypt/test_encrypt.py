import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Verifica se ocorre a exceção correta para tipo inválido de key
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("a", "b")

# Verifica se ocorre a exceção correta para tipo inválido de message
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 2)

# Verifica se aretorna o resultado esperado para casos de teste
    assert encrypt_message("jojo", 3) == "joj_o"
    assert encrypt_message("jojo", 21) == "ojoj"
    assert encrypt_message("jojo", 4) == "ojoj"

    pass
