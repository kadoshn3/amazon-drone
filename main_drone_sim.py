import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
from itertools import product, combinations
import random
from generate_trajectory import csv_2_df
import os

plt.close('all')

# Drone components
class Drone():
    def __init__(self, x, y):
        # Max and initial velocity (mph)
        self.max_vel = 100
        self.vel = 0
        self.descent_vel = 10
        # Max and initial altitude (ft)
        self.max_alt = 400
        self.alt_bounds = [200, 500]
        self.alt = 0
        
        # Positional starting coordinates dependent on position of warehouse
        self.x = x
        self.y = y
        self.z = 0

# Amazon Warehouse components
class Warehouse():
    def __init__(self):
        # Rectangular size [ft]
        self.length = 894
        self.width = 894
        self.height = 60
        
        # Positional coordinates
        self.x = 2000
        self.y = 2000
        self.z = 0

# Develop 3 piecewise trajectories of drone
#  1. Parabolic ascent from warehouse
#  2. In max altitutde remain in max altitude adjust x and y only
#  3. Once x and y coordinate home reached, descend z only
def get_traj(wh, home_coord, drone, num_traj):
    # Coordinate dimensionality
    #  Traj number (1 - number trajectories)
    #    List of coordinates
    #        X Y Z Coordinate
    traj = []
    # traj = [
    #         [ [traj1_x1, traj1_y1, traj1_z1],
    #           [traj1_x2, traj1_y2, traj1_z2],
    #           . . . 
    #           [traj1_xn, traj1_yn, traj1_zn] ],
    #           . . .
    #         [ [trajn_xn, trajn_yn, trajn_zn] ]
    #                                           ]
                
    # Compute distance away using distance formula to get number of data points
    distance_away = 0
    # X Y Z Dimensions
    num_dimensions = 3
    reached_destination_alt = True
    # Loop until trajectory is completed, once traj is populated go to next traj
    next_traj = False
    # Iterate to generate all trajectories
    for i in range(num_traj):
        while next_traj == False:
            j = 0
            for k in range(num_dimensions):
                # TODO: Compute iterable x y z drone position
                drone.x = 0
                drone.y = 0
                drone.z = 0
                
                if [drone.x, drone.y] == home_coord[i]:
                    reached_destination_alt = True
                # Store coordinate in matrix
                # X dimension
                if k == 0:
                    traj[i, j, k] = drone.x
                # Y dimension
                elif k == 1: 
                    traj[i, j, k] = drone.y
                # Z dimension
                elif k == 2: 
                    # Piecewise once max altitude is reached set that as max altitude
                    if drone.z > drone.max_alt:
                        drone.z = drone.max_alt
                    traj[i, j, k] = drone.z
                # If target is reached
                if reached_destination_alt:
                    drone.z -= drone.descent_vel
                    traj[i, j] = [home_coord[i][0], home_coord[i][1], drone.z] 
                    
                # Reached home and coordinate ground altitude, get next trajectory
                if drone.z == 0:
                    next_traj == True
                    
            # Add counter to while loop condition
            j += 1
                    
    return traj
    
# TODO: Try to generate cube to simulate the warehouse on the 3-D space 
#  using wh cooridnates and wh size

def warehouse_init(wh):
    num_bars = 1
    x_pos = wh.length
    y_pos = wh.width
    z_pos = 100
    x_size = np.ones(1000)
    y_size = np.ones(1000)
    z_size = wh.height
    
    ax.bar3d(x_pos, y_pos, z_pos, x_size, y_size, z_size, color='aqua')

class Obstacle():
	def __init__ (self, x, y, l, w):
		self.cx = x
		self.cy = y
		self.l = l
		self.w = w
        
def plotObst(O):
    i = 0
    for obst in O:
        box_x = [obst.cx - obst.l/2, obst.cx + obst.l/2, obst.cx + obst.l/2, obst.cx - obst.l/2, obst.cx - obst.l/2]
        box_y = [obst.cy - obst.w/2, obst.cy - obst.w/2, obst.cy + obst.w/2, obst.cy + obst.w/2, obst.cy - obst.w/2]
        if i == 0:
            plt.plot(box_x, box_y, 'b-', label='Warehouse')
        elif i == 1:
            plt.plot(box_x, box_y, 'g-', label='Forest')
        else:
            plt.plot(box_x, box_y, 'r-', label='No Fly Zone')
        i += 1
        
# Declares variables to be animated
def init():
    traj_0.set_data([], [])
    traj_0.set_3d_properties([])
    traj_1.set_data([], [])
    traj_1.set_3d_properties([])
    traj_2.set_data([], [])
    traj_2.set_3d_properties([])
    traj_3.set_data([], [])
    traj_3.set_3d_properties([])
    traj_4.set_data([], [])
    traj_4.set_3d_properties([])
    traj_5.set_data([], [])
    traj_5.set_3d_properties([])
    traj_6.set_data([], [])
    traj_6.set_3d_properties([])
    traj_7.set_data([], [])
    traj_7.set_3d_properties([])
    traj_8.set_data([], [])
    traj_8.set_3d_properties([])
    traj_9.set_data([], [])
    traj_9.set_3d_properties([])
    traj_10.set_data([], [])
    traj_10.set_3d_properties([])
    traj_11.set_data([], [])
    traj_11.set_3d_properties([])
    traj_12.set_data([], [])
    traj_12.set_3d_properties([])
    traj_13.set_data([], [])
    traj_13.set_3d_properties([])
    traj_14.set_data([], [])
    traj_14.set_3d_properties([])
    traj_15.set_data([], [])
    traj_15.set_3d_properties([])
    traj_16.set_data([], [])
    traj_16.set_3d_properties([])
    traj_17.set_data([], [])
    traj_17.set_3d_properties([])
    traj_18.set_data([], [])
    traj_18.set_3d_properties([])
    traj_19.set_data([], [])
    traj_19.set_3d_properties([])
    traj_20.set_data([], [])
    traj_20.set_3d_properties([])
    traj_21.set_data([], [])
    traj_21.set_3d_properties([])
    traj_22.set_data([], [])
    traj_22.set_3d_properties([])
    traj_23.set_data([], [])
    traj_23.set_3d_properties([])
    traj_24.set_data([], [])
    traj_24.set_3d_properties([])
    traj_25.set_data([], [])
    traj_25.set_3d_properties([])
    traj_26.set_data([], [])
    traj_26.set_3d_properties([])
    traj_27.set_data([], [])
    traj_27.set_3d_properties([])
    traj_28.set_data([], [])
    traj_28.set_3d_properties([])
    traj_29.set_data([], [])
    traj_29.set_3d_properties([])
    traj_30.set_data([], [])
    traj_30.set_3d_properties([])
    traj_31.set_data([], [])
    traj_31.set_3d_properties([])
    traj_32.set_data([], [])
    traj_32.set_3d_properties([])
    traj_33.set_data([], [])
    traj_33.set_3d_properties([])
    traj_34.set_data([], [])
    traj_34.set_3d_properties([])
    traj_35.set_data([], [])
    traj_35.set_3d_properties([])
    
    return traj_0, traj_1, traj_2, traj_3, traj_4, traj_5, \
            traj_6, traj_7, traj_8, traj_9, traj_10, traj_11, \
            traj_12, traj_13, traj_14, traj_15, traj_16, traj_17, \
            traj_18, traj_19, traj_20, traj_21, traj_22, traj_23, \
            traj_24, traj_25, traj_26, traj_27, traj_28, traj_29, \
            traj_30, traj_31, traj_32, traj_33, traj_34, traj_35, 

# Input trajectories to animate drone
def animate(i, traj_0, traj_1, traj_2, traj_3, traj_4, traj_5,
                traj_6, traj_7, traj_8, traj_9, traj_10, traj_11, 
                traj_12, traj_13, traj_14, traj_15, traj_16, traj_17,
                traj_18, traj_19, traj_20, traj_21, traj_22, traj_23,
                traj_24, traj_25, traj_26, traj_27, traj_28, traj_29,
                traj_30, traj_31, traj_32, traj_33, traj_34, traj_35,all_traj, N):
    traj_0.set_data(all_traj[0][:, 0][:i], all_traj[0][:, 1][:i])
    traj_0.set_3d_properties(all_traj[0][:, 2][:i])
    traj_1.set_data(all_traj[1][:, 0][:i], all_traj[1][:, 1][:i])
    traj_1.set_3d_properties(all_traj[1][:, 2][:i])
    traj_2.set_data(all_traj[2][:, 0][:i], all_traj[2][:, 1][:i])
    traj_2.set_3d_properties(all_traj[2][:, 2][:i])
    traj_3.set_data(all_traj[3][:, 0][:i], all_traj[3][:, 1][:i])
    traj_3.set_3d_properties(all_traj[3][:, 2][:i])
    traj_4.set_data(all_traj[4][:, 0][:i], all_traj[4][:, 1][:i])
    traj_4.set_3d_properties(all_traj[4][:, 2][:i])
    traj_5.set_data(all_traj[5][:, 0][:i], all_traj[5][:, 1][:i])
    traj_5.set_3d_properties(all_traj[5][:, 2][:i])
    traj_6.set_data(all_traj[6][:, 0][:i], all_traj[6][:, 1][:i])
    traj_6.set_3d_properties(all_traj[6][:, 2][:i])
    traj_7.set_data(all_traj[7][:, 0][:i], all_traj[7][:, 1][:i])
    traj_7.set_3d_properties(all_traj[7][:, 2][:i])
    traj_8.set_data(all_traj[8][:, 0][:i], all_traj[8][:, 1][:i])
    traj_8.set_3d_properties(all_traj[8][:, 2][:i])
    traj_9.set_data(all_traj[9][:, 0][:i], all_traj[9][:, 1][:i])
    traj_9.set_3d_properties(all_traj[9][:, 2][:i])
    traj_10.set_data(all_traj[10][:, 0][:i], all_traj[10][:, 1][:i])
    traj_10.set_3d_properties(all_traj[10][:, 2][:i])
    traj_11.set_data(all_traj[11][:, 0][:i], all_traj[11][:, 1][:i])
    traj_11.set_3d_properties(all_traj[11][:, 2][:i])
    traj_12.set_data(all_traj[12][:, 0][:i], all_traj[12][:, 1][:i])
    traj_12.set_3d_properties(all_traj[12][:, 2][:i])
    traj_13.set_data(all_traj[13][:, 0][:i], all_traj[13][:, 1][:i])
    traj_13.set_3d_properties(all_traj[13][:, 2][:i])
    traj_14.set_data(all_traj[14][:, 0][:i], all_traj[14][:, 1][:i])
    traj_14.set_3d_properties(all_traj[14][:, 2][:i])
    traj_15.set_data(all_traj[15][:, 0][:i], all_traj[15][:, 1][:i])
    traj_15.set_3d_properties(all_traj[15][:, 2][:i])
    traj_16.set_data(all_traj[16][:, 0][:i], all_traj[16][:, 1][:i])
    traj_16.set_3d_properties(all_traj[16][:, 2][:i])
    traj_17.set_data(all_traj[17][:, 0][:i], all_traj[17][:, 1][:i])
    traj_17.set_3d_properties(all_traj[17][:, 2][:i])
    traj_18.set_data(all_traj[18][:, 0][:i], all_traj[18][:, 1][:i])
    traj_18.set_3d_properties(all_traj[18][:, 2][:i])
    traj_19.set_data(all_traj[19][:, 0][:i], all_traj[19][:, 1][:i])
    traj_19.set_3d_properties(all_traj[19][:, 2][:i])
    traj_20.set_data(all_traj[20][:, 0][:i], all_traj[20][:, 1][:i])
    traj_20.set_3d_properties(all_traj[20][:, 2][:i])
    traj_21.set_data(all_traj[21][:, 0][:i], all_traj[21][:, 1][:i])
    traj_21.set_3d_properties(all_traj[21][:, 2][:i])
    traj_22.set_data(all_traj[22][:, 0][:i], all_traj[22][:, 1][:i])
    traj_22.set_3d_properties(all_traj[22][:, 2][:i])
    traj_23.set_data(all_traj[23][:, 0][:i], all_traj[23][:, 1][:i])
    traj_23.set_3d_properties(all_traj[23][:, 2][:i])
    traj_24.set_data(all_traj[24][:, 0][:i], all_traj[24][:, 1][:i])
    traj_24.set_3d_properties(all_traj[24][:, 2][:i])
    traj_25.set_data(all_traj[25][:, 0][:i], all_traj[25][:, 1][:i])
    traj_25.set_3d_properties(all_traj[25][:, 2][:i])
    traj_26.set_data(all_traj[26][:, 0][:i], all_traj[26][:, 1][:i])
    traj_26.set_3d_properties(all_traj[26][:, 2][:i])
    traj_27.set_data(all_traj[27][:, 0][:i], all_traj[27][:, 1][:i])
    traj_27.set_3d_properties(all_traj[27][:, 2][:i])
    traj_28.set_data(all_traj[28][:, 0][:i], all_traj[28][:, 1][:i])
    traj_28.set_3d_properties(all_traj[28][:, 2][:i])
    traj_29.set_data(all_traj[29][:, 0][:i], all_traj[29][:, 1][:i])
    traj_29.set_3d_properties(all_traj[29][:, 2][:i])
    traj_30.set_data(all_traj[30][:, 0][:i], all_traj[30][:, 1][:i])
    traj_30.set_3d_properties(all_traj[30][:, 2][:i])
    traj_31.set_data(all_traj[31][:, 0][:i], all_traj[31][:, 1][:i])
    traj_31.set_3d_properties(all_traj[31][:, 2][:i])
    traj_32.set_data(all_traj[32][:, 0][:i], all_traj[32][:, 1][:i])
    traj_32.set_3d_properties(all_traj[32][:, 2][:i])
    traj_33.set_data(all_traj[33][:, 0][:i], all_traj[33][:, 1][:i])
    traj_33.set_3d_properties(all_traj[33][:, 2][:i])
    traj_34.set_data(all_traj[34][:, 0][:i], all_traj[34][:, 1][:i])
    traj_34.set_3d_properties(all_traj[34][:, 2][:i])
    traj_35.set_data(all_traj[35][:, 0][:i], all_traj[35][:, 1][:i])
    traj_35.set_3d_properties(all_traj[35][:, 2][:i])
    #traj_.set_data(all_traj[][:, 0][:i], all_traj[][:, 1][:i])
    #traj_.set_3d_properties(all_traj[][:, 2][:i])

    
    return traj_0, traj_1, traj_2, traj_3, traj_4, traj_5, \
            traj_6, traj_7, traj_8, traj_9, traj_10, traj_11, \
            traj_12, traj_13, traj_14, traj_15, traj_16, traj_17, \
            traj_18, traj_19, traj_20, traj_21, traj_22, traj_23, \
            traj_24, traj_25, traj_26, traj_27, traj_28, traj_29, \
            traj_30, traj_31, traj_32, traj_33, traj_34, traj_35, 

if __name__=='__main__':
    # Get classes and assign to variables
    wh = Warehouse()
    drone = Drone(wh.x, wh.y)
    
    # Plot parameters
    fig = plt.figure()
    ax = p3.Axes3D(fig)
    # 0 to 5000 feet
    ax.set_xlim3d([0, 5000])
    ax.set_xlabel('East (ft)')
    ax.set_ylim3d([0, 5000])
    ax.set_ylabel('North (ft)')
    ax.set_zlim3d([0, 500])
    ax.set_zlabel('Up (ft)')
    ax.set_title('Amazon Drone Simulation')
    
    # Plot Warehouse, Forest, No Fly Zone
    O = [Obstacle(2500, 2500, 500, 500), Obstacle(1000, 4000, 1500, 1500), 
         Obstacle(4000, 1000, 1500, 1500)]
    plotObst(O)
    
    # Select number of trajectories
    N = 100
    # Initialize all trajectory variable
    all_traj = []

    # Get all trajectories and housing delivery locations
    for n in range(N):
        filename = 'traj_' + str(n) + '.csv'
        file = csv_2_df(filename)
        all_traj.append(file)
        # Plot delivery location
        house = file[-1]
        if n == 0:
            plt.scatter(house[0], house[1], house[2], 'r', label='Customer')
        elif n <= 35:
            plt.scatter(house[0], house[1], house[2], 'r')
            
    # Get the longest trajectory
    longest = []
    for n in range(N):
        longest.append(len(all_traj[n]))
    # Find max
    max_len = max(longest)
    
    # Initialize plotting variable for animation
    traj_0, = ax.plot([], [], [], lw=3, label='Trajectory')
    traj_1, = ax.plot([], [], [], lw=3)
    traj_2, = ax.plot([], [], [], lw=3)
    traj_3, = ax.plot([], [], [], lw=3)
    traj_4, = ax.plot([], [], [], lw=3)
    traj_5, = ax.plot([], [], [], lw=3)
    traj_6, = ax.plot([], [], [], lw=3)
    traj_7, = ax.plot([], [], [], lw=3)
    traj_8, = ax.plot([], [], [], lw=3)
    traj_9, = ax.plot([], [], [], lw=3)
    traj_10, = ax.plot([], [], [], lw=3)
    traj_11, = ax.plot([], [], [], lw=3)
    traj_12, = ax.plot([], [], [], lw=3)
    traj_13, = ax.plot([], [], [], lw=3)
    traj_14, = ax.plot([], [], [], lw=3)
    traj_15, = ax.plot([], [], [], lw=3)
    traj_16, = ax.plot([], [], [], lw=3)
    traj_17, = ax.plot([], [], [], lw=3)
    traj_18, = ax.plot([], [], [], lw=3)
    traj_19, = ax.plot([], [], [], lw=3)
    traj_20, = ax.plot([], [], [], lw=3)
    traj_21, = ax.plot([], [], [], lw=3)
    traj_22, = ax.plot([], [], [], lw=3)
    traj_23, = ax.plot([], [], [], lw=3)
    traj_24, = ax.plot([], [], [], lw=3)
    traj_25, = ax.plot([], [], [], lw=3)
    traj_26, = ax.plot([], [], [], lw=3)
    traj_27, = ax.plot([], [], [], lw=3)
    traj_28, = ax.plot([], [], [], lw=3)
    traj_29, = ax.plot([], [], [], lw=3)
    traj_30, = ax.plot([], [], [], lw=3)
    traj_31, = ax.plot([], [], [], lw=3)
    traj_32, = ax.plot([], [], [], lw=3)
    traj_33, = ax.plot([], [], [], lw=3)
    traj_34, = ax.plot([], [], [], lw=3)
    traj_35, = ax.plot([], [], [], lw=3)
    
    ax.legend()
    # Global animation function
    anim = animation.FuncAnimation(fig, animate, init_func=init, 
                            fargs=(traj_0, traj_1, traj_2, traj_3, traj_4, traj_5,
                                   traj_6, traj_7, traj_8, traj_9, traj_10, traj_11, 
                                   traj_12, traj_13, traj_14, traj_15, traj_16, traj_17,
                                   traj_18, traj_19, traj_20, traj_21, traj_22, traj_23,
                                   traj_24, traj_25, traj_26, traj_27, traj_28, traj_29,
                                   traj_30, traj_31, traj_32, traj_33, traj_34, traj_35,
                                   all_traj, N),
                               frames=max_len, interval=5,
                               repeat_delay=5, blit=True)
    file = os.path.abspath('') + '\\drone_sim.gif'
    anim.save(file, writer='imagemagick', fps=100)
    plt.show()