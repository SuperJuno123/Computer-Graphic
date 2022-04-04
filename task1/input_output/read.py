# чтобы не считывать координаты из файла два раза (в модуле скэлинг и шоу), я верну из этой функции сразу координаты (массив вершин x и y)

def read_obj_var1(path_file):
    # Первый вариант: первый раз прохожу по файлу и подсчитываю количество кол-во координат, чтобы потом создать
    # массив нампай нужного размера. Далее заполняю данный массив координатами из файла. Недостатки: требуется 2 прохода


    f = open(path_file, 'r')
    file: str = f.readlines()

    import numpy as np

    number_of_str = 0
    for line in file:
        if line[0] == "v" and line[1] == " ": #нам нужны только обычные вершины (v). Кроме вершин, бывают vt, vn, vp...
            # Они не используются в данной программе
            number_of_str += 1

    vertex = np.zeros(shape=(number_of_str, 2))

    count = 0
    for line in file:
        if line[0] == "v" and line[1] == " ":

            splitted_line = line.replace('v', '').lstrip(' ').split(' ') # работаю со строкой, из которой удалена 'v'
            # Удаляю лишние пробелы в начале (слева), затем разделяю на отдельные подстроки, каждая из которых - значение координаты
            vertex[count, 0] = float(splitted_line[0])  # x
            vertex[count, 1] = float(splitted_line[1])  # y
            count += 1


    return vertex

def read_obj_var2(path_file):

    # Второй вариант: создаю список, добавляю в него вершины по мере продвижения по файлу, потом получившийся список
    # преобразовываю в массив numpy.

    f = open(path_file, 'r')
    file: str = f.readlines()

    vertex_x: list = []
    vertex_y: list = []

    for line in file:
        if line[0] == "v" and line[1] == " ":
            splitted_line = line.replace('v', '').lstrip(' ').split(' ')
            vertex_x.append(float(splitted_line[0]))
            vertex_y.append(float(splitted_line[1]))

    import numpy as np

    vertex = np.array((vertex_y, vertex_x))
    vertex = np.rot90(vertex, k = -1) #Данные манипуляции проделаны для сохранения порядка координат
    #(если мы посмотрим в табличку, составленную из массива вертекс, она будет выглядеть как .obj файл

    return vertex




