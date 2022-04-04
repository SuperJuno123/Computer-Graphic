from core import *
import numpy as np

kv1_1=np.array([200,200])
kv1_3=np.array([400,200])
kv1_4=np.array([200,400])
kv2_2=np.array([200,200])
kv2_3=np.array([100,200])
kv2_4=np.array([200,100])
vertexes=np.array([kv1_1,kv1_3,kv1_4,kv2_2,kv2_3,kv2_4])
faces=np.array([[0,1,2],[3,4,5]])

alpha = -30
a = np.pi*alpha/180

R = np.array([[np.cos(a), -np.sin(a), 0], [np.sin(a), np.cos(a), 0], [0, 0, 1]])

vertexes = vertexes_to_projective(vertexes)

vertexes = np.round(R.dot(vertexes.T).T).astype(int)

image=prepare_image()
wireframe_render_float(image,vertexes,faces, 255)
show_image(image)