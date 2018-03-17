# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:10:58 2017

@author: syrine belakaria
"""
import numpy as np
import matplotlib.pyplot as plt
#best_weights0= net.layers[0].w.eval()
#best_weights1= net.layers[1].w.eval()
#np.save("/home/syrine92/Quick_Draw_Project/weights0",best_weights0)
#np.save("/home/syrine92/Quick_Draw_Project/weights1",best_weights1)
weights0=np.load("weights0.npy")
i=-1
fig, ax = plt.subplots(nrows=4, ncols=5)
for row in ax:
    for col in row:
        col.axes.get_xaxis().set_visible(False)
        col.axes.get_yaxis().set_visible(False)
        i=i+1
        col.imshow(weights0[i][0],cmap='Greys')
fig.savefig('weights0.png')
weights1=np.load("weights1.npy")
i=-1
fig, ax = plt.subplots(nrows=5, ncols=8)
for row in ax:
    for col in row:
        col.axes.get_xaxis().set_visible(False)
        col.axes.get_yaxis().set_visible(False)
        i=i+1
        col.imshow(weights1[i][0],cmap='Greys')
fig.savefig('weights1.png')