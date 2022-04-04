
from visualize import lines
#lines.integer_bresenham_line_algorithm(result, 10, 10, 10, 165)


def create_polygons(img, vertexes, indices_of_v):
    for i in range(0, indices_of_v.shape[0]): #строим треугольники, попарно соединяю вершины
        #вершина первая + вторая
        lines.integer_bresenham_line_algorithm(img, x0=vertexes[indices_of_v[i, 0] - 1, 0],
                                           y0=vertexes[indices_of_v[i, 0] - 1, 1],
                                           x1=vertexes[indices_of_v[i, 1] - 1, 0],
                                           y1=vertexes[indices_of_v[i, 1] - 1, 1]) #естественная нумерация переходит в неестественную
        # вершина вторая + третья
        lines.integer_bresenham_line_algorithm(img, x0=vertexes[indices_of_v[i, 1] - 1, 0],
                                           y0=vertexes[indices_of_v[i, 1] - 1, 1],
                                           x1=vertexes[indices_of_v[i, 2] - 1, 0],
                                           y1=vertexes[indices_of_v[i, 2] - 1, 1])
        # вершина первая + третья
        lines.integer_bresenham_line_algorithm(img, x0=vertexes[indices_of_v[i, 0] - 1, 0],
                                           y0=vertexes[indices_of_v[i, 0] - 1, 1],
                                           x1=vertexes[indices_of_v[i, 2] - 1, 0],
                                           y1=vertexes[indices_of_v[i, 2] - 1, 1])
    return img
