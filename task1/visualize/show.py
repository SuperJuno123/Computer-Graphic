
import matplotlib.pyplot as plt
import numpy as np

def show_obj(vertex, size_of_img):
    img_1 = np.ones((size_of_img + 1, size_of_img + 1, 3))

    vertex = np.around(vertex).astype(np.int64) #округление до ближайшего четного: работает так:
    #np.around([.5, 1.5, 2.5, 3.5, 4.5]) # rounds to nearest even value
    #array([0.,  2.,  2.,  4.,  4.])
    #в интернете написано, что the reason for the "nearest even number" rule is to reduce the overall error

    img_1[vertex[:, 0], vertex[:, 1]] = (0, 0, 0)

    img_1 = np.rot90(img_1)

    plt.imshow(img_1)

    plt.show()
