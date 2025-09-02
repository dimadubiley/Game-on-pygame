import pygame

clock = pygame.time.Clock()

#Создание и настройка окна
pygame.init() #Важная строчка кода
screen = pygame.display.set_mode((1004, 565)) #Отключить рамки - flags=pygame.NOFRAME
pygame.display.set_caption("Игра") #Название Окна
icon = pygame.image.load("images/icon.jpg") #Создаёт путь к иконке
pygame.display.set_icon(icon) #Делает иконку для програмы
screen.fill((0, 155, 0)) #Создает цвет заднего фона

#создание текста
font = pygame.font.Font('fonts/Jersey10-Regular.ttf', 40)
text_surface = font.render("I'm Mister_NP", False, "Black", )

bg = pygame.image.load("images/bg.png")
player = pygame.image.load("images/sans.png")

walkLeft = [
    pygame.image.load('images/plLeft/1.png'),
    pygame.image.load('images/plLeft/2.png'),
    pygame.image.load('images/plLeft/3.png'),
    pygame.image.load('images/plLeft/4.png')
]

walkRight = [
    pygame.image.load('images/plRight/1.png'),
    pygame.image.load('images/plRight/2.png'),
    pygame.image.load('images/plRight/3.png'),
    pygame.image.load('images/plRight/4.png')
]

plAnimCout = 0

running = True
while running: #Чтобы окно не закывалось

    screen.blit(bg, (0,0))
    screen.blit(text_surface, (790, 10))
    screen.blit(walkLeft[plAnimCout], (400,250))


    pygame.display.update() #Обновление окна. Т.е чтобы все было видно

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Чтобы Коректно закрывалось програма
            running = False
            pygame.quit()

'''
        elif event.type == pygame.KEYDOWN: # Отслеживет если нажана английская кнопка "А"
            if event.key == pygame.K_a:
                if plAnimCout == 3:
                    plAnimCout = 0
                else:
                    plAnimCout += 1
'''

    clock.tick(2)