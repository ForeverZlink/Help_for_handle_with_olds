def separa_idosos(pessoas,idade_para_ser_idoso):
    pessoas_separadas = {
        'maiores_60':[],'menores_60':[]
    }
    for nome, idade in zip(pessoas_cadastradas['nome'],pessoas_cadastradas['idade']):
        if idade>=idade_para_ser_idoso:
            pessoas_separadas['maiores_60'].append([nome,idade])
        else:
            pessoas_separadas['menores_60'].append([nome,idade])
        
    return pessoas_separadas

def fila_prioridade_por_idosos(pessoas, condição_de_ordenação_fila):
    fila_prioridade=[]
    #a cada x idosos, um nao idoso é atendido

