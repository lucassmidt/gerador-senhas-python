import random

def gerar_senha(tamanho, incluir_simbolos=True):
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "!@#$%&*"

    caracteres = letras + numeros
    if incluir_simbolos:
        caracteres += simbolos

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Entrada do usuário
tamanho = int(input("Digite o tamanho da senha: "))
usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

senha = gerar_senha(tamanho, incluir_simbolos=usar_simbolos)
print("Senha gerada:", senha)
