import random
import math

def generate_houses(N):
    house_lst = []
    
    center_x = 2500
    center_y = 2500
    
    inner_radius = 500
    outer_radius = 5000
    count = 0
    while (count != N):
        x = random.randint(0, outer_radius)
        y = random.randint(0, outer_radius)
        
        in_check = (x-center_x)^2 + (y - center_y)^2 > inner_radius^2
        out_check = (x-center_x)^2 + (y - center_y)^2 < outer_radius^2
        
        if (in_check == True) & (out_check == True):
            house_lst.append([x, y])
            count += 1
        
    return house_lst