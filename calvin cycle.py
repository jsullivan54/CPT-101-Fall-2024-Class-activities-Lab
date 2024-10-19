import matplotlib.pyplot as plt
import numpy as np

# Define the components of the Calvin cycle
stages = [
    "1. Carbon Fixation\n(CO₂ + RuBP → 3-PGA)",
    "2. Reduction Phase\n(3-PGA + ATP + NADPH → G3P)",
    "3. Regeneration of RuBP\n(G3P → RuBP)"
]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})

# Define the angles for each stage
angles = np.linspace(0, 2 * np.pi, len(stages), endpoint=False).tolist()
angles += angles[:1]  # Close the circle

# Set radius for each stage
radii = [1] * len(stages)
radii += [1]  # Close the circle

# Create the plot
ax.fill(angles, radii, color='lightgreen', alpha=0.5)
ax.set_xticks(angles[:-1])  # Set the ticks
ax.set_xticklabels(stages)  # Label the stages

# Add title
plt.title("The Calvin Cycle", fontsize=16)
ax.set_yticklabels([])  # Hide radial ticks

# Display the plot
plt.show()
