import pygame
import getpass
import principal
from pygame import mixer
from Button import Button

#sound----------------------------------
mixer.init()
sound = pygame.mixer.Sound('./sounds/sound.mp3')
mixer.Channel(0).play(sound)
#Menu-------------------------------------------
FPS = 60
class owner :
    username=getpass.getuser()




    def __init__(self):
        username = getpass.getuser()
bg = pygame.image.load("./img/bg.jpg")
bgim=pygame.transform.scale (bg , (900,600))
start_image = pygame.image.load(r'./img/Start-Button-Vector-PNG.png')
start_button_img = pygame.transform.scale (start_image , (250,150))

replay_image = pygame.image.load(r'./img/replay-button.png')
replay_button_img = pygame.transform.scale (replay_image , (150,150))

EXIT_image = pygame.image.load(r'./img/EXIT BUTTON.png')
EXIT_button_img = pygame.transform.scale (EXIT_image , (210,120))
pygame.init()
pygame.font.init()

width , height = 900,500
win =pygame.display.set_mode((width,height))

#colors----------------------------------
color =(135,206,250)
black= (0,0,0)
red =(255 , 0 ,0)
red2=(144, 10, 17)
blue = (0,0,255)
green = (0,255,0)
WHITE = (255,255,255)
#Fonts----------------------------------------
FONT = pygame.font.Font('./fonts/Poppins-Bold.ttf', 44 )
FONT1 = pygame.font.Font('./fonts/Poppins-Regular.ttf', 20 )

run = True
page = 0
win.fill((0, 0, 0))
win.blit(bgim, (0, 0))
o=owner()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    if page == 0:
        welcome_msg = FONT.render(f"Welcome {o.username.capitalize()} ", 1, WHITE)
        welcome_msg_rect = welcome_msg.get_rect(center=(width / 2, height / 6))
        win.blit(welcome_msg, welcome_msg_rect)
        start_button = Button(width // 2 - start_button_img.get_width() // 2, 150, start_button_img, win)
        exit_button = Button(width // 2 - EXIT_button_img.get_width() // 2, 300, EXIT_button_img, win)

        if start_button.drawONwindow():
            page += 1
        if exit_button.drawONwindow():
            run = False
    if page == 1:
       principal.start()

