import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the Euclidean distance between two points
def distance(point1, point2):
    return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))

# Function to read waypoints from file
def read_waypoints(file_path):
    waypoints = []
    with open(file_path, 'r') as file:
        for line in file:
            values = line.split()
            if len(values) >= 3:  # Ensure there are at least x, y, z values
                try:
                    # Extract x, y, z coordinates and convert to float
                    x, y, z = map(float, values[:3])
                    waypoints.append((x, y, z))
                except ValueError:
                    print(f"Invalid line in file: {line}")
    return waypoints

# Function to plot waypoints and toolpaths
def plot_waypoints(waypoints, max_jump=5):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Extract x, y, z coordinates
    xs, ys, zs = zip(*waypoints)

    # Plot waypoints
    ax.scatter(xs, ys, zs, c='red', marker='o', s=2)  # s is the size of the point

    # Plot toolpaths (lines) with jump detection
    for i in range(len(waypoints) - 1):
        if distance(waypoints[i], waypoints[i + 1]) <= max_jump:
            ax.plot([xs[i], xs[i+1]], [ys[i], ys[i+1]], [zs[i], zs[i+1]], color='blue')

    # Set axis limits to make them equal
    max_range = np.array([max(xs)-min(xs), max(ys)-min(ys), max(zs)-min(zs)]).max() / 2.0
    mid_x = (max(xs) + min(xs)) * 0.5
    mid_y = (max(ys) + min(ys)) * 0.5
    mid_z = (max(zs) + min(zs)) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.title('Waypoints and Toolpaths Visualization')
    plt.show()

# Replace 'waypoints_file.txt' with the path to your waypoints file
waypoints_file = '11.txt'
waypoints = read_waypoints(waypoints_file)
plot_waypoints(waypoints)
