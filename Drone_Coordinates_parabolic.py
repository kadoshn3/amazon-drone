import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from generate_houses import generate_houses
from generate_trajectory import df_2_csv

class Warehouse():
    def __init__(self):
        # Rectangular size [ft]
        self.length = 894
        self.width = 894
        self.height = 60
        
        # Positional coordinates
        self.x = 2500
        self.y = 2500
        self.z = 0
        
class Drone:
	def __init__(self, W,a,b,t):
	    self.Ware = W
	    self.x = W.x
	    self.y = W.y
	    self.z = W.z
	    self.ret = False
	    self.max_alt = 200
	    self.leave_time = -1
	    self.ascent_vel = 5
	    self.descent_vel = 5
	    self.max_vel = 5
	    self.deploy_time = t
	    self.dest_time = -1
	    self.dest_x = a
	    self.dest_y = b
	    self.done = False
        
def Coordinates(drone, t):
    x = drone.x
    y = drone.y
    z = drone.z
    
    if(drone.leave_time != -1):
        cost = 1
        sint = 1
        if(drone.dest_x < drone.Ware.x):
            sint = -1
            cost = -1
        if(drone.dest_x == drone.Ware.x and drone.dest_y < drone.Ware.y):
            sint = -1
	            
        if(drone.dest_x != drone.Ware.x):
            x = drone.x + drone.max_vel * cost * math.cos(math.atan((drone.dest_y - drone.Ware.y) / (drone.dest_x - drone.Ware.x)))
            y = drone.y + drone.max_vel * sint * math.sin(math.atan((drone.dest_y - drone.Ware.y) / (drone.dest_x - drone.Ware.x)))
        else:
            y = drone.y + drone.max_vel * sint
	        
    if(drone.dest_x > drone.Ware.x and x >= drone.dest_x):
        if(drone.dest_y >= drone.Ware.y and y >= drone.dest_y):
            x = drone.dest_x
            y = drone.dest_y
            if(drone.dest_time == -1):
                drone.dest_time = t
        elif(drone.dest_y <= drone.Ware.y and y <= drone.dest_y):
            x = drone.dest_x
            y = drone.dest_y
            if(drone.dest_time == -1):
                drone.dest_time = t
    elif(drone.dest_x < drone.Ware.x and x <= drone.dest_x):
        if(drone.dest_y >= drone.Ware.y and y >= drone.dest_y):
            x = drone.dest_x
            y = drone.dest_y
            if(drone.dest_time == -1):
                drone.dest_time = t
        elif(drone.dest_y <= drone.Ware.y and y <= drone.dest_y):
            x = drone.dest_x
            y = drone.dest_y
            if(drone.dest_time == -1):
                drone.dest_time = t
    if(t >= drone.deploy_time):
        if(drone.dest_time == -1 and z < drone.max_alt):
            z = drone.ascent_vel  * math.exp(-(t - drone.deploy_time) / (drone.max_alt /1.8)) * (t - drone.deploy_time)
            if(drone.leave_time == -1 and drone.z > 0):
                drone.leave_time = t
        elif(drone.dest_time == -1):
            z = drone.max_alt
        else:
            z = z - drone.descent_vel
            if(z < 0):
                z = 0
                
    if(drone.x == drone.dest_x and drone.y == drone.dest_y and z == 0):
        drone.done = True
	
                
    drone.x = x
    drone.y = y
    drone.z = z

# Number of trajectories
N = 

# Generate houses
house_lst = generate_houses(N)
#fig = plt.figure()
#ax = plt.axes(projection='3d')
for n in range(N):
    house_x = house_lst[n][0]
    house_y = house_lst[n][1]
    W = Warehouse()
    D = Drone(W,house_x,house_y,0)
    
    path = []
    traj_x = []
    traj_y = []
    traj_z = []
    t = 0
    while (D.done == False):
        Coordinates(D, t)
        if(D.done == False):
            path.append( [D.x, D.y, D.z])
            traj_x.append(D.x)
            traj_y.append(D.y)
            traj_z.append(D.z)
        t += 1
    
    df_2_csv(traj_x, traj_y, traj_z, n)