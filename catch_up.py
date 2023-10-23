import pygame as pg

# создай окно игры
window = pg.display.set_mode((700, 500))
pg.display.set_caption('Догонялки')
# задай фон сцены
background = pg.transform.scale(pg.image.load('background.png'), (700, 500))
# создай 2 спрайта и размести их на сцене
sprite_1 = pg.transform.scale(pg.image.load('sprite1.png'), (100, 100))
sprite_2 = pg.transform.scale(pg.image.load('sprite2.png'), (100, 100))
# обработай событие «клик по кнопке "Закрыть окно"»
game = True
FPS = 60
clock = pg.time.Clock()
x_1 = 150
y_1 = 250
x_2 = 550
y_2 = 250

while game:
    window.blit(background, (0, 0))
    window.blit(sprite_1, (x_1, y_1))
    window.blit(sprite_2, (x_2, y_2))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            game = False
    key_pressed = pg.key.get_pressed()
    if key_pressed[pg.K_LEFT] and x_1 > 5:
        x_1 -= 10
    if key_pressed[pg.K_RIGHT] and x_1 < 595:
        x_1 += 10
    if key_pressed[pg.K_UP] and y_1 > 5:
        y_1 -= 10
    if key_pressed[pg.K_DOWN] and y_1 < 395:
        y_1 += 10

    if key_pressed[pg.K_a] and x_2 > 5:
        x_2 -= 10
    if key_pressed[pg.K_d] and x_2 < 595:
        x_2 += 10
    if key_pressed[pg.K_w] and y_2 > 5:
        y_2 -= 10
    if key_pressed[pg.K_s] and y_2 < 395:
        y_2 += 10     
    pg.display.update()
    clock.tick(FPS)
