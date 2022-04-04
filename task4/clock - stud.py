import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
from matplotlib.animation import FuncAnimation
from core import *

class Digits:

    digits=\
    np.array([
        # zero
        [[159.0, 84.0, 123.0, 158.0, 131.0, 258.0],
        [139.0, 358.0, 167.0, 445.0, 256.0, 446.0],
        [345.0, 447.0, 369.0, 349.0, 369.0, 275.0],
        [369.0, 201.0, 365.0, 81.0, 231.0, 75.0]],
        # one
        [[226.0, 99.0, 230.0, 58.0, 243.0, 43.0],
        [256.0, 28.0, 252.0, 100.0, 253.0, 167.0],
        [254.0, 234.0, 254.0, 194.0, 255.0, 303.0],
        [256.0, 412.0, 254.0, 361.0, 255.0, 424.0]],
        # two
        [[152.0, 55.0, 208.0, 26.0, 271.0, 50.0],
        [334.0, 74.0, 360.0, 159.0, 336.0, 241.0],
        [312.0, 323.0, 136.0, 454.0, 120.0, 405.0],
        [104.0, 356.0, 327.0, 393.0, 373.0, 414.0]],
        # three
        [[113.0, 14.0, 267.0, 17.0, 311.0, 107.0],
        [355.0, 197.0, 190.0, 285.0, 182.0, 250.0],
        [174.0, 215.0, 396.0, 273.0, 338.0, 388.0],
        [280.0, 503.0, 110.0, 445.0, 93.0, 391.0]],
        # four
        [[249.0, 230.0, 192.0, 234.0, 131.0, 239.0],
        [70.0, 244.0, 142.0, 138.0, 192.0, 84.0],
        [242.0, 30.0, 283.0, -30.0, 260.0, 108.0],
        [237.0, 246.0, 246.0, 435.0, 247.0, 438.0]],
        # five
        [[226.0, 42.0, 153.0, 44.0, 144.0, 61.0],
        [135.0, 78.0, 145.0, 203.0, 152.0, 223.0],
        [159.0, 243.0, 351.0, 165.0, 361.0, 302.0],
        [371.0, 439.0, 262.0, 452.0, 147.0, 409.0]],
        # six
        [[191.0, 104.0, 160.0, 224.0, 149.0, 296.0],
        [138.0, 368.0, 163.0, 451.0, 242.0, 458.0],
        [321.0, 465.0, 367.0, 402.0, 348.0, 321.0],
        [329.0, 240.0, 220.0, 243.0, 168.0, 285.0]],
        # seven
        [[168.0, 34.0, 245.0, 42.0, 312.0, 38.0],
        [379.0, 34.0, 305.0, 145.0, 294.0, 166.0],
        [283.0, 187.0, 243.0, 267.0, 231.0, 295.0],
        [219.0, 323.0, 200.0, 388.0, 198.0, 452.0]],
        # eight
        [[336.0, 184.0, 353.0, 52.0, 240.0, 43.0],
        [127.0, 34.0, 143.0, 215.0, 225.0, 247.0],
        [307.0, 279.0, 403.0, 427.0, 248.0, 432.0],
        [93.0, 437.0, 124.0, 304.0, 217.0, 255.0]],
        # nine
        [[323.0, 6.0, 171.0, 33.0, 151.0, 85.0],
        [131.0, 137.0, 161.0, 184.0, 219.0, 190.0],
        [277.0, 196.0, 346.0, 149.0, 322.0, 122.0],
        [298.0, 95.0, 297.0, 365.0, 297.0, 448.0]]

    ])
    end_points=\
    np.array([
        # zero
        [254, 47],
        # one
        [138, 180],
        # two
        [104, 111],
        # three
        [96, 132],
        # four
        [374, 244],
        # five
        [340, 52],
        # six
        [301, 26],
        # seven
        [108, 52],
        # eight
        [243,242],
        # nine
        [322, 105]
    ]).astype(float)
    def __init__(self):
        pass
    def get_coords(self, digit):
        return self.digits[digit]


    def get_end_point(self, digit): #
        return self.end_points[digit]

class Clock:

    def __init__(self, anim_speed=20):
        self.anim_speed=anim_speed
        self.finish=False
        self.Digits=Digits()
        self.fig, self.ax = plt.subplots()
        self.fig.suptitle("Clock")
        self.img = np.zeros((512,512,3), dtype=np.uint8)
        self.blank = np.zeros((512,512,3), dtype=np.uint8)
        self.im = plt.imshow(self.img, animated=True)

        # cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)

        self.ani = FuncAnimation(self.fig, self.plot_digit, init_func=self.init_anim, frames=self.end_clock, blit=True, interval=50)
        plt.show()

    def end_clock(self):
        ii = 0
        while not self.finish:
            ii += 1
            yield ii

    def init_anim(self, digit=0):
        self.cur_digit = digit
        self.cur_step = 0
        #TODO достать координаты цифры
        self.current_coordd_points = self.Digits.get_coords(digit).copy()
        self.current_coordd_end_points = self.Digits.get_end_point(digit).copy()
        #TODO задать смещения для выбранной скорости анимации

        if self.cur_digit == 9:
            delta_digit = self.Digits.get_coords(0) - self.Digits.get_coords(9)
            delta_end_point = self.Digits.get_end_point(0) - self.Digits.get_end_point(9)
        else:
            delta_digit = self.Digits.get_coords(digit + 1) - self.Digits.get_coords(digit)
            delta_end_point = self.Digits.get_end_point(digit + 1) - self.Digits.get_end_point(digit)

        self.delta_step_points = delta_digit / self.anim_speed
        self.delta_step_end_points = delta_end_point / self.anim_speed

        return self.im,

    def onclick(self, event):
        self.finish=not self.finish

    def plot_digit(self, par):

        if self.cur_step==self.anim_speed:
            #TODO сменить цифру - вызов init_anim
            if self.cur_digit == 9:
                self.cur_digit = 0
            else:
                self.cur_digit += 1
            self.init_anim(self.cur_digit)
            return self.im,
        else:
            self.img=self.blank.copy()


            for i in range(3, -1, -1):
                points = []
                if i != 0:
                    points.extend(self.current_coordd_points[i-1][4:6])
                else:
                    points.extend(self.current_coordd_end_points)
                # print(self.current_coordd_points[i])
                points.extend(self.current_coordd_points[i])
                # print(points)
                self.img = de_CastelJoJo_splain(self.img, points)
                pass

            #TODO достать текущие координаты, запустить алгоритм Кастельжо, нарисовать апроксимацию кривой Безье
            #TODO с помощью draw line
            self.im.set_array(np.fliplr(np.rot90(self.img, k = 3)))
            self.cur_step+=1
            #TODO обновить текущие координаты

            self.current_coordd_points += self.delta_step_points
            self.current_coordd_end_points += self.delta_step_end_points

            return self.im,



clock=Clock()



