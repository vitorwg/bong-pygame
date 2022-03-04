import pygame

pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")


def main():
    update = True

    while update:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                update = False
                break

    pygame.quit()

if __name__ == '__main__':
    main()