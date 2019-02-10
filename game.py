# -*- coding: utf8 -*-

import os
import sys
import pygame
import copy
import random

questions_mode1 = {'Переведите 965 из 10-чной в 16-чную сс': '3C5',
                   'Переведите 562 из 10-чной в 2-чную сс': '1000110010',
                   'Переведите в 10-чную сc двоичное число 101001': '41'}
questions_mode2 = {'Вычислите 8F – 80 в 16-чной cc (ответ дать в 10-чной)': '15',
                   'Вычислите 8E − 8B в 16-чной сc (ответ дать в 10-чной)': '4',
                   'Вычислите 82 + 1E в 16-чной cc (ответ дать в 10-чной)': '160'}
questions_mode3 = {'((K \/ L) -> (L /\ M /\ N)) = 0': '10',
                   '(X /\ Y \/ Z) -> (Z \/ P) = 0': '1',
                   '(K /\ L) \/ (M /\ N) = 1': '7'}
pygame.init()
size = width, height = 700, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dyno IT")
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
running = True
start_running = True
wasted_running = True
mode = -1
hp = 100


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class MainMenu:
    def start_screen():
        global running, start_running, rules_running, screen, size, mode
        intro_text = ['Hello, world!',
                      'Пожалуйста, выберите режим игры!']
        buttons = ['Системы счисления',
                   'Операции в сс, отличных от 10-чной',
                   'Логические уравнения']
        rules = ['Правила игры']
        fon = pygame.transform.scale(load_image('rules_fon.jpg'), (700, 450))
        screen.blit(fon, (0, 0))
        font = pygame.font.SysFont('verdana', 35)
        text_coord = 30
        for line in intro_text:
            string_rendered = font.render(line, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        font = pygame.font.SysFont('verdana', 20)
        for line in rules:
            string_rendered = font.render(line, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            print(intro_rect)
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        font = pygame.font.SysFont('serif', 17)
        for line in buttons:
            string_rendered = font.render(line, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            print(intro_rect)
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        while start_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start_running = False
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (event.pos[0] > 10 and event.pos[0] < 155 and
                            event.pos[1] > 148 and event.pos[1] < 174):
                        start_running = False
                        rules_running = True
                    elif (event.pos[0] > 10 and event.pos[0] < 174 and
                          event.pos[1] > 184 and event.pos[1] < 204):
                        mode = 0
                        start_running = False
                        size = width, height = 700, 400
                        screen = pygame.display.set_mode(size)
                    elif (event.pos[0] > 10 and event.pos[0] < 323 and
                          event.pos[1] > 214 and event.pos[1] < 234):
                        mode = 1
                        start_running = False
                        size = width, height = 700, 400
                        screen = pygame.display.set_mode(size)
                    elif (event.pos[0] > 10 and event.pos[0] < 215 and
                          event.pos[1] > 244 and event.pos[1] < 264):
                        mode = 2
                        start_running = False
                        size = width, height = 700, 400
                        screen = pygame.display.set_mode(size)
            pygame.display.flip()
            clock.tick(20)


class Rules:
    def start_screen():
        global running, start_running, rules_running, screen, size, mode
        intro_text = ['Правила игры']
        rules_text = ['1) Выберите режим игры в главном меню',
                      '2) Вы играете за динозаврика',
                      '   Вы должны уворачиваться от злых котов',
                      '3) Если вы сталкиваетесь с котом, ваше здоровье падает',
                      '4) Если ваши очки здоровья равны нулю, вы должны',
                      '   решить задачу по информатике, чтобы продолжить игру']
        main_text = ['В главное меню']
        fon = pygame.transform.scale(load_image('rules_fon.jpg'), (700, 450))
        screen.blit(fon, (0, 0))
        font = pygame.font.SysFont('verdana', 35)
        text_coord = 30
        for line in intro_text:
            string_rendered = font.render(line, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        font = pygame.font.SysFont('serif', 20)
        for line in rules_text:
            string_rendered = font.render(line, 1, (230, 230, 230))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        font = pygame.font.SysFont('serif', 25)
        for line in main_text:
            string_rendered = font.render(line, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            print(intro_rect)
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
            font = pygame.font.SysFont('verdana', 20)
        while rules_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rules_running = False
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (event.pos[0] > 10 and event.pos[0] < 146
                            and event.pos[1] > 292 and event.pos[1] < 315):
                        start_running = True
                        rules_running = False
            pygame.display.flip()
            clock.tick(20)


class Questioner_1:
    def start_screen():
        global running, screen, size, mode, wasted, wasted_running, dyno
        global questions_mode1, start_running, running, player_sprites, hp, sprite, image
        global pause, rules_running, enemy_sprites, up, down, updelta, downdelta, y_speed, x_speed
        screen.fill((100, 100, 200))
        intro_text = ['Вы проиграли!', 'Чтобы продолжить, ответьте на вопрос:']
        question = random.sample(questions_mode1.items(), 1)
        main_text = ['В главное меню']
        fon = pygame.transform.scale(load_image('rules_fon.jpg'), (700, 450))
        screen.blit(fon, (0, 0))
        font = pygame.font.SysFont('verdana', 30)
        text_coord = 30
        for line in intro_text:
            string_rendered = font.render(line, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        font = pygame.font.Font(None, 27)
        text = font.render(question[0][0], True, (255, 255, 255))
        screen.blit(text, [10, 150])
        answer = ''
        pygame.draw.rect(screen, (255, 255, 255), (0, 200, 900, 30))
        font = pygame.font.SysFont('serif', 25)
        text_coord = 30
        for line in main_text:
            string_rendered = font.render(line, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = 300
            intro_rect.x = 10
            print(intro_rect)
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        while wasted_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start_running = False
                    running = False
                    wasted_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (event.pos[0] > 10 and event.pos[0] < 178 and
                            event.pos[1] > 300 and event.pos[1] < 329):
                        running = True
                        start_running = True
                        wasted_running = False
                        wasted = False
                        mode = -1
                        hp = 100
                        player_sprites = pygame.sprite.Group()
                        sprite = pygame.sprite.Sprite()
                        image = pygame.transform.scale(load_image("dyno_running.png"), (150, 80))
                        dyno = AnimatedSprite(image, 2, 1, 50, 50)
                        dyno.rect = dyno.image.get_rect()
                        player_sprites.add(dyno)
                        dyno.rect.x = 5
                        dyno.rect.y = 150
                        pause = 0
                        y_speed = 0
                        x_speed = 0
                        wasted = False
                        rules_running = False
                        enemy_sprites = pygame.sprite.Group()
                        for _ in range(10):
                            sprite = pygame.sprite.Sprite()
                            sprite.image = pygame.transform.scale(load_image("2.png"), (50, 50))
                            sprite.rect = sprite.image.get_rect()
                            sprite.rect.x = random.randrange(0, 700)
                            sprite.rect.y = random.randrange(0, 700)
                            enemy_sprites.add(sprite)

                        up = False
                        down = False
                        updelta = 10
                        downdelta = -10
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if answer != question[0][1]:
                            start_running = False
                            running = False
                            wasted_running = False
                        else:
                            hp = 100
                            running = True
                            wasted_running = False
                            wasted = False
                    elif event.key == pygame.K_BACKSPACE:
                        answer = answer[:-1]
                        pygame.draw.rect(screen, (255, 255, 255), (0, 200, 900, 30))
                    else:
                        answer += event.unicode
            if answer != '':
                answer_text = font.render(answer, True, (0, 10, 0))
                screen.blit(answer_text, [10, 200])
            pygame.display.flip()
            clock.tick(20)


class Questioner_2:
    def start_screen():
        global running, screen, size, mode, wasted, wasted_running, dyno
        global questions_mode2, start_running, running, player_sprites, \
            hp, sprite, image
        global pause, rules_running, enemy_sprites, up, down, \
            updelta, downdelta, y_speed, x_speed
        screen.fill((100, 100, 200))
        intro_text = ['Вы проиграли!', 'Чтобы продолжить, ответьте на вопрос:']
        question = random.sample(questions_mode2.items(), 1)
        main_text = ['В главное меню']
        fon = pygame.transform.scale(load_image('rules_fon.jpg'), (700, 450))
        screen.blit(fon, (0, 0))
        font = pygame.font.SysFont('verdana', 30)
        text_coord = 30
        for line in intro_text:
            string_rendered = font.render(line, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        font = pygame.font.Font(None, 27)
        text = font.render(question[0][0], True, (255, 255, 255))
        screen.blit(text, [10, 150])
        answer = ''
        pygame.draw.rect(screen, (255, 255, 255), (0, 200, 900, 30))
        font = pygame.font.SysFont('serif', 25)
        text_coord = 30
        for line in main_text:
            string_rendered = font.render(line, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = 300
            intro_rect.x = 10
            print(intro_rect)
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        while wasted_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start_running = False
                    running = False
                    wasted_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (event.pos[0] > 10 and event.pos[0] < 178 and
                            event.pos[1] > 300 and event.pos[1] < 329):
                        running = True
                        start_running = True
                        wasted_running = False
                        wasted = False
                        mode = -1
                        hp = 100
                        player_sprites = pygame.sprite.Group()
                        sprite = pygame.sprite.Sprite()
                        image = pygame.transform.scale(load_image("dyno_running.png"), (150, 80))
                        dyno = AnimatedSprite(image, 2, 1, 50, 50)
                        dyno.rect = dyno.image.get_rect()
                        player_sprites.add(dyno)
                        dyno.rect.x = 5
                        dyno.rect.y = 150
                        pause = 0
                        y_speed = 0
                        x_speed = 0
                        wasted = False
                        rules_running = False
                        enemy_sprites = pygame.sprite.Group()
                        for _ in range(10):
                            sprite = pygame.sprite.Sprite()
                            sprite.image = pygame.transform.scale(load_image("2.png"), (50, 50))
                            sprite.rect = sprite.image.get_rect()
                            sprite.rect.x = random.randrange(0, 700)
                            sprite.rect.y = random.randrange(0, 700)
                            enemy_sprites.add(sprite)

                        up = False
                        down = False
                        updelta = 10
                        downdelta = -10
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if answer != question[0][1]:
                            start_running = False
                            running = False
                            wasted_running = False
                        else:
                            hp = 100
                            running = True
                            wasted_running = False
                            wasted = False
                    elif event.key == pygame.K_BACKSPACE:
                        answer = answer[:-1]
                        pygame.draw.rect(screen, (255, 255, 255), (0, 200, 900, 30))
                    else:
                        answer += event.unicode
            if answer != '':
                answer_text = font.render(answer, True, (0, 10, 0))
                screen.blit(answer_text, [10, 200])
            pygame.display.flip()
            clock.tick(20)


class Questioner_3:
    def start_screen():
        global running, screen, size, mode, wasted, wasted_running, dyno
        global questions_mode3, start_running, running, player_sprites, hp, sprite, image
        global pause, rules_running, enemy_sprites, up, down, \
            updelta, downdelta, y_speed, x_speed
        screen.fill((100, 100, 200))
        intro_text = ['Вы проиграли!', 'Найдите, сколько различных решений имеет уравнение:']
        question = random.sample(questions_mode3.items(), 1)
        main_text = ['В главное меню']
        fon = pygame.transform.scale(load_image('rules_fon.jpg'), (700, 450))
        screen.blit(fon, (0, 0))
        font = pygame.font.SysFont('verdana', 20)
        text_coord = 30
        for line in intro_text:
            string_rendered = font.render(line, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        font = pygame.font.Font(None, 27)
        text = font.render(question[0][0], True, (255, 255, 255))
        screen.blit(text, [10, 150])
        answer = ''
        pygame.draw.rect(screen, (255, 255, 255), (0, 200, 900, 30))
        font = pygame.font.SysFont('serif', 25)
        text_coord = 30
        for line in main_text:
            string_rendered = font.render(line, 1, (255, 255, 255))
            intro_rect = string_rendered.get_rect()
            intro_rect.top = 300
            intro_rect.x = 10
            print(intro_rect)
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        while wasted_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start_running = False
                    running = False
                    wasted_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if (event.pos[0] > 10 and event.pos[0] < 178 and
                            event.pos[1] > 300 and event.pos[1] < 329):
                        running = True
                        start_running = True
                        wasted_running = False
                        wasted = False
                        mode = -1
                        hp = 100
                        player_sprites = pygame.sprite.Group()
                        sprite = pygame.sprite.Sprite()
                        image = pygame.transform.scale(load_image("dyno_running.png"), (150, 80))
                        dyno = AnimatedSprite(image, 2, 1, 50, 50)
                        dyno.rect = dyno.image.get_rect()
                        player_sprites.add(dyno)
                        dyno.rect.x = 5
                        dyno.rect.y = 150
                        pause = 0
                        y_speed = 0
                        x_speed = 0
                        wasted = False
                        rules_running = False
                        enemy_sprites = pygame.sprite.Group()
                        for _ in range(10):
                            sprite = pygame.sprite.Sprite()
                            sprite.image = pygame.transform.scale(load_image("2.png"), (50, 50))
                            sprite.rect = sprite.image.get_rect()
                            sprite.rect.x = random.randrange(0, 700)
                            sprite.rect.y = random.randrange(0, 700)
                            enemy_sprites.add(sprite)

                        up = False
                        down = False
                        updelta = 10
                        downdelta = -10
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if answer != question[0][1]:
                            start_running = False
                            running = False
                            wasted_running = False
                        else:
                            hp = 100
                            running = True
                            wasted_running = False
                            wasted = False
                    elif event.key == pygame.K_BACKSPACE:
                        answer = answer[:-1]
                        pygame.draw.rect(screen, (255, 255, 255), (0, 200, 900, 30))
                    else:
                        answer += event.unicode
            if answer != '':
                answer_text = font.render(answer, True, (0, 10, 0))
                screen.blit(answer_text, [10, 200])
            pygame.display.flip()
            clock.tick(20)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(player_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


def main_cycle():
    global up, down, updelta, downdelta, running, dyno, y_speed, \
        x_speed, hp, mode, wasted, wasted_running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: x_speed = -10
            if event.key == pygame.K_RIGHT: x_speed = 10
            if event.key == pygame.K_UP: y_speed = -10
            if event.key == pygame.K_DOWN: y_speed = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: x_speed = 0
            if event.key == pygame.K_RIGHT: x_speed = 0
            if event.key == pygame.K_UP: y_speed = 0
            if event.key == pygame.K_DOWN: y_speed = 0
    hits_array = pygame.sprite.spritecollide(dyno, enemy_sprites, False)
    if len(hits_array) > 0:
        hp -= len(hits_array)
    if (hp < 1):
        wasted = True
        wasted_running = True
        # pygame.quit()
        # running = False
        # sys.exit(0)
    for i in enemy_sprites:
        i.rect.x -= 10
        if (i.rect.x < 0 or i.rect.y < 0):
            i.rect.x = width - 1
            i.rect.y = random.randrange(0, 600)
    dyno.rect.x += x_speed
    dyno.rect.y += y_speed
    print(x_speed, y_speed)
    if dyno.rect.x < 0:
        dyno.rect.x = 0
    if dyno.rect.x > 600:
        dyno.rect.x = 600
    if dyno.rect.y < 0:
        dyno.rect.y = 0
    if dyno.rect.y > 310:
        dyno.rect.y = 310

    screen.blit(pygame.transform.scale(second_fon, (700, 400)), (0, 0))
    # tiles_group.draw(screen)
    enemy_sprites.draw(screen)
    player_sprites.draw(screen)
    dyno.update()
    font = pygame.font.Font(None, 25)
    text = font.render("Жизнь " + str(hp), True, (255, 255, 255))
    screen.blit(text, [10, 10])
    pygame.display.flip()
    clock.tick(20)


player_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
image = pygame.transform.scale(load_image("dyno_running.png"), (150, 80))
dyno = AnimatedSprite(image, 2, 1, 50, 50)
dyno.rect = dyno.image.get_rect()
player_sprites.add(dyno)
dyno.rect.x = 5
dyno.rect.y = 150
pause = 0
y_speed = 0
x_speed = 0
wasted = False
rules_running = False
enemy_sprites = pygame.sprite.Group()
second_fon = load_image('second_fon.png')
for _ in range(10):
    sprite = pygame.sprite.Sprite()
    sprite.image = pygame.transform.scale(load_image("2.png"), (50, 50))
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = random.randrange(0, 700)
    sprite.rect.y = random.randrange(0, 700)
    enemy_sprites.add(sprite)

up = False
down = False
updelta = 10
downdelta = -10

while running:
    if start_running:
        MainMenu.start_screen()
    elif rules_running:
        Rules.start_screen()
    elif wasted:
        if mode == 0:
            Questioner_1.start_screen()
        elif mode == 1:
            Questioner_2.start_screen()
        elif mode == 2:
            Questioner_3.start_screen()
    else:
        main_cycle()
pygame.quit()
