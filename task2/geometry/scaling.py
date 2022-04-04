
def scaling(vertex, size_of_img):
    import numpy as np

    max_x = np.max(vertex[:, 0])
    max_y = np.max(vertex[:, 1])

    min_x = np.min(vertex[:, 0])
    min_y = np.min(vertex[:, 1])

    #получаю переменные perenos, чтобы избавиться от координат, которые начинались бы не с нуля

    #perenos_x = -min_x
    #perenos_y = -min_y

    coefficient = size_of_img / max(max_x - min_x, max_y - min_y) #вычисляю коэффициент, на который умножу координаты из файла .obj

    vertex[:, 0] = (vertex[:, 0] - min_x) * coefficient
    vertex[:, 1] = (vertex[:, 1] - min_y) * coefficient

    return vertex



    #data_for_new_coordinates = [perenos_x, perenos_y, coefficient]
