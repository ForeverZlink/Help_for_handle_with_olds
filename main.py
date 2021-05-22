from modulo import separa_idosos, fila_prioridade_por_idosos


pessoas_cadastradas = {
    'nome':[],'idade':[]
    }


while True:
    name = str(input('Digite o nome:')).strip()
    age  = int(input('Agora a idade:'))
    opcao = str(input('Quer continuar?s ou n')).strip().upper()
    pessoas_cadastradas['nome'].append(name)
    pessoas_cadastradas['idade'].append(age)
    if opcao == 'N':
        break


pessoas_separadas = separa_idosos(pessoas_cadastradas,60)

fila_ordenada= fila_prioridade_por_idosos(pessoas_separadas,2)




print(fila_ordenada)









