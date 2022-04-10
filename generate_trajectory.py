import csv
import os
import pandas as pd

global PATH
PATH = os.path.abspath('Trajectories')

# Converts dataframe to csv file, n is trajectory number
def df_2_csv(traj_x, traj_y, traj_z, n):
    # Get path
    filename = 'traj_' + str(n)
    path = PATH + '\\' + filename + '.csv'
    
    # Create dataframe
    df = pd.DataFrame(list(zip(*[traj_x, traj_y, traj_z])))
    # Export to .csv file
    df.to_csv(path, index=False, header=['X', 'Y', 'Z'])
    

# Reads csv and gets trajectory dataframe
def csv_2_df(filename):
    # Get path
    path = PATH + '\\' + filename
    # Read trajectory
    traj = pd.read_csv(path).to_numpy()

    return traj
    