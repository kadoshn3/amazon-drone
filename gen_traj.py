import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


class Warehouse():
    def __init__(self):
        # Rectangular size [ft]
        self.length = 894
        self.width = 894
        self.height = 60
        
        # Positional coordinates
        self.x = 0
        self.y = 0
        self.z = 0

class Drone:
	def __init__(self, W,a,b,t):
	    self.Ware = W
	    self.x = W.x
	    self.y = W.y
	    self.z = W.z
	    self.ret = False
	    self.max_alt = 200
	    self.max_alt_time = -1
	    self.ascent_vel = 5
	    self.descent_vel = 5
	    self.max_vel = 5
	    self.deploy_time = t
	    self.dest_time = -1
	    self.dest_x = a
	    self.dest_y = b

def Coordinates(drone, t):
	x = drone.x
	y = drone.y
	z = 0
	
	if(drone.ret == False):
	    if(drone.max_alt_time != -1):
	        cost = 1
	        sint = 1
	        if(drone.dest_x < 0):
	            sint = -1
	            cost = -1
	            
	        x = drone.x + drone.max_vel * cost * math.cos(math.atan(drone.dest_y / drone.dest_x))
	        y = drone.y + drone.max_vel * sint * math.sin(math.atan(drone.dest_y / drone.dest_x))
	        
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
	    if(t < drone.deploy_time + drone.max_alt / drone.ascent_vel):
	        z = drone.ascent_vel * (t - drone.deploy_time)
	    elif(drone.dest_time == -1):
	        z = drone.max_alt
	        if(drone.max_alt_time == -1):
	            drone.max_alt_time = t
	    else:
	        z = drone.max_alt - drone.descent_vel * (t - drone.dest_time)
	        if(z < 0):
	            z = 0
	
	if(drone.ret):
	    if(drone.max_alt_time != -1):
	        cost = 1
	        sint = 1
	        if(drone.dest_x < 0):
	            sint = -1
	            cost = -1
	        x = drone.x - drone.max_vel * cost * math.cos(math.atan(drone.dest_y / drone.dest_x))
	        y = drone.y - drone.max_vel * sint * math.sin(math.atan(drone.dest_y / drone.dest_x))

	        
	    if(drone.dest_x > drone.Ware.x and x <= drone.Ware.x):
		    if(drone.dest_y >= drone.Ware.y and y <= drone.Ware.y):
		        x = drone.Ware.x
		        y = drone.Ware.y
		        if(drone.dest_time == -1):
		            drone.dest_time = t
		    elif(drone.dest_y <= drone.Ware.y and y >= drone.Ware.y):
		        x = drone.Ware.x
		        y = drone.Ware.y
		        if(drone.dest_time == -1):
		            drone.dest_time = t
		            
	    elif(drone.dest_x < drone.Ware.x and x >= drone.Ware.x):
	        if(drone.dest_y >= drone.Ware.y and y <= drone.Ware.y):
	            x = drone.Ware.x
	            y = drone.Ware.y
	            if(drone.dest_time == -1):
	                drone.dest_time = t
	        elif(drone.dest_y <= drone.Ware.y and y >= drone.Ware.y):
	            x = drone.Ware.x
	            y = drone.Ware.y
	            if(drone.dest_time == -1):
	                drone.dest_time = t
	                
	    if(t >= drone.deploy_time):
	        if(t <= drone.deploy_time + drone.max_alt / drone.ascent_vel):
	            z = drone.ascent_vel * (t - drone.deploy_time)
	        elif(drone.dest_time == -1):
	            z = drone.max_alt
	            if(drone.max_alt_time == -1):
	                drone.max_alt_time = t
	        else:
	            z = drone.max_alt - drone.descent_vel * (t - drone.dest_time)
	            if(z < 0):
	                z = 0
	                
	drone.x = x
	drone.y = y
	drone.z = z
	
	
W = Warehouse()
D = Drone(W,1000,1500,0)

fig = plt.figure()
ax = plt.axes(projection='3d')

path = []
traj_x = []
traj_y = []
traj_z = []
for t in range(1000):
    if(D.dest_time != -1 and D.z == 0 and D.ret == False):
        D.max_alt_time = -1
        D.deploy_time = t + 5
        D.dest_time = -1
        D.ret = True
    Coordinates(D, t)
    path.append( [D.x, D.y, D.z])
    traj_x.append(D.x)
    traj_y.append(D.y)
    traj_z.append(D.z)
#print(path)
ax.plot3D(traj_x, traj_y, traj_z)