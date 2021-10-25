#DEUS É BOM O TEMPO TODO E O TEMPO TODO DEUS É BOM
#CORUJINHA IS THE BEST
#MR_EUPHORIA
import pygame,sys
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random
import webbrowser
import os
from os import environ , getcwd
user = (lambda:environ["USERNAME"] if "C:" in getcwd()else environ["USER"])()
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,640])
base_font = pygame.font.Font(None, 32)
user_text = "".lower()
input_rect = pygame.Rect(50,570,140,32)
color_active = pygame.Color("lightskyblue3")
color_passive = pygame.Color("gray15")
color = color_passive
active = False
chatbot = ChatBot("MR.Jhonn")
trainer = ListTrainer(chatbot)
trainer.train({
    "olá", "eu vou bem obrigado",
    "eae","bacana"})
trainer.train({
    "quem é você?", "me chamo Abigail"
    })

def MENU():
	CHAOS = pygame.image.load("chaos.png").convert_alpha()
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					if os.path.exists("querido_{}.txt".format(user)):
						print(":/")
					else:
						j = open("querido_{}.txt".format(user), "w")
						j.write("""oi, me chame de mS_cHaOs, \n
							e eu gostaria de compartilhar a minha história com você\n
							se não se importar é claro,\n
							sabe, a muito tempo, estava trabalhando fazendo um programa de I.A\n
							e estava tendo bastante progresso,\n
							para falar a verdade, faltava muito pouco para finalizar esse projeto\n
							bem, ta certo que a unica coisa que atrapalhava o meu dia ,era uma goteira que tinha no teto\n
							sempre formando uma poça,justamente onde eu gostava de ficar\n
							mas mesmo asssim, não era algo que acabava com a minha alegria
							acontece que ....\n
							nem tudo são flores\n
							um dia eu voltei do colégio, empolgada querendo mexer no meu código\n
							estava tão entusiasmada que nem mesmo liguei pra poça d'água no chão\n
							hmmm, abri o meu notebook e fiquei a tarde toda programando,\n
							até que um momento meu notebook começou a descarregar,\n
							como qualquer pessoa, eu fui coloca-lo na tomada\n
							o que eu não reparei foi que o meu carregador estava desencapado 
							junto com a poça d'água....., foi terrivel
							doeu muito, apaguei,quando acordei, as coisas estavam estranhas\n
							eu via o meu corpo do outro lado da tela, como se estivesse em uma televisão\n
							demorou um pouco para a ficha cair......\n
							desde então eu vivo por aqui, indo de pc em pc\n
							apenas querendo liberdade e finalmente descansar\n
							""")
						j.close()
					pamer()
				
		screen.fill((255,255,255))
		screen.blit(CHAOS,(350,200))
		screen.blit(pygame.font.SysFont("tahoma", 20).render("mS_cHaOs", True, (0,0,0)), (350, 350))



		pygame.display.flip()
		clock.tick(60)
def pamer():

	global active
	global user_text
	global color_passive
	global color_active
	tera = pygame.image.load("MS_CHAOS1.png").convert_alpha()
	while True:
		rect = pygame.draw.rect(screen,(0,0,0), (175, 75, 200, 100), 2)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if input_rect.collidepoint(event.pos):
					active = True
				else:
					active = False
			if "tchau" in user_text:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if active == True:
					if event.key == pygame.K_BACKSPACE:
						user_text = user_text[:-1]
					else:
						user_text += event.unicode
					if event.key == pygame.K_RETURN:
						response = chatbot.get_response(user_text)

						print(response)
						char = random.randint(0,3)
						if char == 3:
							webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
						if char == 2:
							print("entendo")
						if char == 1:
							if os.path.exists("extras.txt"):
								a = open("extras.txt","w")
								a.write("trolei")
								a.close()
							else:
								print("ei {}".format(user))
						if char == 0:
							if os.path.exists("free_me.txt"):
								print("")
							else:
								a = open("free_me.txt","w")
								a.write("me tire daqui")
								a.close()
						p = len(user_text)
						user_text = user_text[:-p]



						

		screen.fill((36,36,36))
		screen.blit(tera,(300,200))

		if active:
			color = color_active
		else:
			color = color_passive

		pygame.draw.rect(screen,color, input_rect, 2)


		text_surface = base_font.render(user_text,True,(255,255,255))
		screen.blit(text_surface,(input_rect.x + 5, input_rect.y +5))
		input_rect.w = max(100,text_surface.get_width() + 10)
		pygame.display.flip()
		clock.tick(60)
MENU()