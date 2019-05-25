### Imports
import random
import os
import desenhos as Draw
import aventuras as Adventures
import menu as Menu

### Variaveis Globais
allAdventures = ['0','1','2','3','4','5','6','7','8','9']
exploreDay = 1
exploreSouth = []
exploreEast = []
exploreWest = []
days = 1
money = 100

backGround = 1
waveIncoming = random.randrange(3, 5)
wavesTrought = 0
soldiers = random.randrange(80, 100)
castleDmg = 1000

## Construcoes
# Torre de Vigia
watchTowerExist = False

# Mineradora
minerExist = False
iron = 0
ironCollect = 0

# Plantacao
farmExist = False
betterFarm = False
collectIncome = 0
daysIncome = 0

# Quartel
quartersExist = False
betterArmor = False
betterWeapon = False

#### Wait
def Wait():
	k = input("Pressione enter para continuar")

### Definir as aventuras de cada local
def CreateExplore():
	global exploreEast
	global exploreSouth
	global exploreWest
	global allAdventures

	exEast = 0
	exSouth = 0
	exWest = 0

	for i in allAdventures:
		x = random.randrange(3)
		if x == 0 and exSouth < 3:
			exploreSouth.append(i)
			exSouth += 1
		elif x == 1 and exEast < 3:
			exploreEast.append(i)
			exEast += 1
		elif x == 2 and exWest < 3:
			exploreWest.append(i)
			exWest += 1

### Print tabela de escolhas
def InfoMenu():
	global backGround
	global days
	os.system('cls')
	Draw.Head(days, money)
	Draw.BackGround(backGround)
	print("1 - Explore")
	print("2 - Construção")
	print("3 - Proximo Dia")
	print("")
	print("Digite exit para sair")
	Draw.Lines()

### Print Explorar
def InfoExplore():
	global exploreDay
	end = False

	# Exploracao
	while (end == False):
		os.system('cls')
		Draw.Explore()
		print("Exploracoes Restantes:", exploreDay, end = '\n')
		print("1 - Norte", "2 - Sul", "3 - Leste", "4 - Oeste", "" ,"0 - Voltar", sep = '\n', end = '\n')
		x = input("Digite a sua escolha: ").strip()
						
		if (x == "0"):
			end = True
			
		elif (x == "1"):
			print("Melhor não se aventurar ao norte, as invasões estão vindo daquela região")
			Wait()
			
		elif (x == "2"):
			y = input("Tem certeza que quer ir ao sul ? <sim/não> ").lower().strip()
			if (y == "sim" and exploreDay >= 1 and exploreSouth != []):
				Explore(x)
				exploreDay -= 1
				
			elif (y == "sim" and exploreDay < 1):
				print("Você não pode mais explorar hoje")
				Wait()

			elif (exploreSouth == []):
				print("Nao ha mais o que explorar ao Sul")
				Wait()

		elif (x == "3"):
			y = input("Tem certeza que quer ir ao Leste ? <sim/não> ").lower().strip()
			if (y == "sim" and exploreDay >= 1 and exploreEast != []):
				Explore(x)
				exploreDay -= 1
				
			elif (y == "sim" and exploreDay < 1):
				print("Você não pode mais explorar hoje")
				Wait()

			elif (exploreEast == []):
				print("Nao ha mais o que explorar ao Leste")
				Wait()

		elif (x == "4"):
			y = input("Tem certeza que quer ir ao Oeste ? <sim/Não> ").lower().strip()
			if (y == "sim" and exploreDay >= 1 and exploreWest != []):
				Explore(x)
				exploreDay -= 1
				
			elif (y == "sim" and exploreDay < 1):
				print("Você não pode mais explorar hoje")
				Wait()

			elif (exploreWest == []):
				print("Nao ha mais o que explorar ao Oeste")
				Wait()

## Explorar ao Sul da Provincia
def Explore(x):
	global money
	global soldiers
	global exploreEast
	global exploreSouth
	global exploreWest

	if x == "2":
		y = random.randrange(len(exploreSouth))
		lista = Adventures.RandomAdventures(exploreSouth[y], money, soldiers)
		exploreSouth.pop(y)
	elif x == "3":
		y = random.randrange(len(exploreEast))
		lista = Adventures.RandomAdventures(exploreEast[y], money, soldiers)
		exploreEast.pop(y)
	elif x == "4":
		y = random.randrange(len(exploreWest))
		lista = Adventures.RandomAdventures(exploreWest[y], money, soldiers)
		exploreWest.pop(y)

	money = int(lista[0])
	soldiers = int(lista[1])
	Wait()

### Construcao
def InfoBuilding():
	global soldiers
	global betterArmor
	global betterWeapon
	global money
	global days
	global quartersExist
	global farmExist
	global minerExist
	global watchTowerExist
	global ironCollect
	
	while True:
		os.system('cls')
		Draw.Head(days, money)
		#Draw.BuildingsDraw()
		print("1 - Quartel", "2 - Torre de Vigia", "3 - Fazenda", "4 - Mina", "", "0 - Voltar", sep = '\n')
		Draw.Lines()
		x = input("Digite a sua escolha: ").strip()
		if (x == "0"):
			break
		elif (x == "1"):
			if (quartersExist == True):
				Quarters()
			else:
				while True:
					print("Voce nao possui uma quartel", "Quer construir um? <sim/nao> (Custo 40gp)", sep = '\n')
					y = input("").lower().strip()
					if (y == "sim" and money >= 40):
						print("Voce construiu um quartel !!!")
						quartersExist = True
						money -= 40
						Wait()
						break
					elif (y == "sim"):
						print("Voce nao possui dinheiro para conseguir construir um quartel")
					elif(y == "nao"):
						break
		elif (x == "2"):
			if (watchTowerExist == True):
				WatchTower()
			else:
				while True:
					print("Voce nao possui uma torre de vigia", "Quer construir uma? <sim/nao> (Custo 10gp)", sep = '\n')
					y = input("").lower().strip()
					if (y == "sim" and money >= 10):
						print("Voce construiu uma torre de vigia !!!")
						watchTowerExist = True
						money -= 10
						Wait()
						break
					elif (y == "sim"):
						print("Voce nao possui dinheiro para conseguir construir uma torre de vigia")
					elif(y == "nao"):
						break
		elif (x == "3"):
			if (farmExist == True):
				Farm()
			else:
				while True:
					print("Voce nao possui uma fazenda", "Quer construir uma? <sim/nao> (Custo 25gp)", sep = '\n')
					y = input("").lower().strip()
					if (y == "sim" and money >= 25):
						print("Voce construiu uma fazenda!!!")
						farmExist = True
						money -= 25
						Wait()
						break
					elif (y == "sim"):
						print("Voce não possui dinheiro para conseguir construir uma fazenda")
					elif(y == "nao"):
						break
		elif (x == "4"):
			if minerExist == True:
				print("Você já possui uma mina. Logo poderá melhorar os equipamentos dos seu exército.")
				Wait()
			else:
				while True:
					print("Você não possui uma mina", "Gostaria de construir uma? <sim/nao> (Custo 50GP)", sep = '\n')
					y = input('').lower().strip()
					if y == 'sim' and money >= 50:
						print("Você construiu uma mina!!!")
						minerExist = True
						money -= 50
						ironCollect = 2
						Wait()
						break
					elif y == 'sim':
						print("Voce não possui dinheiro para conseguir construir uma mina")
					elif(y == "nao"):
						break

### Funcao torre de vigia
def WatchTower():
	global waveIncoming
	global days
	global money
	os.system('cls')
	Draw.Head(days, money)
	Draw.Watcher()
	if (waveIncoming > 2):
		x = random.randrange (0, 2)
		if (x == 1):
			print("O vigia avisou que a proxima horda de inimigos chegara em", waveIncoming -1, "ou", waveIncoming, "dias")
		else:
			print("O vigia avisou que a proxima horda de inimigos chegara em", waveIncoming, "ou", waveIncoming+1, "dias")
		Wait()
	else:
		print("A proxima horda de inimigos chegara em", waveIncoming, "dias")
		Wait()

### Quartel
def Quarters():
	global soldiers
	global days
	global money
	global betterArmor
	global betterWeapon
	global iron
	global ironCollect

	while True:
		os.system('cls')
		Draw.Head(days, money)
		Draw.DrawingQuarters(betterWeapon, betterArmor)
		
		print("Voce possui", soldiers,"soldados e", iron, "ferros")
		print("1 - Recrutar Tropas (10 GP)", "2 - Melhorar armaduras (5 Ferros)(+30% Defesa)", "3 - Melhorar armas (4 Ferros)(+30% Dano)","","0 - Voltar", sep = '\n')
		
		x = input("Digite a sua escolha: ").strip()
		if (x == "0"):
			break

		elif (x == "1"):
			y = random.randrange(10, 15)
			soldiers += y
			money -= 10
			print("Voce recrutou", y, "novos soldados para seu exercito!!")
			Wait()
			
		elif (x == "2"):
			if (iron < 5 and betterArmor == False):
				print("Voce não possui material suficiente para essa melhoria.")
				Wait()
				
			elif (betterArmor == False):
				betterArmor = True
				iron -= 5
				ironCollect -= 1
				print("Voce melhorou a qualidade geral das suas armadura.")
				Wait()
				
			else:
				print("Voce ja melhorou suas armaduras.")
				Wait()

		elif (x == "3"):
			if (iron < 4 and betterWeapon == False):
				print("Voce não possui material suficiente para essa melhoria.")
				Wait()
				
			elif (betterWeapon == False):
				betterWeapon = True
				iron -= 4
				ironCollect -= 1
				print("Voce melhorou a qualidade geral das suas armas.")
				Wait()
				
			else:
				print("Voce ja melhorou suas armas.")
				Wait()

### Fazenda
def Farm():
	global collectIncome
	global betterFarm
	global money
	global daysIncome
	global days

	while True:
		os.system('cls')
		Draw.Head(days, money)
		#Draw.DrawFarm()
		print("1 - Coletar lucros", "2 - Construir moinho (35gp) (Aumento significativo do lucro ao longo prazo)", "", "0 - Voltar", sep = '\n')
		Draw.Lines()
		y = input("Digite a sua escolha: ").lower().strip()
		if (y == "0"):
			break
		elif (y == "1"):
			money += collectIncome
			print("Você coletou", collectIncome, "gp")
			collectIncome = 0
			daysIncome = 0
			Wait()
		elif (y == "2"):
			if (betterFarm == True):
				print("Você já construiu um moinho!")
			elif (money >= 40):
				print("Você construiu um moinho.")
				money -= 35
				betterFarm = True
			else:
				print("Você não tem dinheiro para construir o moinho.")
			Wait()

### Função entre dias
def NewDay():
	global exploreDay
	global waveIncoming
	global backGround
	global wavesTrought
	global castleDmg
	global days
	global farmExist
	global minerExist
	global collectIncome
	global betterFarm
	global daysIncome
	global iron
	global ironCollect
	
	days += 1
	exploreDay = 1
	waveIncoming -= 1

	# Recurso Mina
	if minerExist == True and ironCollect > 0:
		iron += random.randrange(1, ironCollect+1)

	# Lucro Fazenda
	if (farmExist == True):
		daysIncome += 1
		if (betterFarm == True):
			collectIncome = daysIncome**2 - daysIncome
		else:
			collectIncome = daysIncome*2
	
	# Check dia da horda
	if (waveIncoming <= 0):
		wavesTrought += 1
		Wave()
		waveIncoming = random.randrange(3, 8 - wavesTrought)
		
	# Check estado do castelo
	if (castleDmg > 400 and castleDmg < 750):
		backGround = 2
	elif (castleDmg < 400):
		backGround = 3

	Menu.Loading()

## Ação da Horda
def Wave():
	global wavesTrought
	global castleDmg
	global soldiers
	global betterWeapon
	global betterArmor
	
	waveNumberHP = random.randrange(50 + wavesTrought*50, 100 + wavesTrought*50)       
			
	# Transformar o int castleDmg em uma String
	def CastleStatus(castleDmg):
		if (castleDmg > 750):
			return "em boas condicoes"
		elif (castleDmg < 750 and castleDmg > 400):
			return "com rachaduras"
		elif (castleDmg < 400):
			return "desmoronando"

   # Combate da Horda 
	while (waveNumberHP > 0 and soldiers > 0):
		os.system('cls')
		
		Draw.WaveDrawing(soldiers, betterWeapon)
		if (waveNumberHP > 100):
			print("A horda esta a sua porta, eles possuem por volta de", (waveNumberHP//100)*100,"monstros.")
			print("Voce possui", soldiers, "soldados e seu castelo esta", CastleStatus(castleDmg))
		elif (waveNumberHP < 10):
			print("A horda esta a sua porta, eles possuem por volta de", waveNumberHP,"monstros.")
			print("Voce possui", soldiers, "soldados e seu castelo esta", CastleStatus(castleDmg))
		else:
			print("A horda esta a sua porta, eles possuem por volta de", (waveNumberHP//10)*10,"monstros.")
			print("Voce possui", soldiers, "soldados e seu castelo esta", CastleStatus(castleDmg))

		print("O que deseja fazer ?")
		print("", "1 - Atacar", "2 - Defender", "", sep = '\n')
		
		x = input("Digite a sua escolha: ").strip()
		
		if (x == "1"):
			tempWaveNumberHP = waveNumberHP
		
			if (betterWeapon == True):
				waveNumberHP -= soldiers
			else:
				waveNumberHP -= soldiers//2 + soldiers//4

			if (betterArmor == True):
				soldiers -= tempWaveNumberHP//8
			else:           
				soldiers -= tempWaveNumberHP//6

		elif (x == "2"):
			tempWaveNumberHP = waveNumberHP
			castleDmg -= tempWaveNumberHP/2
		
			if (betterWeapon == True):
				waveNumberHP -= soldiers//2 + soldiers//4
			else:
				waveNumberHP -= soldiers//2

			if (betterArmor == True):
				soldiers -= tempWaveNumberHP//15
			else:           
				soldiers -= tempWaveNumberHP//10            
			
	if (soldiers <= 0):
		LoseScreen()
	else:
		print("Voce venceu a " + str(wavesTrought) + "o Horda!!!")
		Wait()
			
### Lose Screen
def LoseScreen():
	os.system('cls')
	Draw.BackGround(4)
	print("Voce perdeu, os monstros invadiram o seu reino e o deixaram e ruinas")
	Wait()
	exit()

### Win Screen
def WinScreen():
	Draw.BackGround(backGround)
	print("Parabens, voce conseguiu sobreviver as 3 hordas !!!")
	Wait()
	exit()

### Start Loop
CreateExplore()
Menu.MainMenu()
while True:
	InfoMenu()
	x = input("Digite a sua escolha: ").strip().lower()
	if (x == "1"):
		InfoExplore()
	elif (x == "2"):
		InfoBuilding()
	elif (x == "3"):
		NewDay()
		if (wavesTrought >= 4):
			WinScreen()
	elif (x == "exit"):
		exit()