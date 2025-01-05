import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

L = 150             # size
dx = 1.0            # spacing
dt = 0.01           # time step
epsilon = 1.5       # interface
M = 1.0             # mobility
num_steps = 10000   # total steps
plot_interval = 500 # steps between frames

# Initialize phi as hexagonal grid
initial_phi = np.zeros((L, L))
initial_phi += 0.05 * (np.random.rand(L, L) * 2 - 1)
spacing = 20
for i in range(0, L, spacing):
    for j in range(0, L, spacing):
        initial_phi[i:i+spacing//2, j:j+spacing//2] = np.random.choice([-1, 1])
initial_phi += 0.1 * (np.random.rand(L, L) * 2 - 1)

def laplacian(phi):
    return (np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0) +
            np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1) - 4 * phi) / dx**2

fig, ax = plt.subplots()
img = ax.imshow(initial_phi, cmap='gray', vmin=-1, vmax=1)
cbar = plt.colorbar(img)

def reset():
    """Reset phi to the initial configuration."""
    global phi
    phi = initial_phi.copy()

def update(frame):
    global phi
    if frame == 0:  # Reset phi at the start of a new loop
        reset()
    
    for _ in range(plot_interval):
        lap_phi = laplacian(phi)
        chem_pot = phi**3 - phi - epsilon**2 * lap_phi
        phi += dt * M * laplacian(chem_pot)
    
    img.set_data(phi)
    ax.set_title(f"Step {frame * plot_interval}")
    return img, ax

# Create animation
num_frames = num_steps // plot_interval
reset()  # reset phi before animation starts
ani = FuncAnimation(fig, update, frames=num_frames, blit=False, repeat=True)

ani.save("giraffe_simulation.gif", writer=PillowWriter(fps=10))

plt.show()
