import time
from pygame import *



def main():
    #t0 = time.time()
    #tindex += 1
    screen.fill("green")
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0)) # 10: 60+ FPS
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0)) # 20: 32 FPS
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0)) # 30: 25FPS
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0)) # 40: 21 FPS
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0))
    screen.blit(image, (0, 0)) # 50: 17 FPS

    #if tindex % 10 == 1:
    #    print(1 / (tt / tindex), "FPS")
    #tt += (time.time() - t0)

if __name__ == "__main__":
    #t0 = time.time()
    #tt = 0
    #tindex = 0
    pygame.display.set_icon("http://www.stackoverflow.com/favicon.ico")
    pygame.display.set_caption("Pygame Title")

    pygame.mixer.music.load("assets/music/final_boss.ogg")
    pygame.mixer.music.play(-1)

    screen = pygame.display.set_mode((800, 480), 1) # fullscreen flag
    image = pygame.image.load("assets/img/logo.png") # 450x178

    pygame.loop(main, 32) # <--- 32 = frames per second
