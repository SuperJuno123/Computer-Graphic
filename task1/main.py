#Программа совершает 3 основных действия, которые выполняются в трех разных модулях. В своей программе
#я сделала функции внутри модулей и обращаюсь к ним. В случае, если мне понадобятся различные варианты одних и тех же
#действий, я просто смогу добавить новые функции в этот же модуль

size_of_img = 512

import os
path = os.getcwd() + "\\task1.obj"

import input_output.read

vertex_arr = input_output.read.read_obj_var1(path)
vertex_arr = input_output.read.read_obj_var2(path)

import geometry.scaling
vertex_arr = geometry.scaling.scaling(vertex_arr, size_of_img) #обновляю координаты вершин (с учетом масштабирования)

import visualize.show
visualize.show.show_obj(vertex_arr, size_of_img)










#import numpy as np
#import matplotlib.pyplot as plt

#import PyWavefront
#scene = PyWavefront.Wavefront('something.obj')


# img_255 = np.zeros((512,512,3), dtype=np.uint8) #целочисленный массив
# img_1 = np.zeros((512,512,3)) #действительный массив
# #Покрасить пиксель с координатами x,y в белый цвет можно следующим образом:
# img_255[66,66]=(255,255,255)
# img_1[66,66]=(1,1,1)
# #Числа в кортеже соответствуют цветам RGB модели, в первом случае в целочисленном представлении, во втором в действительном.
# #Непосредственная визуализация изображения осуществляется следующим
# #образом:
# plt.imshow(img_255) # или plt.imshow(img_1)
# plt.show()
