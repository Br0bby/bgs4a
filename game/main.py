from pygame import *

def main():
    screen.fill("green")
    screen.blit(background, (0, 0))
    screen.blit(image, (415, 311)) # 1280 / 2 (screen width) - 450 / 2 (image width)...

if __name__ == "__main__":
    pygame.display.set_icon("http://www.stackoverflow.com/favicon.ico")
    pygame.display.set_caption("Pygame Title")

    #pygame.mixer.music.load("assets/music/battle.ogg")
    #pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((1280, 800), 1) # fullscreen flag
    background = pygame.image.load("assets/img/background.jpg") # 1280x800
    image = pygame.image.load("assets/img/logo.png") # 450x178

    pygame.loop(main, 32) # <--- 32 = frames per second
