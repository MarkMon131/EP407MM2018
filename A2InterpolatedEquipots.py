"""
Name: A2InterpolatedEquipots.py
Author: Mark Monaghan
Date: 11/02/2018
Description: 2D interpolation of excel based electrostatic lens model
"""
#Imports
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as spl
import pandas as pnd

#Read in data from csv file
simArr = pnd.read_csv('equipots_EP407.csv')

#Assign x and y axes
X = np.linspace(0,23,24)
Y = np.linspace(2,12,12)

#generate meshgrid
x,y = np.meshgrid(X,Y)

#interpolate in quintic format
f = spl.interp2d(x,y,simArr,kind='quintic')

#rescale the simulation to mm resolution
Xnew = np.linspace(0,23,240)
Ynew = np.linspace(2,12,120)

#assign new array
hiRes = f(Xnew,Ynew)

#Plotting commands
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Simulated Equipotentials')
plt.imshow(hiRes)
ax.set_aspect('equal')
plt.colorbar(orientation='vertical')
plt.show()
