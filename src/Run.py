# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 12:22:00 2017

@author: Syrine Belakaria
"""
import network3
from network3 import Network
from network3 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer
from network3 import ReLU
from network3 import sigmoid
import numpy as np
import matplotlib.pyplot as plt

expanded_training_data, validation_data, test_data = network3.load_data_shared("../data/quickdraw_expanded.pkl.gz")
mini_batch_size = 10
net = Network([
        ConvPoolLayer(image_shape=(mini_batch_size, 1, 28, 28),filter_shape=(20, 1, 5, 5),poolsize=(2, 2)),
        ConvPoolLayer(image_shape=(mini_batch_size, 20, 12, 12),filter_shape=(40, 20, 3, 3),poolsize=(2, 2)),
        FullyConnectedLayer(n_in=40*5*5, n_out=500, activation_fn=sigmoid, p_dropout=0.1),
        FullyConnectedLayer(n_in=500, n_out=500, activation_fn=sigmoid, p_dropout=0.1),
        SoftmaxLayer(n_in=500, n_out=10, p_dropout=0.1)], mini_batch_size)
net.SGD(expanded_training_data, 70, mini_batch_size, 0.01,validation_data, test_data)
####Plot the weights of first layer
weights0=np.load("/home/syrine92/Syrine_Belakaria/weights0.npy")
i=-1
fig, ax = plt.subplots(nrows=4, ncols=5)
for row in ax:
    for col in row:
        col.axes.get_xaxis().set_visible(False)
        col.axes.get_yaxis().set_visible(False)
        i=i+1
        col.imshow(weights0[i][0],cmap='Greys')
fig.savefig('/home/syrine92/Syrine_Belakaria/weights0.png')
####Plot the weights of second layer
weights1=np.load("/home/syrine92/Syrine_Belakaria/weights1.npy")
i=-1
fig, ax = plt.subplots(nrows=5, ncols=8)
for row in ax:
    for col in row:
        col.axes.get_xaxis().set_visible(False)
        col.axes.get_yaxis().set_visible(False)
        i=i+1
        col.imshow(weights1[i][0],cmap='Greys')
fig.savefig('/home/syrine92/Syrine_Belakaria/weights1.png')
