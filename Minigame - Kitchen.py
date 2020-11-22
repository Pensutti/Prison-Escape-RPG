import time
import os

def minigame_kitchen():
    minigame = 0 
    minigame_kitchen = 0
    scr_mk = 0
    score_minigame_kitchen = 0

    #RESPOSTAS: 42135  5213674  24351

    #Explicação do Minigame
    print('''\n
        Você conseguiu se passar por cozinheiro. Agora deve acertar a preparação de 3 pratos em 
        sequência para conseguir acessar o depósito. Caso erre você será descoberto.
        ''')

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
            minigame_kitchen += 1 
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
        else: 
            print('\nFaça a próxima.\n')
        time.sleep(1)

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
            minigame_kitchen += 1
        else: 
            print('\n------- Verificando se acertou todas as receitas... -------\n')
        time.sleep(4)

        if(minigame_kitchen == 0):
            print('Você não acertou nenhuma receita. Tente novamente!\n')
            scr_mk = scr_mk - 6
            os.system('clear') or None

        elif(minigame_kitchen == 1):
            print('Você acertou apenas uma receita. Tente novamente!\n')
            scr_mk = scr_mk - 4
            os.system('clear') or None

        elif(minigame_kitchen == 2):
            print('Você acertou apenas duas receita. Tente novamente!\n')
            scr_mk = scr_mk -2
            os.system('clear') or None

        else:
            print('BOA! Você mostra que é um bom cozinheiro e consegue o acesso ao depósito.\n')
            scr_mk = scr_mk + 12
            score_minigame_kitchen = scr_mk
            time.sleep(3)
            break
        time.sleep(3)
        os.system('clear') or None
        

minigame_kitchen()    











