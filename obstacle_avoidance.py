import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
from itertools import product, combinations
import random

plt.close('all')

# Drone parameter
start_x = 10
start_y = 50
f = np.linspace(0, 100, 200)
# Plot parameters
fig = plt.figure()
ax = plt.axes()
# 0 to 100 feet
ax.set_xlim([0, 140])
ax.set_xlabel('East (ft)')
ax.set_ylim([0, 100])
ax.set_ylabel('North (ft)')

ax.set_title('Amazon Drone Object Avoidance Simulation')

# fly in the middle
A = 40
X = np.arange(0, 100, 1)
Y = []
for i in range(20):
    Y.append(A)
avoidance = 25*np.sin(0.0638*X) + 40
avoid_lst = []
for i in range(len(avoidance)):
    Y.append(avoidance[i])
for i in range(20):
    Y.append(A)
    
X = np.arange(0, 140, 1)

# Initialize plotting variable for animation
traj, = ax.plot(X, Y, lw=2)
drone, = ax.plot(X, Y, 'ro')

def animate(i, traj, X, Y, drone):
    traj.set_data(X[i-20:i], Y[i-20:i])
    drone.set_data(X[i], Y[i])
    
    return traj, drone,

animation.FuncAnimation(fig, animate, fargs=(traj, X, Y, drone),
                           frames=len(Y), interval=50,
                           blit=True)
plt.show()