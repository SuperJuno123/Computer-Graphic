
def scaling(vertex, size_of_img):
    import numpy as np

    max_x = np.max(vertex[:, 0])
    max_y = np.max(vertex[:, 1])

    min_x = np.min(vertex[:, 0])
    min_y = np.min(vertex[:, 1])

    coefficient = size_of_img / max(max_x - min_x, max_y - min_y)

    vertex[:, 0] = (vertex[:, 0] - min_x) * coefficient
    vertex[:, 1] = (vertex[:, 1] - min_y) * coefficient

    vertex = np.around(vertex).astype(np.int64)

    return vertex

