import time
import os

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
