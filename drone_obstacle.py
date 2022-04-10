import math
import matplotlib.pyplot as plt
from matplotlib import animation
import os

plt.close('all')

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
	    self.dest_y =b
	    self.blocked = False
	    
class Obstacle():
	def __init__ (self, x, y, l, w):
		self.cx = x
		self.cy = y
		self.l = l
		self.w = w

def Coordinates(drone, dest_x, dest_y, t, x, y, sx, sy):        
    cost = 1
    sint = 1
    if(dest_x < sx):
        sint = -1
        cost = -1
    if(dest_x == sx and dest_y < sy):
        sint = -1
        
    
    if(dest_x != sx):
        x = x + drone.max_vel * cost * math.cos(math.atan((dest_y - sy) / (dest_x - sx)))
        y = y + drone.max_vel * sint * math.sin(math.atan((dest_y - sy) / (dest_x - sx)))
    else:
        y = y + drone.max_vel * sint
	        
    if(dest_x >= sx and x >= dest_x):
	        if(dest_y > sy and y >= dest_y):
	            x = dest_x
	            y = dest_y
	        elif(dest_y < sy and y <= dest_y):
	            x = dest_x
	            y = dest_y
    elif(dest_x <= sx and x <= dest_x):
	        if(dest_y > sy and y >= dest_y):
	            x = dest_x
	            y = dest_y
	        elif(dest_y < sy and y <= dest_y):
	            x = dest_x
	            y = dest_y
	               
    return x, y
	
	
def distance(sx, sy, ex, ey):
    return math.sqrt(pow(ex-sx, 2) + pow(ey-sy, 2))

def getObstacle(sx, sy, ex, ey, O):
    m = "inf"
    if(ex - sx != 0):
        m = (ey - sy)/(ex-sx)
    blocked = False
    
    for obst in O:
        if(obst.cx - obst.l/2 <= ex and ex <= obst.cx + obst.l/2 and obst.cy - obst.w/2 <= ey and ey <= obst.cy + obst.w/2):
            return "invalid", ex, ey
        if(blocked == False):
            if(m == "inf"):
                x = sx
                if(obst.cx - obst.l/2 <= x and x <= obst.cx + obst.l/2):
                    blocked = True
                    Blocker = obst
            elif(m == 0):
                y = sy
                if(obst.cy - obst.w/2 <= y and y <= obst.cy + obst.w/2):
                    blocked = True
                    Blocker = obst
                
            else:
                x = ((obst.cy - obst.w / 2) - sy)/m + sx
                if(obst.cx - obst.l/2 <= x and x <= obst.cx + obst.l/2 and x <= ex and x >= sx):
                    blocked = True
                    Blocker = obst
                x = ((obst.cy + obst.w / 2) - sy)/m + sx
                if(obst.cx - obst.l /2 <= x and x <= obst.cx + obst.l /2  and x <= ex and x >= sx):
                    blocked = True
                    Blocker = obst
                y = m * ((obst.cx - obst.l / 2) - sx)	+ sy
                if(obst.cy - obst.w/2 <= y and y <= obst.cy + obst.w/2 and y <= ey and y >= sy):
                    blocked = True
                    Blocker = obst
                y = m * ((obst.cx + obst.l / 2) - sx)	+ sy
                if(obst.cy - obst.w/2 <= y and y <= obst.cy + obst.w/2 and y <= ey and y >= sy):
                    blocked = True
                    Blocker = obst
	
    if(blocked):
        close_x, close_y = Blocker.cx - Blocker.l/2, Blocker.cy - Blocker.w/2
        test_x, test_y = Blocker.cx + Blocker.l/2, Blocker.cy - Blocker.w/2
        new_dest_x1, new_dest_y1 = Blocker.cx - Blocker.l/2 - 10, Blocker.cy + Blocker.w/2 + 10
        new_dest_x2, new_dest_y2 = Blocker.cx + Blocker.l/2 + 10, Blocker.cy - Blocker.w/2 - 10
        
        if(distance(sx, sy, test_x, test_y) <  distance(sx, sy, close_x, close_y)):
            close_x, close_y = test_x, test_y
            new_dest_x1, new_dest_y1 = Blocker.cx - Blocker.l/2 - 10, Blocker.cy - Blocker.w/2 - 10
            new_dest_x2, new_dest_y2 = Blocker.cx + Blocker.l/2 + 10, Blocker.cy + Blocker.w/2 + 10
            
            test_x, test_y = obst.cx - obst.l/2, obst.cy + obst.w/2
        if(distance(sx, sy, test_x, test_y) <  distance(sx, sy, close_x, close_y)):
                close_x, close_y = test_x, test_y
                new_dest_x1, new_dest_y1 = Blocker.cx - Blocker.l/2 - 10, Blocker.cy - Blocker.w/2 - 10
                new_dest_x2, new_dest_y2 = Blocker.cx + Blocker.l/2 + 10, Blocker.cy + Blocker.w/2 + 10
                
                test_x, test_y = obst.cx + obst.l/2, obst.cy + obst.w/2
        if(distance(sx, sy, test_x, test_y) <  distance(sx, sy, close_x, close_y)):
            close_x, close_y = test_x, test_y
            new_dest_x1, new_dest_y1 = Blocker.cx - Blocker.l/2 - 10, Blocker.cy + Blocker.w/2 + 10
            new_dest_x2, new_dest_y2 = Blocker.cx + Blocker.l/2 + 10, Blocker.cy - Blocker.w/2 - 10
	        
        if(distance(new_dest_x1, new_dest_y1, ex, ey) < distance(new_dest_x2, new_dest_y2, ex, ey)):
            return obst, new_dest_x1, new_dest_y1
        return obst, new_dest_x2, new_dest_y2
    return -1, ex, ey	

def plotObst(O):
    label = True
    for obst in O:
        #name = 'Obstacle ' + str(i)
        box_x = [obst.cx - obst.l/2, obst.cx + obst.l/2, obst.cx + obst.l/2, obst.cx - obst.l/2, obst.cx - obst.l/2]
        box_y = [obst.cy - obst.w/2, obst.cy - obst.w/2, obst.cy + obst.w/2, obst.cy + obst.w/2, obst.cy - obst.w/2]
        if label:
            plt.plot(box_x, box_y, 'g-', label='Obstacle')
            label = False
        else:
            plt.plot(box_x, box_y, 'g-')

W = Warehouse()
D = Drone(W,150,150,0)
O = [Obstacle(50, 50, 25, 20), Obstacle(100, 100, 5, 50), Obstacle(-5, 10, 5, 5), \
     Obstacle(120, 140, 1, 10), Obstacle(50, -50, 10, 10), Obstacle(130, 100, 30, 20)]
path = []
tx, ty = D.x, D.y
obst, tdest_x, tdest_y = getObstacle(D.x, D.y, D.dest_x, D.dest_y, O)
x, y = D.x, D.y

# Animate figure data
fig = plt.figure()
ax = plt.axes()
ax.set_xlabel('East (ft)')
ax.set_ylabel('North (ft)')
ax.set_title('Amazon Drone 2D Object Avoidance Simulation')

plt.plot(x, y, 'ro', label='Start/End Destination')
plt.plot(D.dest_x, D.dest_y, 'ro')
path.append([x, y])
trajx = [x]
trajy = [y]
for t in range (200):
    while(obst != -1 and obst != "invalid"):
        obst, tdest_x, tdest_y = getObstacle(x, y, tdest_x, tdest_y, O)
    x, y = Coordinates(D, tdest_x, tdest_y, t, x, y, tx, ty)
    if(obst == "invalid"):
        x, y = D.Ware.x, D.Ware.y
        D.blocked = True
    if((x != tdest_x or y != tdest_y)):
        path.append( [x, y])
        trajx.append(x)
        trajy.append(y)     
    elif(x != D.dest_x and y != D.dest_y):
        path.append( [x, y])
        trajx.append(x)
        trajy.append(y)
        tx, ty = tdest_x, tdest_y
        tdest_x, tdest_y = D.dest_x, D.dest_y
        obst, tdest_x, tdest_y = getObstacle(x, y, tdest_x, tdest_y, O)
        
    elif(D.dest_time == -1):
        D.dest_time = t
    
if(D.blocked == False):
    for i in range(3):
        path.append([D.dest_x, D.dest_y])
        trajx.append(D.dest_x)
        trajy.append(D.dest_y)
else:
    print("Destination is Blocked")


l = len(path)
for i in range(l):
    path.append(path[l - i - 1])
    
# Plot the obstacles
plotObst(O)

# Create animation variable
traj, = ax.plot(trajx, trajy, lw=4, label='Trajectory')

drone, = ax.plot(trajx, trajy, 'bo', lw=4, label='Drone')
ax.legend()

# Function to iterate each element in trajectory
def animate(i, traj, X, Y, drone):
    traj.set_data(X[:i], Y[:i])
    drone.set_data(X[i-1], Y[i-1])
    
    return traj, drone, 

# Call function
anim = animation.FuncAnimation(fig, animate, fargs=(traj, trajx, trajy, drone),
                           frames=len(trajx), interval=50,
                           blit=True)

file = os.path.abspath('') + '\\object_avoidance_animation.gif'
anim.save(file, writer='imagemagick', fps=100)

# Show plot
plt.show()