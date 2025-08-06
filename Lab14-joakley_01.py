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
    # Restrict x-value range to make asymptotes clearer
    limited_x = list(range(-90, 91))
    # To avoid the asymptotes, create a list of the angles that do not equal (90 + [k*180]) degrees
    safe_angles = [a for a in limited_x if a % 180 != 90]

    # Convert the safe values to radians
    safe_radians = [math.radians(a) for a in safe_angles]

    # Calculate the tangent values for the safe angles using the radian values
    y = [math.tan(rad) for rad in safe_radians]

    # Plot the tangent function
    plt.figure(figsize=(10, 5))
    plt.plot(safe_angles, y, color='blue', linewidth=2, label='tan(x)')

    # Draw the tangent asymptotes
    asymptotes_values = [a for a in range(-270, 271, 180) if a != 0]
    for i, a in enumerate(asymptotes_values):
        plt.axvline(x=a, color='red', linestyle='--', linewidth=1, label='Asymptote' if i == 0 else "")

    # Set the plot limits and labels
    plt.title('Tangent Function with Asymptotes')
    plt.xlabel('Angle (Degrees)')
    plt.ylabel('tan(angle)')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.ylim(-5, 5)
    plt.legend()
    plt.show()

# Call the tangent function
plot_tangent()
