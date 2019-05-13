import desenhos as Draw
import os
import time

### Main Menu
def MainMenu():
    while True:
        os.system('cls')
        Draw.Lines()
        print("Bem vindo ao reino !!!")
        print()
        print("1 - Jogar")
        print("2 - Sair")
        Draw.Lines()
        x = input("Digite sua escolha: ").strip().lower()
        if (x == "1"):
            Loading()
            break
        elif (x == "2"):
            exit()

def Loading():
    for i in range(1,4):
        os.system('cls')
        Draw.DrawLoading(i%3)
        time.sleep(0.5)
