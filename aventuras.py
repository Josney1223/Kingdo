import desenhos as Draw
import os

Adventure1 = True
Adventure2 = True
Adventure3 = True
Adventure4 = True
Adventure5 = True
Avdenture6 = True
Adventure7 = True
Adventure8 = True


def RandomAdventures(x, money, soldiers):
    os.system('cls')

    ## Igreja no Pantano
    if (x == '1'):
        Draw.Lines()
        print("Voce caminha pra um pantano, nele ha uma igreja abandonada. Ela lhe chama a atencao.")
        print()
        print("1 - Enviar um soldado para checar", "2 - Checar pessoalmente", "3 - Nao fazer nada", sep = '\n')
        y = input("O que voce faz ? ").strip()
        if (y == "1"):
            print("Voce envia o soldado, alguns momentos depois ele retorna sem nada nas maos, dizendo que ela estava vazia")
        elif (y == "2"):
            print("Voce encontra 10 GP")
            money += 10
        elif (y == "3"):
            print("Voce resolve nao fazer nada, e, como ja estar a anoitecer, retorna ao seu castelo")
        Adventure1 = False
        return [money, soldiers]

    ## Old Guy on the road
    elif (x == '2'):
        Draw.Lines()
        print("Voce caminha pela estrada, quando avista um senhor caminhando a distancia")
        print("Ele possui um chapeu acinzentado e anda com ajuda de um cajado")
        print("1 - Conversar com ele", "2 - Ignorar e continuar andando", sep = '\n')
        y = input("O que voce faz ? ").strip()
        if (y == "1"):
            print("Bom dia !!! Percebo que esta de passagem, esta passando por alguma dificuldade ?")
            print("1 - Sim, meu castelo esta em grande perigo, a Horda esta se aproximando.", "2 - As hordas estao impiedosas ultimamente, estou preocupado com minha populacao.", "3 - Está tudo bem.", sep = '\n')
            y = input("O que voce faz ? ").strip()
            if (y == "1"):
                print("Acontece, infelizmente nao tenho como te ajudar")
            elif ( y == "2"):
                print("Acho que posso ajudar com isso, me de algumas moedas de ouro.")
                y = input("Dar 10 moedas de ouro ? <sim/nao> ")
                if (y == "sim" and money >= 10):
                    print("Muito obrigado!! Tome essa saquinho")
                    money -= 10
                elif (y == "sim" and money < 10):
                    print("Parece que voce nao tem dinheiro suficiente. É realmente uma pena...")
                else:
                    print("Tudo bem você não querer, vou seguir meu caminho.", "Ele continua seguindo seu caminho.", sep = '\n')
                    
        print("Sua aventura nao chegou em lugar nenhum.")
        return [money, soldiers]

    ## 
    # elif (x == '3'):

    # ## 
    # elif (x == '4'):
    
    # ##
    # elif (x == '5'):
    
    # ##
    # elif (x == '6'):
    
    # ##
    # elif (x == '7'):
    
    # ##
    # elif (x == '8'):
    
    # ##
    # elif (x == '9'):

    ## Nao tem aventura
    else:
        return [money, soldiers]
