from modulo import Pessoa

            
          
pessoas_cadastradas = {
 'nome':[],'idade':[]
}

while True:
    name = str(input('Digite o nome:')).strip()
    age  = int(input('Agora a idade:'))
    opcao = str(input('Quer continuar?S/N')).strip().upper()
    pessoas_cadastradas['nome'].append(name)
    pessoas_cadastradas['idade'].append(age)
    if opcao == 'N':
        break

pessoas=Pessoa(pessoas_cadastradas)

pessoas_separadas = pessoas.separa_idosos(60)

fila_ordenada= pessoas.fila_prioridade_por_idosos(pessoas_separadas,2)

pessoas.mostra_tabela_idosos_e_nao_idosos(pessoas_separadas)

print(f'A fila de prioridade é {fila_ordenada}')











