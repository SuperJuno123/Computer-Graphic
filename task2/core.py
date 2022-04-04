import numpy as np
import matplotlib.pyplot as plt

def prepare_image(pic_size):
    img = np.zeros(shape=(pic_size+1,pic_size+1)).astype(np.uint8)
    return img

def show_image(image):
    plt.imshow(image.T, cmap="gray")
    plt.show()