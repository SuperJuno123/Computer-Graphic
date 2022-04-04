
from matplotlib.animation import FuncAnimation
import time
from core import *




#класс игры
class Game:


    def __init__(self, pic_size = 512):
        # сохранили параметр как поле класса
        self.pic_size=pic_size
        # проверяет нужно ли завершить игру
        self.finish = False
        # готовит окна
        self.fig, self.ax = plt.subplots()
        self.fig.suptitle("Game")
        # TODO считать вершины и грани. Адаптировать размер вершин

        self.color = (255, 255, 255)
        self.multiply = 1

        self.speed_counter = 0
        self.size_counter = 0
        self.speed_counter2 = 0
        self.deceleration_rate = 0.1 # скорость замедления вращения чайника

        import os
        path = os.getcwd() + "\\small_teapot.obj"
        from input_output import input_output
        self.vertexes = input_output.read_v1(path)
        self.poly = input_output.read_f(path)
        from geometry import scaling
        self.teapot_size = pic_size / 20
        import math
        self.teapot_diagonal = self.teapot_size * math.sqrt(2)
        self.vertexes = scaling.scaling(self.vertexes, self.teapot_size)

        self.vertexes = vertexes_to_projective(self.vertexes)

        angle_of_rotate = 20
        a = np.pi * angle_of_rotate / 180
        self.R = np.array([[np.cos(a), -np.sin(a), 0], [np.sin(a), np.cos(a), 0], [0, 0, 1]])  # матрица пооворота

        pass

        print("123")
        # Обработчик на клик мышкой-выстрел
        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        # подготовка изображения-массива
        self.img = np.zeros((pic_size,pic_size,3), dtype=np.uint8)
        # визуализация с анимацией
        self.im = plt.imshow(self.img, animated=True)
        # запуск анимации
        # self.fig - окно для анимации
        # self.update - функция отрисовки каждого кадра
        # self.init_target - функция, которая отработает перед запуском анимациии
        # self.end_game - функция-обман для matplotlib. Matplotlib требует точного количества кадров для завершения анимации. Мы же сделаем бесконечный генератор.
        # interval - количество миллисекунд, после которых снова вызывается функция self.update
        self.ani = FuncAnimation(self.fig, self.update, init_func=self.init_target, frames=self.end_game, blit=True, interval=5)
        plt.show()

    #остановит игру
    def end_game(self):
        i = 0
        while not self.finish:
            i += 1
            yield i

    #функция инициализациии полета
    def init_target(self, x0=0, y0=None, alpha=None, v0=None):
        """
        Эмулирует полёт под углом к горизонту с ускорением свободного падения
        :param x0: стартовая координата x тела
        :param y0: стартовая координата y тела
        :param alpha: угол в градусах по отношению к горизонту
        :param v0: начальная скорость
        :return:
        """

        # Обнулили поле
        self.img = np.zeros((self.pic_size, self.pic_size, 3), dtype=np.uint8)


        # Если в функцию не передали такой параметр, генерируем случаную координату y
        if y0 is None:
            y0 = np.random.randint(0, self.pic_size)
        # то же самое с углом
        if alpha is None:
            alpha = np.deg2rad(np.random.randint(-50, -20))
        # и со скоростью
        if v0 is None:
            v0 = np.random.randint(20, 50)
        # фиксируем начальное время - оно понадобится для вычисленния новых координат
        self.t = time.time()
        self.v0 = v0
        self.x0 = x0
        self.y0 = y0
        self.alpha = alpha
        # неземное ускорение свободного падения
        self.g = 3 * 9.8
        # начальные проекции скоростей
        self.vx = self.v0 * np.cos(self.alpha)
        self.vy = self.v0 * np.sin(self.alpha)
        return self.im,

    # функция отрисовки
    def update(self, par):
        # посмотрели сколько прошло времени с момента запуска снаряда
        cur_t = time.time() - self.t
        # пересчитали положение снаряда
        cur_x = self.x0 + self.v0 * cur_t * np.cos(self.alpha)
        cur_y = self.y0 + self.v0 * cur_t * np.sin(self.alpha) - self.g * cur_t * cur_t / 2

        # сразу здесь меняю координаты, чтоб потом проверить, не сбежали ли они за пределы листа

        if self.size_counter != 0 and self.size_counter % 2 == 0:
            self.multiply = self.multiply * 2
            self.size_counter = 0

        if self.speed_counter > self.speed_counter2:
            self.rotate_teapot()
            self.speed_counter2 += self.deceleration_rate
            self.speed_counter = 0
        self.speed_counter += 1

        # если вышли за вертикальные пределы изображения или каким-то образом влево - проиграли
        # TODO закончить условие проигрыша
        if cur_x < 0 or cur_y < 0 or cur_y + self.teapot_diagonal*self.multiply >= self.pic_size or cur_x + self.teapot_diagonal*self.multiply >= self.pic_size:
            self.multiply = 1
            # ВНИМАНИЕ! ЗДЕСЬ МОЖНО ВЫКЛЮЧИТЬ РАЗНОЦВЕТНОСТЬ
            self.color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
            self.init_target()
            # self.finish=True
            return self.im,
        # # если просто вышли за пределы правой части экрана - запускам новый снаряд
        # if cur_x >= self.pic_size:
        #     self.init_target()
        #     return self.im,
        self.last_x=int(cur_x)
        self.last_y=int(cur_y)
        # TODO отрисовка чайника, летящего по параболической траектории и прочие плюшки (о них ниже)
        pass


        self.img = np.zeros((self.pic_size, self.pic_size, 3), dtype=np.uint8) #не буду рисовать след от чайника, слишком грязно выходит


        # self.draw_teapot() #рисование по точкам
        self.raster_teapot() #растеризация как в задании №2

        # рисуем снаряд
        self.img[self.last_x, self.last_y] = (255, 0, 0)
        self.img[self.last_x + int(self.teapot_size*self.multiply), self.last_y + int(self.teapot_size*self.multiply)] = (255, 0, 0)


        # запомнили скорости текущие
        self.vx = self.v0 * np.cos(self.alpha)
        self.vy = self.v0 * np.sin(self.alpha) - self.g * cur_t

        #обновили буфер отрисовки
        self.im.set_array(np.rot90(self.img))
        return self.im,

    def rotate_teapot(self):
        pass
        self.vertexes[:, :] = (self.vertexes[:, :] - int(self.teapot_size / 2)) #центрирование
        self.vertexes = np.round(self.R.dot(self.vertexes.T).T).astype(int)
        self.vertexes[:, :] = (self.vertexes[:, :] + int(self.teapot_size / 2)) #центрирование

    def draw_teapot(self):
        for i in range(0, self.vertexes.shape[0]):
            x0 = int(round(self.last_x + self.vertexes[i, 0] * self.multiply))
            y0 = int(round(self.last_y + self.vertexes[i, 1] * self.multiply))
            self.img[x0, y0] = self.color

    def raster_teapot(self):
        from visualize import show
        show.create_polygons(self.img, np.around(self.vertexes).astype(np.int64) * self.multiply, self.poly, self.last_x, self.last_y, self.color)



    # функция выстрела
    def onclick(self, event):
        # задали размер хитбокса
        heat_box = self.teapot_size*self.multiply
        # вывели дебаг информацию
        print(self.last_x, self.last_y, event.xdata, event.ydata, self.vx, self.vy)
        # Если кликнули в место, где сейчас летит снаряд
        if self.last_x - heat_box < event.xdata and event.xdata < self.last_x + heat_box and \
                self.pic_size-self.last_y - heat_box < event.ydata and event.ydata < self.pic_size-self.last_y + heat_box:
            # придать ему доп скорость и подкинуть от текущего положения
            #TODO также заставить чайник вращаться, чайник должен вращаться быстро, а спустя некторое время замедлять вращение и вовсе его прекращать
            #TODO после второго попадания по тому же чайнику, увеличить его размер в два раза, сохранив текущую ориентацию вращения
            self.init_target(self.last_x, self.last_y, np.deg2rad(45), self.v0 + np.abs(self.vx))
            self.size_counter += 1
            self.speed_counter = 0
            self.speed_counter2 = 0


gg=Game()
