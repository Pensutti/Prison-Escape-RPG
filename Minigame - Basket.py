import time
import os

def minigame_basket():
    minigame = 0
    points = 0

    #Explicação do minigame
    '''
    A cada 3 cestas - 1 ponto.
    2 pontos - Ganha o jogo.
    Você poderá usar apenas números inteiros.
    '''

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
                Droga, 1 cesta...
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
                Droga, 1 cesta...
                ''')
            time.sleep(3)
            points = points + 1
            print("Pontuação: ", points, "pontos.")
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

minigame_basket()