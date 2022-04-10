import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
from generate_trajectory import csv_2_df

plt.close('all')

N = 10
# Plot parameters
fig = plt.figure()
ax = p3.Axes3D(fig)

filenames = []
# Get files
for n in range(N):
    filenames.append('traj_' + str(n) + '.csv')

for n in range(N):
    traj = csv_2_df(filenames[n])
    
    X = traj[:, 0]
    Y = traj[:, 1]
    Z = traj[:, 2]
    
    ax.plot3D(X, Y, Z)

# 0 to 5000 feet
ax.set_xlim3d([0, 5000])
ax.set_xlabel('East (ft)')
ax.set_ylim3d([0, 5000])
ax.set_ylabel('North (ft)')
ax.set_zlim3d([0, 500])
ax.set_zlabel('Up (ft)')
ax.set_title('Amazon Drone Simulation')
    
plt.show()