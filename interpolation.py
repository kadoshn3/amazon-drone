from scipy.interpolate import interp1d
import numpy as np
from generate_trajectory import csv_2_df

N = 10

filenames = []
all_traj = []
# Get files
for n in range(N):
    filenames.append('traj_' + str(n) + '.csv')
    all_traj.append(csv_2_df(filenames[n]))
traj_1 = csv_2_df(filenames[0])
traj_2 = csv_2_df(filenames[1])

x_old = traj_2[:, 0]
y_old = traj_2[:, 1]
z_old = traj_2[:, 2]

# Interpolate the data using a cubic spline to "new_length" samples
new_length = len(traj_1)
new_x = np.linspace(x_old.min(), x_old.max(), new_length)
new_y = interp1d(x_old, y_old, kind='cubic')(new_x)

print(len(x_old))