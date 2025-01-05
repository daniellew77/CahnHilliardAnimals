import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

L = 100             # Grid size 
dx = 1.0            # Spacing
dt = 0.01           # Time step
epsilon = 0.5       # Interface width
M = 1.0             # Mobility
num_steps = 5000    # Number of time steps
plot_interval = 500 # Interval to plot
num_spots = 10000   # Number of initial spots

def initialize_phi():
    """Initialize phi with random spots."""
    phi = np.zeros((L, L))
    for _ in range(num_spots):
        x, y = np.random.randint(0, L, size=2)
        phi[x, y] = np.random.choice([-1, 1])
    return phi

initial_phi = initialize_phi()

def laplacian(phi):
    """Compute the Laplacian of phi."""
    return (np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0) +
            np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1) - 4 * phi) / dx**2

fig, ax = plt.subplots()
img = ax.imshow(initial_phi, cmap='gray', vmin=-1, vmax=1)
cbar = plt.colorbar(img)

def reset():
    """Reset phi to the initial random spot configuration."""
    global phi
    phi = initialize_phi()

def update(frame):
    global phi
    if frame == 0:  
        reset()
    
    for _ in range(plot_interval):
        lap_phi = laplacian(phi)
        chem_pot = phi**3 - phi - epsilon**2 * lap_phi
        phi += dt * M * laplacian(chem_pot)
    
    img.set_data(phi)
    ax.set_title(f"Step {frame * plot_interval}")
    return img, ax

num_frames = num_steps // plot_interval
reset()  
ani = FuncAnimation(fig, update, frames=num_frames, blit=False, repeat=True)

ani.save("leopard_simulation.gif", writer=PillowWriter(fps=10))

plt.show()
