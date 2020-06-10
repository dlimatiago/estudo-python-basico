def notas(*grade, sit=False):
    """
    > Função que recebe uma ou mais notas.
    :param grade: Notas que foram passadas como parâmetro.
    :param sit: Parâmetro opcional para mostrar a situação do aluno/turma
    :return: Retorna um dicionário com as seguintes informações:
                - Total de notas
                - Maior nota
                - Menor nota
                - Média
                - Situação(Se requisitada): Bom, Mediano ou Ruim
    """
    from statistics import mean as md

    info = dict()
    info['Total'] = len(grade)
    info['Maior nota'] = round(max(grade), 1)
    info['Menor nota'] = round(min(grade), 1)
    info['Média'] = round(md(grade), 1)

    if sit is True:
        info['Situação'] = 'Bom' if info['Média'] >= 7 else 'Mediano' if info['Média'] >= 5 else 'Ruim'
    return info


# Main Code
dados = notas(5.6, 6.3, 5.89, 1.53, 4.9, sit=True)
print(dados)