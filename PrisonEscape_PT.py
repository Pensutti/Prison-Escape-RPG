import time
import os

score = 0

def prison_escape():
    def credits():
        os.system('clear') or None
        print("Jogo desenvolvido por alunos da Universidade Presbiteriana Mackenzie. \n")
        time.sleep(3)
        print("Francis Kenji Teruya          TIA: 41912055")
        time.sleep(1)        
        print("Guilherme Heitor Pensutti     TIA: 41921704")
        time.sleep(1)
        print("João Vitor Duarte Queiroz     TIA: 41930096") 
        time.sleep(3)
        os.system('clear') or None
        prison_escape()

    def game_en():
        os.system('clear') or None
        print("VERSÃO INGLÊS EM DESENVOLVIMENTO | ENGLISH VERSION UNDER DEVELOPMENT")
        time.sleep(4)
        os.system('clear') or None
        prison_escape()


    def game_pt():
        game = 0
        score = 0

        #-------------------------------------------- Minigame Basquete ---------------------------------------------
        def minigame_basket():
            minigame = 0
            points = 0

            #Explicação do minigame
            print('''
            Calcule com precisão as forças e alturas de arremesso necessárias para pontuar.
            Você poderá usar apenas números inteiros.
            1 cesta = 1 ponto
            Você precisa de 3 pontos para vencer!
            ''')
            time.sleep(10)

            #1º Rodada --> tentativa 9 ~ 14
            while minigame == 0:
                print('''
                    1˚ Rodada:
                    Estilo de arremesso: frontal
                    Distância: 2 metros
                    ''')

                power = int(input('Digite a força de arremesso desejada entre 0 e 5:\n'))
                altura = int(input('Digite a altura de arremesso desejada entre 0 e 5:\n'))
                tent = altura * power

                if tent < 3:               
                    print('''
                        Clin: 
                        - Hahahaha! Você está realmente tentando?!
                        ''')
                    time.sleep(3)
                    os.system('clear') or None

                elif tent >= 3 and tent < 9:        
                    print('''
                        Clin: 
                        - Essa foi perto...
                        ''')
                    time.sleep(3)
                    os.system('clear') or None

                elif tent >= 9 and tent <= 14:      
                    print('''
                        Clin: 
                        Droga, 1 cesta...
                        ''')
                    time.sleep(3)
                    points = points + 1
                    print("Pontuação: ", points, "ponto.")
                    time.sleep(3)
                    os.system('clear') or None
                    break

                elif tent > 14 and tent <= 19:       
                    print('''
                        Clin: 
                        - Essa foi perto...
                        ''')
                    time.sleep(3)
                    os.system('clear') or None

                elif tent > 19 and tent <= 25 :      
                    print('''
                        Clin: 
                        - Hahahaha! Você está realmente tentando?!
                        ''')
                    time.sleep(3)
                    os.system('clear') or None

                else: 
                    print("Algum valor foi inserido errado... Tente novamente.")
                    time.sleep(3)
                    os.system('clear') or None
                

                #2º Rodada --> tentativa 14 ~ 18
            while minigame == 0:
                print('''
                    2˚ Rodada:
                    Estilo de arremesso: lateral
                    Distância: 5 metros
                    ''')

                power = int(input('Digite a força de arremesso desejada entre 0 e 5:\n'))
                altura = int(input('Digite a altura de arremesso desejada entre 0 e 5:\n'))
                tent = altura * power

                if tent < 9:               
                    print('''
                        Clin: 
                        - Hahahaha! Você está realmente tentando?!
                        ''')
                    time.sleep(3)
                    os.system('clear') or None

                elif tent >= 9 and tent < 14:        
                    print('''
                        Clin: 
                        - Essa foi perto...
                        ''')
                    time.sleep(3)
                    os.system('clear') or None

                elif tent >= 14 and tent <= 18:      
                    print('''
                        Clin: 
                        Ah não, mais uma cesta...
                        ''')
                    time.sleep(3)
                    points = points + 1
                    print("Pontuação: ", points, "pontos.")
                    time.sleep(3)
                    os.system('clear') or None
                    break

                elif tent > 18 and tent <= 22 :       
                    print('''
                        Clin: 
                        - Essa foi perto...
                        ''')
                    time.sleep(3)
                    os.system('clear') or None

                elif tent > 22 and tent <= 25 :      
                    print('''
                        Clin: 
                        - Hahahaha! Você está realmente tentando?!
                        ''')
                    time.sleep(3)
                    os.system('clear') or None

                else: 
                    print("Algum valor foi inserido errado... Tente novamente.")
                    time.sleep(3)
                    os.system('clear') or None



            #3º Rodada --> tentativa = 18
            while minigame == 0:
                print('''
                    3˚ Rodada:
                    Estilo de arremesso: diagonal
                    Distância: 7 metros
                    ''')

                power = int(input('Digite a força de arremesso desejada entre 0 e 6:\n'))
                altura = int(input('Digite a altura de arremesso desejada entre 0 e 6:\n'))
                tent = altura * power

                if tent < 8:               
                    print('''
                        Clin: 
                        - Hahahaha! Você está realmente tentando?!
                        ''')
                    time.sleep(3)
                    os.system('clear') or None

                elif tent >= 8 and tent < 18:        
                    print('''
                        Clin: 
                        - Essa foi perto...
                        ''')
                    time.sleep(3)
                    os.system('clear') or None

                elif tent == 18:      
                    print('''
                        Clin: 
                        Cesta...
                        ''')
                    time.sleep(3)
                    points = points + 1
                    print("Pontuação: ", points, "pontos.")
                    time.sleep(2)
                    print("Você conseguiu completar o desafio.")
                    time.sleep(3)
                    os.system('clear') or None
                    break

                elif tent > 18 and tent <= 28:       
                    print('''
                        Clin: 
                        - Essa foi perto...
                        ''')
                    time.sleep(3)
                    os.system('clear') or None

                elif tent > 28 and tent <= 36 :      
                    print('''
                        Clin: 
                        - Hahahaha! Você está realmente tentando?!
                        ''')
                    time.sleep(3)
                    os.system('clear') or None

                else: 
                    print("Algum valor foi inserido errado... Tente novamente.")
                    time.sleep(3)
                    os.system('clear') or None

        #-------------------------------------------- Minigame Receita ----------------------------------------------
        def minigame_kitchen():
            minigame = 0 
            minigame_kitchen = 0


            #RESPOSTAS: 42135  5213674  24351

            #Explicação do Minigame
            print('''\n
                Você conseguiu se passar por cozinheiro. Agora deve acertar a preparação de 3 pratos em 
                sequência para conseguir acessar o depósito. Caso erre você será descoberto.
                ''')
            
            time.sleep(4)
            print('''
                Regra:
                - Será disponibilizado os modos de preparo e você deverá acertar a ordem.
                ''')
            time.sleep(3)

            #Primeira Receita:
            while minigame == 0:
                print('''
                    ------- Ovos Mexidos -------
                    Colocaremos o sal no final da receita.

                    Ingredientes:
                    - Ovo
                    - Óleo
                    - Sal

                    Modo de Preparo:

                    - Quebrar ovo (1)
                    - Colocar Óleo (2)
                    - Fritar (3)
                    - Pegar Frigideira (4)
                    - Colocar sal (5)
                ''')
                time.sleep(1)
                answer_mgkitchen_1_1 = int(input('Qual é o primeiro passo?\n'))
                answer_mgkitchen_1_2 = int(input('Qual é o segundo passo?\n'))
                answer_mgkitchen_1_3 = int(input('Qual é o terceiro passo?\n'))
                answer_mgkitchen_1_4 = int(input('Qual é o quarto passo?\n'))
                answer_mgkitchen_1_5 = int(input('Qual é o quinto passo?\n'))
                time.sleep(2)
                if (answer_mgkitchen_1_1 == 4 and answer_mgkitchen_1_2 == 2 and answer_mgkitchen_1_3 == 1 and answer_mgkitchen_1_4 == 3 and answer_mgkitchen_1_5 == 5):
                    print('\nFaça a próxima.\n')
                    time.sleep(2)
                    minigame_kitchen += 1 
                    os.system('clear') or None
                else: 
                    print('\nFaça a próxima.\n')
                    time.sleep(1)

            #Segunda Receita
                print('''
                    ------- Gelatina ------- 
                    Ingredientes:
                    - Água
                    - Gelatina

                    Modo de Preparo:
                    - Pegar o recipiente (1)
                    - Ferver metade da água (2)
                    - Colocar a água quente no recipiente (3)
                    - Colocar na geladeira (4)
                    - Pegar a panela (5)
                    - Misturar a gelatina (6)
                    - Colocar a água fria no recipiente (7)
                ''')
                time.sleep(1)
                answer_mgkitchen_2_1 = int(input('Qual é o primeiro passo?\n'))
                answer_mgkitchen_2_2  = int(input('Qual é o segundo passo?\n'))
                answer_mgkitchen_2_3 = int(input('Qual é o terceiro passo?\n'))
                answer_mgkitchen_2_4 = int(input('Qual é o quarto passo?\n'))
                answer_mgkitchen_2_5 = int(input('Qual é o quinto passo?\n'))
                answer_mgkitchen_2_6 = int(input('Qual é o sexto passo?\n'))
                answer_mgkitchen_2_7 = int(input('Qual é o sétimo passo?\n'))
                time.sleep(1)
                if (answer_mgkitchen_2_1 == 5 and answer_mgkitchen_2_2 == 2 and answer_mgkitchen_2_3 == 1 and answer_mgkitchen_2_4 == 3 and answer_mgkitchen_2_5 == 6 and answer_mgkitchen_2_6 == 7 and answer_mgkitchen_2_7 == 4):
                    print('\nFaça a próxima.\n')
                    minigame_kitchen += 1
                    time.sleep(3)
                    os.system('clear') or None
                else: 
                    print('\nFaça a próxima.\n')
                    time.sleep(3)
                    os.system('clear') or None

            #Terceira Receita
                print('''
                    ------- Purê de batatas -------
                    Ingredientes:
                    - Batatas
                    - Água
                    - Sal
                
                    Modo de Preparo:
                    - Amassar as batatas (1)
                    - Pegar Panela (2)
                    - Colocar sal (3)
                    - Ferver a água (4)
                    - Cozinhar as batatas (5)
                ''')
                time.sleep(1)
                answer_mgkitchen_3_1 = int(input('Qual é o primeiro passo?\n'))
                answer_mgkitchen_3_2 = int(input('Qual é o segundo passo?\n'))
                answer_mgkitchen_3_3 = int(input('Qual é o terceiro passo?\n'))
                answer_mgkitchen_3_4 = int(input('Qual é o quarto passo?\n'))
                answer_mgkitchen_3_5 = int(input('Qual é o quinto passo?\n'))
                time.sleep(1)
                if (answer_mgkitchen_3_1 == 2 and answer_mgkitchen_3_2 == 4 and answer_mgkitchen_3_3 == 3  and answer_mgkitchen_3_4 == 5 and answer_mgkitchen_3_5 == 1):
                    print('\n------- Verificando se acertou todas as receitas... -------\n')
                    time.sleep(3)
                    minigame_kitchen += 1
                else: 
                    print('\n------- Verificando se acertou todas as receitas... -------\n')
                    time.sleep(4)

                if(minigame_kitchen == 0):
                    print('Você não acertou nenhuma receita. Tente novamente!\n')
                    time.sleep(3)
                    os.system('clear') or None

                elif(minigame_kitchen == 1):
                    print('Você acertou apenas uma receita. Tente novamente!\n')
                    time.sleep(3)
                    os.system('clear') or None

                elif(minigame_kitchen == 2):
                    print('Você acertou apenas duas receita. Tente novamente!\n')
                    time.sleep(3)
                    os.system('clear') or None

                else:
                    print('BOA! Você mostrou que é um bom cozinheiro e conseguiu o acesso ao depósito.\n')
                    time.sleep(3)
                    os.system('clear') or None
                    break

    #------------------------------------------------ INTRODUÇÃO ------------------------------------------------
        print("Você foi acusado injustamente por um assassinato e terá que cumprir pena perpétua.")
        time.sleep(3.51)
        print("Sua única salvação acaba sendo algumas filmagens captadas por uma câmera de segurança no local do crime.")
        time.sleep(3.5)
        print("Porém você fica sabendo por terceiros que essas provas serão corroídas pelos reais culpados em poucos dias.")
        time.sleep(3.5)
        print("Seu dever agora é fugir da prisão para conseguir apresentar esses dados a justiça.")
        time.sleep(5)
        os.system('clear') or None
    #------------------------------------------------ Parte 1 ---------------------------------------------------
        while game == 0:
            print('''
                Para começar sua fuga, você precisa primeiro sair de sua cela.
                Na prisão, você possui um amigo que pode lhe fornecer somente uma ferramenta.
                Escolha a melhor para te tirar da cela:
            ''')

            print('''
                ------------------------------
                1. Maçarico      
                2. Picareta
                3. TNT
                4. Vodka
                5. Alicate
                ------------------------------
            ''')

            #Pedir opção
            option_pt1_1 = int(input("Digite a opção desejada: "))

        #Definir resultados das escolhas de ferramentas. (ERRADAS)
            if option_pt1_1 == 1:
                os.system('clear') or None
                print("Ligando maçarico...")
                time.sleep(3)
                print('''
                BOOOOOOM!            
                Ops, o maçarico que pegou possuia um defeito e explodiu em sua mão... :(
                GAME OVER!\n''')
                time.sleep(5)
                score = score - 2
                os.system('clear') or None
                
            elif option_pt1_1 == 2:
                os.system('clear') or None
                print("Cavando...")
                time.sleep(3)
                print('''
                PLOFT!
                Você não planejava um poço sem fim embaixo de sua cela…
                GAME OVER!\n''')
                time.sleep(5)
                score = score - 2
                os.system('clear') or None
                
            elif option_pt1_1 == 3:
                os.system('clear') or None
                print("Plantando TNT...")
                time.sleep(3)
                print('''
                BOOOOOOM!
                Parece que a explosão era mais forte do que planejava…
                GAME OVER!\n''')
                time.sleep(5)
                score = score - 2
                os.system('clear') or None

            elif option_pt1_1 == 5:
                os.system('clear') or None
                print("Cortando cadeado...")
                time.sleep(3)
                print('''
                PARADO!
                O policial flagrou você tentando cortar o cadeado.…
                GAME OVER!\n''')
                time.sleep(5)
                score = score - 2
                os.system('clear') or None


        #Definir resultados das escolhas de ferramentas. (CERTA)
            elif option_pt1_1 == 4:
                os.system('clear') or None
                print("\nAbrindo garrafa de vodka...\n")
                time.sleep(3)
                score = score + 8
                os.system('clear') or None
                break

        #Recusar opções inválidas.
            else: 
                os.system('clear') or None
                print("\nOpção inválida!\nTente novamente.\n")
                time.sleep(3)
                os.system('clear') or None

        #Definindo continuação da resposta certa.
        while game == 0:
            print('''\n
                Policial se aproxima:
                Policial: 
                -Parado! Aonde conseguiu isso?\n
                ''')
            time.sleep(5)
            print('''\n
                -----------------------------------------------
                1. Roubei do refeitório.    
                2. Ganhei de um guarda por bom comportamento.
                3. Consegui com um amigo aqui dentro.
                -----------------------------------------------
                ''')

            #Pedir resposta
            answer_pt1_1 = int(input("Digite a resposta desejada: "))
            
            #Definir resultados das escolhas de resposta. (ERRADAS)
            if answer_pt1_1 == 1:
                print('''\n
                Você: 
                -Ah, você sabe né, todos distraídos no refeitório, uma garrafa não faria falta…\n
                ''')
                time.sleep(3)
                print("Resposta incorreta. O guarda confiscou sua vodka.\n")
                time.sleep(5)
                score = score - 3
                os.system('clear') or None

            elif answer_pt1_1 == 3:
                print('''\n
                Você: 
                -Seu guarda… todos nós temos nosso contatos, não?\n
                ''')
                time.sleep(3)
                print("Resposta incorreta. O guarda confiscou sua vodka.\n")
                time.sleep(5)
                score = score - 3
                os.system('clear') or None

            elif answer_pt1_1 == 2:
                print('''\n
                Você:
                -Ganhei de um guarda por ter feito meu trabalho... maneiro, não?\n
                ''')
                time.sleep(3)
                score = score + 6
                break

            #Recusar opções inválidas.
            else: 
                print("\nOpção inválida!\nTente novamente.\n")
                time.sleep(3)
                os.system('clear') or None

        while game == 0: 
            print('''\n
                Policial:
                -Entendi... e o que pensa em fazer com isso?\n
                ''')
            time.sleep(3)

            print('''\n
            ----------------------------------
            1. Convidar para beber.
            2. Dar de presente para policial.
            3. Desafiar policial.\n
            ----------------------------------
            ''')

            #Pedir resposta
            answer_pt1_2 = int(input("Digite a resposta desejada: "))
            
            #Definir resultados das escolhas de resposta. (ERRADAS)
            if answer_pt1_2 == 1:
                os.system('clear') or None
                print('''\n
                Você: 
                -O que acha que tomarmos umas juntos?\n
                ''')
                time.sleep(3)
                print("Resposta incorreta. O guarda confiscou sua vodka.")
                time.sleep(5)
                score = score - 3
                os.system('clear') or None

            elif answer_pt1_2 == 2:
                os.system('clear') or None
                print('''\n
                Você:
                -Ah, já é o final do seu turno… pensei em fazer uma caridade. Toma, de presente para você.\n
                ''')
                time.sleep(3)
                print("Resposta incorreta. O guarda recusou o presente e confiscou sua vodka.\n")
                time.sleep(5)
                score = score - 3
                os.system('clear') or None

            #Definir resultados das escolhas de resposta. (CERTA)    
            elif answer_pt1_2 == 3:
                os.system('clear') or None
                print('''\n
                Você: 
                -Olha, já é final do seu turno… dizem que essa aqui é só para os homens fortes mesmo. 
                Acha que é capaz? Eu acho que não…\n
                ''')
                time.sleep(5)
                print('''
                Policial:
                -Ah é?! Me dê isso aqui então e eu te mostro o que é homem!
                ''') 
                time.sleep(6)
                score = score + 6
                os.system('clear') or None
                break

            #Recusar opções inválidas.
            else: 
                os.system('clear') or None
                print("\nOpção inválida!\nTente novamente.\n")
                time.sleep(3)
                os.system('clear') or None

    #------------------------------------------------ Parte 2 ---------------------------------------------------

        
        print("O policial ficou bêbado e você conseguiu pegar a chave da cela e sair.")
        time.sleep(4)
        print("Agora, terá que escolher a melhor rota para sair da prisão.")
        time.sleep(4)
        print("Sua missão é encontrar a Sala de Segurança, para então, ter o controle da prisão.")
        time.sleep(4)
        print("O caminho mais discreto para isso é pela tubulação da prisão.")
        time.sleep(4)
        print("Vá para o refeitório tentar o acesso à tubulação.\n")
        time.sleep(6)
        os.system('clear') or None 

        print("Indo para o refeitório...\n")
        time.sleep(5)
        os.system('clear') or None

        print("Você não conseguiu entrar no refeitório devido a uma porta travada.")
        time.sleep(3)
        print("Para conseguir ter acesso à tubulação, você precisará de um cartão de acesso.")
        time.sleep(3)
        print("Dizem que Clin, o chefe da maior gangue do país, tem acesso à essas coisas, devido a mafia policial.")
        time.sleep(5)
        print("Ele passa seu dia no pátio, vá e tente negociar um cartão de acesso.")
        time.sleep(3)
        print("Só não se esqueça com quem está lidando...\n")
        time.sleep(3)
        os.system('clear') or None

        print("Indo para o pátio...")
        time.sleep(5)
        os.system('clear') or None
        
        #Diálogo pré minigame basquete
        print("Você chegou no pátio mas precisa encontrar Clin para negociar o cartão de acesso.\n")
        time.sleep(5)
        print("Dois presos se aproximam de você...\n")
        time.sleep(4)
        os.system('clear') or None
        print('''
                T-Dog:
                -Olha só, Big Mike, temos alguém que se perdeu aqui...\n
                ''') 
        time.sleep(6)

        print('''
                Big Mike:
                -Eai, novato, o que acha que ta fazendo invadindo nosso pedaço?\n
                ''') 
        time.sleep(6)

        while game == 0:
            #Opções de resposta
                print('''\n
                    ------------------------------
                    1. Sai da minha frente!
                    2. Preciso encontrar o Clin.
                    3. Não é da sua conta.
                    ------------------------------
                    ''')

                    #Pedir resposta
                answer_pt2_1 = int(input("Digite a resposta desejada: "))
                    
                #Definir resultados das escolhas de resposta.
                if answer_pt2_1 == 1:
                    print('''\n
                    Você: 
                    -Gordo ainda não é invisível... sai da minha frente! \n
                    ''')
                    time.sleep(4)
                    print('''\n
                    Big Mike não gostou da sua resposta e resolveu te dar uma lição.
                    Missão Fracassada. \n
                    ''')
                    time.sleep(5)
                    score = score - 4
                    os.system('clear') or None

                elif answer_pt2_1 == 2:
                    print('''\n
                    Você:
                    -Preciso falar com o Clin.\n
                    ''')
                    time.sleep(3)
                    score = score + 8
                    break

                #Definir resultados das escolhas de resposta.   
                elif answer_pt2_1 == 3:
                    print('''\n
                    Você: 
                    -Não é da sua conta!\n
                    ''')
                    time.sleep(4)
                    print('''\n
                    Big mike não gostou da sua resposta e resolveu te dar uma lição.
                    Missão Fracassada. \n
                    ''')
                    time.sleep(5)
                    score = score - 4
                    os.system('clear') or None
                
                #Recusar opções inválidas.
                else: 
                    print("\nOpção inválida!\nTente novamente.\n")
                    time.sleep(3)
                    os.system('clear') or None

        print("Clin se aproxima...\n")
        time.sleep(4)

        print('''
            Clin:
            -E o que você quer, novato?\n
            ''')
        time.sleep(6)  

        print('''\n
            Você: 
            -Preciso de um cartão de acesso, e soube que só poderia conseguir um com você.\n
            ''')
        time.sleep(6)

        print('''
            Clin:
            -HAHAHAHA! E você achou mesmo que seria fácil assim, invadir nosso território,
            vir falar comigo e sair feliz com o cartão na mão?!\n
            ''')
        time.sleep(6)

        print("Clin se aproxima mais...\n")
        time.sleep(4)

        print('''
            Clin:
            -Escuta aqui novato, tem uma forma para conseguir esse cartão, porém, se não conseguir,
            virará minha propriedade aqui nessa prisão.\n
            ''')
        time.sleep(6)

        print('''
            Clin:
            -Ta vendo aquela cesta de basquete ali?
            Você vai ter que me mostrar que é bom...
            Caso contrário, ficará sem o seu cartãozinho, e pertencerá a mim...
            E ai, fechado?\n
            ''')
        time.sleep(7)
        

        while game == 0:
        #Opções de resposta
            print('''\n
                -------------------------------------------
                1. Só mostre o que preciso fazer.
                2. Você é louco? Me dá esse cartão agora!
                3. Ameaçar Clin. \n
                --------------------------------------------
                ''')

                #Pedir resposta
            answer_pt2_3 = int(input("Digite a resposta desejada: "))
                
            #Definir resultados das escolhas de resposta.
            if answer_pt2_3 == 1:
                print('''\n
                Você: 
                -Só me fale o que tenho que fazer. \n
                ''')
                time.sleep(4)
                print('''\n
                Clin:
                -É disso que eu to falando, novato! \n
                ''')
                time.sleep(5)
                score = score + 4
                os.system('clear') or None
                break

            #Definir resultados das escolhas de resposta.
            elif answer_pt2_3 == 2:
                print('''\n
                Você: 
                -E você acha que é quem? Me dá esse cartão agora! \n
                ''')
                time.sleep(4)
                print('''\n
                Clin:
                -Hahahahaha! Big Mike, vem aqui ensinar uma lição a esse novato. \n
                ''')
                time.sleep(4)
                print('''\n
                Big Mike:
                -Pode deixar comigo, chefe. \n
                ''')
                time.sleep(4)
                print('''\n
                    Você não conseguiu o cartão de acesso.
                    Missão Fracassada. \n
                    ''')
                time.sleep(4)
                score = score - 2
                os.system('clear') or None

            #Definir resultados das escolhas de resposta.   
            elif answer_pt2_3 == 3:
                print('''\n
                Você: 
                -Você irá se arrepender se não me der esse cartão agora mesmo...\n
                ''')
                time.sleep(4)
                print('''\n
                Clin:
                -Hahahahaha! Big Mike, vem aqui ensinar uma lição a esse novato. \n
                ''')
                time.sleep(4)
                print('''\n
                Big Mike:
                -Pode deixar comigo, chefe. \n
                ''')
                time.sleep(4)
                print('''\n
                    Você não conseguiu o cartão de acesso.
                    Missão Fracassada. \n
                    ''')
                time.sleep(4)
                score = score - 2
                os.system('clear') or None
            
            #Recusar opções inválidas.
            else: 
                print("\nOpção inválida!\nTente novamente.\n")
                time.sleep(3)
                os.system('clear') or None
        
        #Início minigame
        minigame_basket()

        #Pós Minigame
        print("Clin se aproxima de você...")
        time.sleep(3)

        print('''
            Clin:
            -Olha só, e não é que o novato aqui sabe como jogar?
            ''')
        time.sleep(3)

        print('''
            Você:
            -Ok, agora a sua parte do acordo...
            ''')
        time.sleep(3)

        print('''
            Clin:
            -Espera aí, novato...
            -O que está pensando em fazer com esse cartão?
            ''')
        time.sleep(3)

        print('''
            Você:
            ''')

        while game == 0:
        #Opções de resposta
            print('''\n
                ---------------------
                1. Revelar plano.
                2. Ser discreto. 
                3. Ser grosso. \n
                ---------------------
                ''')

                #Pedir resposta
            answer_pt2_2 = int(input("Digite a resposta desejada: "))
                
            #Definir resultados das escolhas de resposta.
            if answer_pt2_2 == 1:
                score = score + 5
                print('''\n
                Você: 
                -Vou fugir desse lugar! \n
                ''')
                time.sleep(3)
                print("O seu plano deveria ser secreto, porém Clin lhe deu o cartão de acesso.")
                time.sleep(4)
                score = score - 2
                os.system('clear') or None
                break

            elif answer_pt2_2 == 2:
                print('''\n
                Você:
                -A injustiça um dia será cobrada e resolvida por todos...\n
                ''')
                time.sleep(3)
                print("Seu plano continua secreto. Clin lhe deu o cartão de acesso.\n")
                time.sleep(4)
                score = score + 6
                os.system('clear') or None
                break

            #Definir resultados das escolhas de resposta.   
            elif answer_pt2_2 == 3:
                print('''\n
                Você: 
                -Isso não é da sua conta! Só me dê o cartão, agora! \n
                ''')
                time.sleep(5)
                print("Clin não gostou da sua resposta e provavelmente não o ajudará caso precise. Porém, lhe deu o cartão de acesso.\n")
                time.sleep(4)
                score = score - 4
                break

            #Recusar opções inválidas.
            else: 
                print("\nOpção inválida!\nTente novamente.\n")
                time.sleep(3)
                os.system('clear') or None

    #------------------------------------------------ Parte 3 ---------------------------------------------------
        print("Você conseguiu o cartão de acesso.")
        time.sleep(4)
        print("Agora poderá ir para o refeitório seguir com seu plano de fuga.")
        time.sleep(4)
        print("Muita atenção com seus passos, ações e diálogos.")
        time.sleep(4)
        print("Um só erro pode comprometer sua missão inteira.")
        time.sleep(4)
        
        os.system('clear') or None
        print("Indo para o refeitório...\n")
        time.sleep(5)
        os.system('clear') or None
        
        #Pré Minigame
        while game == 0:
            print('''
                Você conseguiu acesso ao refeitório, agora terá que escolher a
                opção correta para dar continuidade a sua fuga.\n
                ''')
            time.sleep(4)

            print('''
                ------------------------------------------------------------
                1 - Causar uma briga como distração.
                2 - Se disfarçar de cozinheiro.
                3 - Subornar o guarda para fazer vista grossa.
                ------------------------------------------------------------
                ''')

            option_pt3_1 = int(input("Digite a opção desejada: "))

            if option_pt3_1 == 1:
                os.system('clear') or None
                time.sleep(2)
                print("\nVocê jogou sua comida em um preso.\n")
                time.sleep(2)
                print('''
                    PUNCH! 
                    O preso revidou com uma voadora nas costas e você é nocauteado!
                    GAME OVER!
                    ''')
                time.sleep(5)
                os.system('clear') or None

            elif option_pt3_1 == 2:
                os.system('clear') or None
                time.sleep(2)
                print("\nVocê se vestiu como um cozinheiro e tentará se passar por um.\n")
                time.sleep(4)
                os.system('clear') or None
                break

            if option_pt3_1 == 3:
                os.system('clear') or None
                time.sleep(2)
                print("\nIndo até Bill Gates, guarda responsável pelo refeitório...\n")
                time.sleep(6)
                os.system('clear') or None
                print('''
                    Você:
                    -Ei, guarda.\n
                    ''')
                time.sleep(4)
                print('''
                    Bill:
                    -O que você quer aqui, detento?\n
                    ''')
                time.sleep(4)
                print('''
                    Você:
                    -Estou precisando de uma ajuda... e posso oferecer um bom dinheiro por isso.\n
                    ''')
                time.sleep(4)
                print('''
                    POW! 
                    Por azar, Bill não era corrupto e não quis saber de sua proposta 
                    Você foi imobilizado. \n
                    ''')
                time.sleep(6)
                os.system('clear') or None

        #Início minigame
        minigame_kitchen()

    #------------------------------------------------ FINAL ---------------------------------------------------
        print("Você conseguiu acessar a tubulação e invadir a sala de segurança.")
        time.sleep(3)
        print('''
        Para abrir os portões e conquistar sua liberdade, você deverá informar ao
        sistema policial uma resposta.
        ''')
        time.sleep(4)
        os.system('clear') or None

        unlock_pass = input("Qual a melhor universidade de SP? \n")

        while game == 0:
            if unlock_pass == "Mackenzie" or "mackenzie" or "Mack" or "mack" or "UPM":
                print("\nMuito bem! Você acertou a resposta de segurança e abriu as saídas da prisão.\n")
                score = score + 15
                time.sleep(3)
                os.system('clear') or None
                break

            elif unlock_pass == "PUC" or "USP":
                print("HAHAHA, SÉRIO?")
                time.sleep(2)
                print("Resposta errada. Tente novamente.")
                time.sleep(2)
                score = score - 10
                os.system('clear') or None

            else:
                print("Resposta errada. Tente novamente.")
                time.sleep(2)
                score = score - 2
                os.system('clear') or None
        
        print('''
        Missão Completa! 
        Você conseguiu escapar da prisão e apresentar as provas a justiça. 
        Os reais culpados foram presos e agora você tem sua liberdade novamente.
        FIM DE JOGO! ''')
        time.sleep(5)

        #Mostrar pontuação do jogador.
        print("\nSua pontuação final é de:", score,"pontos.\n")

        print('''\n
            ┌─┐　 ─┐
            │▒│ /▒/
            │▒│/▒/
            │▒ /▒/─┬─┐
            │▒│▒|▒│▒│
        ┌┴─┴─┐-┘─┘
        │▒┌──┘▒▒▒│
        └┐▒▒▒▒▒▒┌┘
        　└┐▒▒▒▒┌
            ''')

    def game_menu():
        game = 0
        start = '''
        |-------------------------------|
        |         Prison Escape         |
        |         Fuga de Prisão        |
        |                               |
        | [1] COMEÇAR JOGO / START GAME |
        | [2] CRÉDITOS / CREDITS        |
        |-------------------------------|
                '''
        
        language = '''
        |------------------------------------|
        |        Selecione o idioma          |
        |        Select the language.        |
        |                                    |
        |     [1] PORTUGUÊS / PORTUGUESE     |
        |     [2] INGLÊS / ENGLISH           |
        |                                    |
        | [0] VOLTAR AO MENU / BACK TO MENU  |
        |------------------------------------|
                '''

        while game == 0:
            print(start)
            menu_option = int(input("Digite a opção de menu: / Enter the menu option: "))

            #Começar Jogo
            if menu_option == 1:
                print (language)
                menu_option_language = int(input("Digite a opção de menu: / Enter the menu option: "))

                #Versão em PT
                if menu_option_language == 1:
                    os.system('clear') or None
                    print("Carregando...")
                    time.sleep(2)
                    os.system('clear') or None
                    game_pt()
                    break
                
                #Versão em EN
                elif menu_option_language == 2:
                    game_en()
                    os.system('clear') or None
                    break

                elif menu_option_language == 0:
                    os.system('clear') or None
                    print("Voltando ao menu...\nReturning to menu...")
                    time.sleep(1)           
                    os.system('clear') or None

                #Opção Inválida
                else:
                    print("Opção inválida, tente novamente. / Invalid option, please try again. ")
                    time.sleep(1)
                    os.system('clear') or None

            #Apresenta os créditos
            elif menu_option == 2:
                credits()
                break

            #Opção Inválida
            else:
                os.system('clear') or None
                print("Opção inválida, tente novamente.\nInvalid option, please try again. ")
                time.sleep(1)
                os.system('clear') or None

    game_menu()

#1˚ Execução do programa.
prison_escape()


