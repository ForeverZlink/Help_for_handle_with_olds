from modulo import Pessoa,InterfacePrograma
     
          
pessoas_cadastradas=InterfacePrograma.menu()
        
pessoas=Pessoa(pessoas_cadastradas)

fila_ordenada = pessoas.fila_prioridade_por_idosos(2,60)

pessoas.mostra_tabela_idosos_e_nao_idosos()
pessoas.cria_um_txt_com_as_pessoas_separadas()
print(f'A fila de prioridade é {fila_ordenada}')











