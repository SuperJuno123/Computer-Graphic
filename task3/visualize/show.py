
from visualize import lines


def create_polygons(img, vertexes, indices_of_v, dx, dy, color):
    for i in range(0, indices_of_v.shape[0]): #строим треугольники, попарно соединяю вершины
        #вершина первая + вторая
        lines.integer_bresenham_line_algorithm(img, x0=vertexes[indices_of_v[i, 0] - 1, 0] + dx,
                                           y0=vertexes[indices_of_v[i, 0] - 1, 1] + dy,
                                           x1=vertexes[indices_of_v[i, 1] - 1, 0] + dx,
                                           y1=vertexes[indices_of_v[i, 1] - 1, 1] + dy, color=color) #естественная нумерация переходит в неестественную
        # вершина вторая + третья
        lines.integer_bresenham_line_algorithm(img, x0=vertexes[indices_of_v[i, 1] - 1, 0] + dx,
                                           y0=vertexes[indices_of_v[i, 1] - 1, 1] + dy,
                                           x1=vertexes[indices_of_v[i, 2] - 1, 0] + dx,
                                           y1=vertexes[indices_of_v[i, 2] - 1, 1] + dy, color=color)
        # вершина первая + третья
        lines.integer_bresenham_line_algorithm(img, x0=vertexes[indices_of_v[i, 0] - 1, 0] + dx,
                                           y0=vertexes[indices_of_v[i, 0] - 1, 1] + dy,
                                           x1=vertexes[indices_of_v[i, 2] - 1, 0] + dx,
                                           y1=vertexes[indices_of_v[i, 2] - 1, 1] + dy, color=color)
    return img

