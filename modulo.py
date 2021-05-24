class Pessoa():

    def __init__(self,pessoas_cadastradas:dict):
        self.pessoas=pessoas_cadastradas

    def separa_idosos(self,idade_para_ser_idoso:int)->dict:
        """
        Separa os idosos em uma lista que está dentro de um dicionário.
        Parametro idade_para_ser_idoso : é com quantos anos alguém é idoso.
        
        """
        pessoas_separadas = {
            'maiores_60':[],'menores_60':[]
        }

        #varre o dicionario
        for nome, idade in zip(self.pessoas['nome'],self.pessoas['idade']):
            
            if idade>=idade_para_ser_idoso:
                pessoas_separadas['maiores_60'].append([nome,idade])
            else:
                pessoas_separadas['menores_60'].append([nome,idade])

         
        return pessoas_separadas


    def fila_prioridade_por_idosos(self,pessoas_separadas, condição_de_ordenação_fila:int)->list:
        """
        gera uma fila de prioridade a partir da idade 
        Parametro pessoas: é as pessoas que serão ordenadas em fila
        Parametro condição_de_ordenação_fila: é o critério para separar a fila. EXemplo: A cada dois idosos, um nao idoso é atendido.
                                            Esse parametro é que decide a quantidade de idosos 

        """
        
        #recebe uma copia dos valores das listas  que estao dentro do dicionario pessoas
        #pois se isso nao for feito, uma ligação entre lista é criada no programa principal e o 
        #a variavel do programa principal fica ligada as listas dessas função
        pessoas_separadas = {
            'maiores_60':pessoas_separadas['maiores_60'].copy(),
            'menores_60':pessoas_separadas['menores_60'].copy()
            }

        fila_prioridade=[]
        quantidade_de_pessoas = len(pessoas_separadas['maiores_60'])+len(pessoas_separadas['menores_60'])
        
        #a cada x idosos, um nao idoso é atendido.
        contador=0

        #Esse loop vai acontecer o mesmo numero de vezes que 
        #existas pessoas, assim nao terei problems of index
        for people_cont in range (0,quantidade_de_pessoas):

            quantidade_de_maiores_60=len(pessoas_separadas['maiores_60'])

            # se nao ha maiores de 60, entao eu posso adicionar.
            if quantidade_de_maiores_60 ==0 or contador ==condição_de_ordenação_fila:
                    contador=0
                    fila_prioridade.append(pessoas_separadas['menores_60'][0])
                    #apaga o primero valor
                    pessoas_separadas['menores_60'].pop(0)

            
            else:
                #se a lista estiver vazia 
                
                fila_prioridade.append(pessoas_separadas['maiores_60'][0])
                #apago o primeiro valor da lista
                pessoas_separadas['maiores_60'].pop(0)
            contador+=1

        return fila_prioridade
        

    def mostra_tabela_idosos_e_nao_idosos(self,pessoas):
        """
        Mostra uma tabela com idosos e nao idosos.
        Só será mostrado as lista que possuir valores
        
        """
        #varre  o dicionario 
        for nome_categoria, value in pessoas.items():
            ##caso a lista esteja vazia, o programa vai para a próxima iteração
            if value == []:
                continue
            print('-+'*50)
            print(f'{nome_categoria:^30}'.upper())
            print(f'{"Nome":<40} {"idade"}')


            ##varre a lista 
            for pessoa in value:
                print(f'{pessoa[0]:<42}{pessoa[1]}')
            print('-+'*50)
