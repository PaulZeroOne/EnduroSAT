
from Ballistic_Integrators import *
from Triangulation import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
import imageio

# Read input file and calculate the x,y,z coordinates of each data point 
x_array, y_array, z_array, data = compute_coordinates('texttest.txt')

# Extract the last two rows of position in data array
last_index = len(x_array) - 1
penultimate_index = last_index - 1

# Take last two rows of data array to compute verlet ballistic trajectory
pos_last = np.array([x_array[last_index], y_array[last_index], z_array[last_index]])
pos_penultimate = np.array([x_array[penultimate_index], y_array[penultimate_index], z_array[penultimate_index]])

# Calculate velocity vector between the last two positions
time_step = data['Time'][last_index] - data['Time'][penultimate_index]
delta_r = pos_last - pos_penultimate
vel_0 = delta_r / time_step

# Example parameters for ballistic trajectory
g = 9.81 # [m/sec^2]
beta = 0.00 # [1/sec] constant for drag
Npoints = 100 # Number of points
t_params = [0.0, 5.0, Npoints] # Time parameters: start time, end time, number of points

# Compute the trajectory using Verlet_Ballistic integration method
t_arr, pos, vel = Verlet_Ballistic(g, beta, pos_last, vel_0, t_params)

# Create a directory to store the frames
frame_dir = 'frames'
os.makedirs(frame_dir, exist_ok=True)
filenames = []

# Plot and save each frame
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(t_arr)):
    ax.clear()
    
    # Plot the recorded data points
    ax.plot(x_array, y_array, z_array, 'ro', label='Recorded Data')
    
    # Plot the predicted trajectory up to the current frame
    ax.plot(pos[0, :i+1], pos[1, :i+1], pos[2, :i+1], 'b-', marker='o', label='Predicted Trajectory')
    
    ax.set_xlim([np.min(np.concatenate([x_array, pos[0]])), np.max(np.concatenate([x_array, pos[0]]))])
    ax.set_ylim([np.min(np.concatenate([y_array, pos[1]])), np.max(np.concatenate([y_array, pos[1]]))])
    ax.set_zlim([0, np.max(np.concatenate([z_array, pos[2]]))])
    
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Z Coordinate')
    
    if i == 0:  # Adding legend only once
        ax.legend()
    
    filename = os.path.join(frame_dir, f'frame_{i}.png')
    filenames.append(filename)
    plt.savefig(filename)

plt.close()

# Create the GIF
with imageio.get_writer('ballistic_trajectory.gif', mode='I', duration=0.1) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Clean up the frame images
for filename in filenames:
    os.remove(filename)
