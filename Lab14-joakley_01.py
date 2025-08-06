"""
Graphing the Tangent Function with its asymtotes
Jeroldine Oakley [author]
This program calculates and plots the tangent function and its asymptotes.
08/06/2025
"""

import math
import matplotlib.pyplot as plt

# Create a list of common angles in degrees
angles = list(range(-360, 361))

# Convert angles to radians for calculations
radians = [math.radians(a) for a in angles]

# Define function to calculate and plot the tangent function
def plot_tangent():
    # Define x-range values to include multiple periods/cycles of the tangent function
    full_x = list(range(-270, 271))

    # Setup the plot
    plt.figure(figsize=(10, 10))

    # Define the tangent asymptotes values
    asymptotes_values = [a for a in range(-270, 271, 180) if a != 0]

    # Plot the asymptotes
    for i, a in enumerate(asymptotes_values):
        plt.axvline(x=a, color='red', linestyle='--', linewidth=1, label='Asymptote' if i == 0 else "")
    
    # Calculate and plot the tangent function per cycle while avoiding the asymptotes
    tangent_edges = [-270] + asymptotes_values + [270]
    for i in range(len(tangent_edges) - 1):
        # Start drawing from the first asymptote to the next one,
        # making sure to be "1" degree away from the asymptote
        start = tangent_edges[i] + 1
        end = tangent_edges[i + 1]

        # Calculate the values for the safe angles between asymptotes
        safe_angles = [a for a in full_x if start < a < end]

        # Calculate the tangent values for the safe angles
        y = [math.tan(math.radians(a)) for a in safe_angles]

        # Plot the tangent function segment
        plt.plot(safe_angles, y, color='blue', linewidth=2, label='tan(angle)' if i == 0 else "")

    # Set the plot limits and labels
    plt.title('Tangent Function with Asymptotes')
    plt.xlabel('Angle (Degrees)')
    plt.ylabel('tan(angle)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.ylim(-20, 20)
    plt.legend()
    plt.show()

# Call the tangent function
plot_tangent()
