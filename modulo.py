def separa_idosos(pessoas,idade_para_ser_idoso):
    pessoas_separadas = {
        'maiores_60':[],'menores_60':[]
    }
    for nome, idade in zip(pessoas['nome'],pessoas['idade']):
        if idade>=idade_para_ser_idoso:
            pessoas_separadas['maiores_60'].append([nome,idade])
        else:
            pessoas_separadas['menores_60'].append([nome,idade])
        
    return pessoas_separadas


def fila_prioridade_por_idosos(pessoas, condição_de_ordenação_fila):
    fila_prioridade=[]
    quantidade_de_pessoas = len(pessoas['maiores_60'])+len(pessoas['menores_60'])
    #a cada x idosos, um nao idoso é atendido.
    contador=0
    for people_cont in range (0,quantidade_de_pessoas):
        
        if len(pessoas['maiores_60'])==0 or contador ==condição_de_ordenação_fila:
                contador=0
                fila_prioridade.append(pessoas['menores_60'][0])
                pessoas['menores_60'].pop(0)

        
        else:
            if pessoas['maiores_60']!=[]:
                fila_prioridade.append(pessoas['maiores_60'][0])
                pessoas['maiores_60'].pop(0)
        contador+=1
        
    print(fila_prioridade)