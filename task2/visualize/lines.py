import numpy as np


def bad_line(img, x0, y0, x1, y1):
    for t in np.linspace(0, 1, 100):  # фор от 0 до 1 (100 шт)
        x = t * x0 + (1 - t) * x1
        y = t * y0 + (1 - t) * y1
        x = int(round(x))
        y = int(round(y))
        img[x, y] = 255


def bad_line2(img, x0, y0, x1, y1):
    for x in range(x0, x1 + 1):
        t = (x - x1) / (x0 - x1)
        y = t * y0 + (1 - t) * y1
        # x = int(round(x)) #x уже целочисленный
        y = int(round(y))
        img[x, y] = 255


def bad_line3(img, x0, y0, x1, y1):
    steep = False
    if abs(x1 - x0) < abs(y0 - y1):
        x0, y0, x1, y1 = y0, x0, y1, x1
        steep = True
    if x1 < x0:
        x1, x0 = x0, x1
        y1, y0 = y0, y1
    for x in range(x0, x1 + 1):
        t = (x - x1) / (x0 - x1)
        y = y0 * t + (1 - t) * y1
        if steep:
            img[int(round(y)), int(round(x))] = 255
        else:
            img[int(round(x)), int(round(y))] = 255
    return img


# tg k = abs(y0-y1)/abs(x1-x0)
# error = 0


def bresenham_line_algorithm(img, x0, y0, x1, y1):
    steep = False
    if abs(x1 - x0) < abs(y0 - y1):
        x0, y0, x1, y1 = y0, x0, y1, x1
        steep = True
    if x1 < x0:
        x1, x0 = x0, x1
        y1, y0 = y0, y1

    dx = x1 - x0
    dy = y1 - y0
    y = y0
    error = 0
    tgk = dy / dx

    for x in range(x0, x1 + 1):
        if steep:
            img[y, x] = 255
        else:
            img[x, y] = 255

        error += tgk
        if error >= 0.5:
            y += 1
            error -= 1

    return img



def integer_bresenham_line_algorithm(img, x0, y0, x1, y1):

    steep = False
    if abs(x1 - x0) < abs(y0 - y1):
        x0, y0, x1, y1 = y0, x0, y1, x1
        steep = True
    if x1 < x0:
        x1, x0 = x0, x1
        y1, y0 = y0, y1

    dx = x1 - x0
    dy = abs(y1 - y0)
    y = y0
    error = 0
    tgk = dy #умножаю всё на dx, чтоб не было деления, а также на 2, чтоб избавиться от вещетвенных чисел

    diry = y1 - y0

    if diry > 0:
        diry = 1
    if diry < 0:
        diry = -1

    for x in range(x0, x1+1):
        if steep:
            img[y, x] = 255
        else:
            img[x, y] = 255

        error += tgk
        if 2 * error >= dx:
            y += diry
            error -= dx

    return img



# tg k = abs(y0-y1)/abs(x1-x0)
# error = 0