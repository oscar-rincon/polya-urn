import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from an Excel file
data = pd.read_excel("Las_muertes_por_viruela_en_Suiza_ en_1877_1900.xlsx")

# Extract data columns as NumPy arrays
months = data.iloc[2:, 0].values
population = data.iloc[2:, 1].values
deaths = data.iloc[2:, 4].values
ec_18 = data.iloc[2:, 5].values
ec_14 = data.iloc[2:, 6].values

# Set the font to a sans-serif font that is available on your system
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 10

# Create a figure with a specified size
plt.figure(figsize=(4, 4))  # Adjust the numbers as needed for your desired vertical size

# Plot lines and specify labels for the legend
plt.step(months, deaths, '-', color="black", label="Reales")
plt.plot(months, ec_18, '--', color="black", label="Estimadas (18)")
plt.plot(months, ec_14, '-', color="black", label="Estimadas (14)")

# Display the legend at the bottom-right corner
plt.legend(loc="lower right")

# Enable grid lines
plt.grid(True)

# Set the limits for the x and y axes
plt.xlim([months[0], months[-1]])
plt.ylim([0, 300])  # Adjust as needed

# Set ticks on the vertical axis from 20 to 20
yticks = np.arange(0, 300, 20)
plt.yticks(yticks)

# Add labels for the vertical and horizontal axes
plt.xlabel("Meses")
plt.ylabel("Numero de muertes")

# Set a title for the plot
#plt.title("Muertes por viruela en Suiza (1877-1900)")

# Save the figure as a PDF with a suitable name
output_filename = "smallpox_deaths_switzerland.pdf"  # Adjust the filename as needed
plt.savefig(output_filename, format="pdf")

# Display the plot
plt.show()