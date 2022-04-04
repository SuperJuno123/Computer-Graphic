
def read_v1(path_file):
    # Первый вариант: первый раз прохожу по файлу и подсчитываю количество кол-во координат, чтобы потом создать
    # массив нампай нужного размера. Далее заполняю данный массив координатами из файла. Недостатки: требуется 2 прохода


    f = open(path_file, 'r')
    file: str = f.readlines()

    import numpy as np

    number_of_str = 0
    for line in file:
        if line[0] == "v" and line[1] == " ": #нам нужны только обычные вершины (v). Кроме вершин, бывают vt, vn, vp...
            number_of_str += 1
            # Они не используются в данной программе

    vertex = np.zeros(shape=(number_of_str, 2))

    count = 0
    for line in file:
        if line[0] == "v" and line[1] == " ":

            splitted_line = line.replace('v', '').lstrip(' ').split(' ') # работаю со строкой, из которой удалена 'v'
            # Удаляю лишние пробелы в начале (слева), затем разделяю на отдельные подстроки, каждая из которых - значение координаты
            vertex[count, 0] = float(splitted_line[0])  # x
            vertex[count, 1] = float(splitted_line[1])  # y
            count += 1
    vertex = np.around(vertex).astype(np.int64)
    return vertex


def read_f(path_file):
    # Первый вариант: первый раз прохожу по файлу и подсчитываю количество кол-во координат, чтобы потом создать
    # массив нампай нужного размера. Далее заполняю данный массив координатами из файла. Недостатки: требуется 2 прохода

    char = 'f'

    f = open(path_file, 'r')
    file: str = f.readlines()

    import numpy as np

    number_of_str = 0
    for line in file:
        if line[0] == char and line[1] == " ":
            number_of_str += 1

    vertex_indices = np.zeros(shape=(number_of_str, 3))

    count = 0
    for line in file:
        if line[0] == char and line[1] == " ":

            splitted_line = line.replace(char, '').lstrip(' ').split(' ') # работаю со строкой, из которой удалена 'f'
            # Удаляю лишние пробелы в начале (слева), затем разделяю на отдельные подстроки, каждая из которых - значение координаты

            if len(splitted_line) > 3: #в данном случае работаю только с треугольниками, если у полигона больше точек, чем 3 - игнорирую
                continue

            for i in range(0, 3):
                buff = splitted_line[i]
                buff = buff[:buff.find("/")]
                vertex_indices[count, i] = buff
            #
            # vertex_indices[count, 0] = float(splitted_line[0])
            # vertex_indices[count, 1] = float(splitted_line[1])
            # vertex_indices[count, 2] = float(splitted_line[2])
            count += 1

    vertex_indices = np.around(vertex_indices).astype(np.int64)
    return vertex_indices


