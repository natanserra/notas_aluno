def notas(*notas, situacao=False):
    """Recebe várias notas e retorna um dicionário com informações sobre elas."""
    
    if not notas:
        return {'Mensagem': 'Nenhuma nota fornecida.'}

    # Verifica se todas as notas são numéricas
    if not all(isinstance(nota, (int, float)) for nota in notas):
        return {'Erro': 'Todas as notas devem ser numéricas.'}

    # Calcula as informações
    total_notas = len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / total_notas

    resultado = {
        'Quantidade de Notas': total_notas,
        'Maior Nota': maior_nota,
        'Menor Nota': menor_nota,
        'Média da Turma': media
    }
    
    # Adiciona a situação, se solicitado
    if situacao:
        if media >= 7:
            resultado['Situação'] = 'Aprovado'
        elif media >= 5:
            resultado['Situação'] = 'Recuperação'
        else:
            resultado['Situação'] = 'Reprovado'
    
    return resultado

def main():
    """Função principal para demonstrar a função notas()."""
    print("Cadastro de Notas de Alunos")

    # Solicita ao usuário as notas
    notas_usuario = input("Digite as notas separadas por espaço: ")
    
    # Converte a string de notas em uma lista de números
    notas_lista = [float(nota) for nota in notas_usuario.split()]

    # Exemplo de uso da função notas
    resultado = notas(*notas_lista, situacao=True)
    
    # Exibe o resultado
    print("\nInformações das Notas:")
    for chave, valor in resultado.items():
        print(f"{chave}: {valor}")

if __name__ == "__main__":
    main()
