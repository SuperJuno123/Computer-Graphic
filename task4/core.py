import tkinter #Работа с GUI
import numpy as np #Работа с массивами
import matplotlib
import matplotlib.pyplot as plt #Вывод на экран
import random


root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# pic_size = 1200
pic_size = min(int(width/2), int(height/2))
# print ("Pic size: (%s,%s)" % (pic_size, pic_size))

def show_image(image):
    # plt.imshow(image, cmap="gray")
    # np.rot90(image)
    plt.imshow(image, cmap="gray", interpolation="none")
    plt.show()


def build_catmul_rom(vertexes, steps):
    pass


def build_ermit_spline(img, vertexes, derivatives, steps):
    for i in range(0, derivatives.size - 1):
        A = np.array([[vertexes[i, 0] ** 3, vertexes[i, 0] ** 2, vertexes[i, 0], 1],
                      [vertexes[i + 1, 0] ** 3, vertexes[i + 1, 0] ** 2, vertexes[i + 1, 0], 1],
                      [3 * vertexes[i, 0], 2 * vertexes[i, 0], 1, 0],
                      [3 * vertexes[i + 1, 0], 2 * vertexes[i + 1, 0], 1, 0]])

        b = np.array([[vertexes[i, 1]],
                      [vertexes[i + 1, 1]],
                      [derivatives[i]],
                      [derivatives[i + 1]]])

        X = np.linalg.inv(A) @ b

        print(X)
        print("\n")

        previous_y = vertexes[i, 1] #начальный y

        _args_x = np.linspace(vertexes[i, 0], vertexes[i + 1, 0], steps, retstep=True)
        step = _args_x[1]
        print(step)

        for xi in _args_x[0]:
            next_y = X[0, 0] * xi**3 + X[1, 0] * xi**2 + X[2, 0] * xi + X[3, 0]

            integer_bresenham_line_algorithm(img, int(round(xi*pic_size)), int(round(previous_y*pic_size)),
            int(round((xi+_args_x[1])*pic_size)), int(round(next_y*pic_size)), (255, 255, 255))
            # img[int(round(xi*pic_size)), int(round(y*pic_size))] = (255, 255, 255)
            previous_y = next_y
    return img



# см. http://grafika.me/node/521


def de_CastelJoJo_splain(img, points, step=100, color = (255, 255, 255)):

    # Подготовка
    points = np.reshape(points, (-1, 2))

    # # Контрольные линии (cyan)
    # for i in range(points.shape[0] - 1):
    #     integer_bresenham_line_algorithm(img, points[i][0], points[i][1], points[i+1][0], points[i+1][1], color=(0, 255, 255))
    #
    # # Контрольные точки (red)
    # for point in np.round(points).astype(int):
    #     img[tuple(point[:2])] = 255, 0, 0

    curve = []
    for t in np.linspace(0, 1, step):
        # Беру точку на расстоянии t и для нее рекурсивным алгоритмом ищу точку, принадлежащуюю кривой Безье
        point = de_CastelJoJo_R(points, t)
        _x, _y = [item for sublist in point for item in sublist]
        # img[int(round(_x)), int(round(_y))] = color
        curve.append([_x, _y])

    # Рисую кривую
    for i in range(len(curve) - 1):
        integer_bresenham_line_algorithm(img, curve[i][0], curve[i][1], curve[i+1][0], curve[i+1][1], color=color)

    return img


def de_CastelJoJo_R(points, t):
    if len(points) == 1: # Если осталась ровно она точка (x, y), происходит выход из рекурсии. Алгоритм вернёт эту точку
        return points

    new_points = []
    for i in range(len(points) - 1): # Вычисляю новые точки, которых будет меньше на одну.
        _x = t * (points[i + 1][0] - points[i][0]) + points[i][0]
        _y = t * (points[i + 1][1] - points[i][1]) + points[i][1]
        new_points.append([_x, _y])
    return de_CastelJoJo_R(new_points, t)



def prepare_image():
    img = np.zeros(shape=(pic_size+1,pic_size+1, 3)).astype(np.uint8)
    return img


def vertexes_renderer(img, vertexes, color):
    for vertex in vertexes:
        img[tuple(vertex[:2])]=color
    return img


def draw_line_bad_float(img, x0, y0, x1, y1, color):
    steep = False
    #если ширина меньше высоты
    if (abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        steep = True
    #если первая координата больше второй
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    for x in range(x0, x1+1):
        if x1==x0:
            t = 0
        else:
            t = (x-x0) / (x1-x0)
        y = int(round(y0 * (1.-t) + y1 * t))
        #поменяли координаты, при отрисовке меняем обратно
        if (steep):
            img[x, y] = color
        else:
            img[y, x] = color


def integer_bresenham_line_algorithm(img, x0, y0, x1, y1, color=(255, 255, 255)):

    x0 = int(round((x0)))
    x1 = int(round((x1)))

    y0 = int(round((y0)))
    y1 = int(round((y1)))

    steep = False
    # если ширина меньше высоты
    if (abs(x0 - x1) < abs(y0 - y1)):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        steep = True
    # если первая координата больше второй
    if (x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    deltax = abs(x1 - x0)
    deltay = abs(y1 - y0)
    error = 0
    deltaerr = deltay
    y = y0
    diry = y1 - y0

    if diry > 0:
        diry = 1
    if diry < 0:
        diry = -1
    for x in range(x0, x1 +1):
        if (steep):
            img[y, x] = color
        else:
            img[x, y] = color

        error = error + deltaerr
        if 2 * error >= deltax:
            y = y + diry
            error = error - deltax


    return img


if __name__=="__main__":
    print(width, height)
