import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from generate_trajectory import csv_2_df

plt.close('all')

N = 1
# Plot parameters
fig = plt.figure()
ax = p3.Axes3D(fig)

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
        
# Plot Warehouse, Forest, No Fly Zone
O = [Obstacle(2500, 2500, 500, 500), Obstacle(1000, 4000, 1500, 1500), 
     Obstacle(4000, 1000, 1500, 1500)]
plotObst(O)
    
filenames = []
# Get files
for n in range(N):
    filenames.append('traj_' + str(n) + '.csv')
    
for n in range(N):
    traj = csv_2_df(filenames[n])
    
    X = traj[:, 0]
    Y = traj[:, 1]
    Z = traj[:, 2]
    
    # Plot delivery location
    house = [X[-1], Y[-1], Z[-1]]
    if n == 0:
        plt.scatter(house[0], house[1], house[2], 'r', label='Customer')
    elif n <= 35:
        plt.scatter(house[0], house[1], house[2], 'r')
    
    if n == 0:
        ax.plot3D(X, Y, Z, lw=3, label='Trajectory')
    else:
        ax.plot3D(X, Y, Z, lw=3)

# 0 to 5000 feet
ax.set_xlim3d([0, 5000])
ax.set_xlabel('East (ft)')
ax.set_ylim3d([0, 5000])
ax.set_ylabel('North (ft)')
ax.set_zlim3d([0, 500])
ax.set_zlabel('Up (ft)')
ax.set_title('Amazon Drone Simulation')
ax.legend()

plt.show()

fig = plt.figure()
plt.plot(X, Y)
