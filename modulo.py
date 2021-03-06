class InterfacePrograma():
    
    


    def leia_opcao(text):
        while True:
            print('-='*34)
            print('Suas opções:')
            print('0-Encerrar Programa')
            print('1-Continuar')
            print('2-Criar_json')
            opcao = str(input(text)).strip().upper()
            if opcao =='1' or opcao =='0' or opcao == "2":
                return opcao
                
            else:
                print('Opção ERRADA! DIGITE APENAS 1 OU 0 ')

    @staticmethod
    def menu():
        pessoas_cadastradas = {
             'nome':[],'idade':[]
            }

        while True:
            name = str(input('Digite o nome:')).strip()
            age  = int(input('Agora a idade:'))
            opcao =InterfacePrograma.leia_opcao('Sua escolha é:')
            
            pessoas_cadastradas['nome'].append(name)
            pessoas_cadastradas['idade'].append(age)
            if opcao == '0' or opcao =='2':
                
                return pessoas_cadastradas,opcao
    



class Pessoa():

    def __init__(self,pessoas_cadastradas:dict):
        self.pessoas=pessoas_cadastradas
    

        
    
    def separa_idosos(function)->dict:
        def with_parameters(self,condição_de_ordenação_fila,idade_para_ser_idoso):
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
            self.pessoas_separadas = pessoas_separadas.copy()
            fila_ordenada=function(self.pessoas_separadas,condição_de_ordenação_fila)
            return fila_ordenada
        return with_parameters
        
    @separa_idosos
    def fila_prioridade_por_idosos(pessoas_separadas,condição_de_ordenação_fila)->list:
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
        fila = fila_prioridade[:]
        return fila

    def mostra_tabela_idosos_e_nao_idosos(self,pessoas_separadas=dict):
        """
        Mostra uma tabela com idosos e nao idosos.
        Só será mostrado as lista que possuir valores
        
        """
        #varre  o dicionario 
        for nome_categoria, value in self.pessoas_separadas.items():
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

    def cria_um_txt_com_as_pessoas_separadas(self):
        with open('pessoas.txt','a+') as arquivo:
            for value in self.pessoas_separadas.values():
                for pessoa in value:
                    arquivo.write(f'{pessoa[0]:<49}{pessoa[1]:}\n')

    def cria_um_json(self,modo):
        '''
        Parametro modo: é como o arquivo vai ser aberto. Usar os parametros da função open do python
        '''
        from json import dumps
        #cria um json
        pessoas_separadas_json= dumps(self.pessoas_separadas)

        #se o modo for x, só vai criar um arquivo se ele não existir
        #se o modo for w, ele sempre vai criar um novo arquivo que vai substituir o antigo
        with open('./arquivos_pessoas/pessoas.json',modo) as archiver:
            #vai para o inicio do arquivo
            archiver.seek(0,0)
            archiver.write(pessoas_separadas_json)