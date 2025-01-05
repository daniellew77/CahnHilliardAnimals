import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

L = 150             # size    
dx = 1.0            # spacing
dt = 0.01           # time step
epsilon = 1.5       # interface
M = 1.0             # mobility
num_steps = 20000   # total steps
plot_interval = 1000 # steps between frames

#initialize phi with random noise around 0
initial_phi = 0.01 * (np.random.rand(L, L) * 2 - 1)

def laplacian_anisotropic(phi):
    """Compute anisotropic laplacian with stronger diffusion in y direction."""
    lap_x = 0.1 * (np.roll(phi, 1, axis=0) + np.roll(phi, -1, axis=0) - 2 * phi) / dx**2
    lap_y = (np.roll(phi, 1, axis=1) + np.roll(phi, -1, axis=1) - 2 * phi) / dx**2
    return lap_x + lap_y

fig, ax = plt.subplots()
img = ax.imshow(initial_phi, cmap='gray', vmin=-1, vmax=1)
cbar = plt.colorbar(img)

def reset():
    """Reset phi to the initial configuration."""
    global phi
    phi = initial_phi.copy()

def update(frame):
    global phi
    if frame == 0:  
        reset()
    
    for _ in range(plot_interval):
        lap_phi = laplacian_anisotropic(phi)
        chem_pot = phi**3 - phi - epsilon**2 * lap_phi
        phi += dt * M * laplacian_anisotropic(chem_pot)
    
    img.set_data(phi)
    ax.set_title(f"Step {frame * plot_interval}")
    return img, ax

# Create animation
num_frames = num_steps // plot_interval
reset()  
ani = FuncAnimation(fig, update, frames=num_frames, blit=False, repeat=True)

ani.save("zebra_simulation.gif", writer=PillowWriter(fps=10))

plt.show()
