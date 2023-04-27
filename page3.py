import pygame
import principal
from pygame import mixer
from Button import Button

def go():
    mixer.init()
    lose = pygame.mixer.Sound('./sounds/Lose.mp3')
    mixer.Channel(0).play(lose)

    pygame.init()
    pygame.font.init()
    bg = pygame.image.load("./img/bg.jpg")
    bgim=pygame.transform.scale (bg , (900,600))
    EXIT_image = pygame.image.load(r'./img/EXIT BUTTON.png')
    EXIT_button_img = pygame.transform.scale (EXIT_image , (210,120))
    replay_image = pygame.image.load(r'./img/replay-button.png')
    replay_button_img = pygame.transform.scale (replay_image , (150,150))

    width , height = 900,500
    win =pygame.display.set_mode((width,height))
    win.fill((0, 0, 0))
    win.blit(bgim, (0, 0))

    replay_button = Button(width // 2 - replay_button_img.get_width() // 2, 150, replay_button_img, win)

    exit_button = Button(width // 2 - EXIT_button_img.get_width() // 2, 320, EXIT_button_img, win)
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()
        if exit_button.drawONwindow():
            run = False
        if replay_button.drawONwindow():
            principal.start()
    pygame.quit()
