
from core import *

size_of_img = 512

import os
path = os.getcwd() + "\\task1.obj"

import input_output.read

vertex_arr = input_output.read.read_v1(path)
indices_arr = input_output.read.read_f(path)

import geometry.scaling
vertex_arr = geometry.scaling.scaling(vertex_arr, size_of_img) #обновляю координаты вершин (с учетом масштабирования)

result = prepare_image(size_of_img)

import visualize.show
result = visualize.show.create_polygons(result, np.around(vertex_arr).astype(np.int64),  np.around(indices_arr).astype(np.int64))



#lines.integer_bresenham_line_algorithm(result, 10, 10, 10, 165)
show_image(np.rot90(result, k=2))
