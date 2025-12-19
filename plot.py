import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Vertical Velocity Profile
# U-x vs y
# For H - 10, 20, 30, 40, 50

# Loading data for all mesh sizes (Vertical)
data_h_10 = pd.read_csv("cavity_H_10/postProcessing/linesampling/10/verticalMid.csv")
data_h_20 = pd.read_csv("cavity_H_20/postProcessing/linesampling/10/verticalMid.csv")
data_h_30 = pd.read_csv("cavity_H_30/postProcessing/lineSampling/10/verticalMid.csv")
data_h_40 = pd.read_csv("cavity_H_40/postProcessing/lineSampling/10/verticalMid.csv")
data_h_50 = pd.read_csv("cavity_H_50/postProcessing/linesampling/10/verticalMid.csv")
data_h_100 = pd.read_csv("cavity_H_100/postProcessing/linesampling/10/verticalMid.csv")
data_h_200 = pd.read_csv("cavity_H_200/postProcessing/linesampling/10/verticalMid.csv")
data_h_300 = pd.read_csv("cavity_H_300/postProcessing/linesampling/9.9999/verticalMid.csv")

# Loading U-x data mesh wise

u_x_h_10 = data_h_10["U_x"]
u_x_h_20 = data_h_20["U_x"]
u_x_h_30 = data_h_30["U_x"]
u_x_h_40 = data_h_40["U_x"]
u_x_h_50 = data_h_50["U_x"]
u_x_h_100 = data_h_100["U_x"]
u_x_h_200 = data_h_200["U_x"]
u_x_h_300 = data_h_300["U_x"]

# Loading y axis mesh wise

y_h_10 = data_h_10["y"]
y_h_20 = data_h_20["y"]
y_h_30 = data_h_30["y"]
y_h_40 = data_h_40["y"]
y_h_50 = data_h_50["y"]
y_h_100 = data_h_100["y"]
y_h_200 = data_h_200["y"]
y_h_300 = data_h_300["y"]

# Loading data for all mesh sizes (Horizontal)
data_h_10_h = pd.read_csv("cavity_H_10/postProcessing/linesampling/10/horizontalMid.csv")
data_h_20_h = pd.read_csv("cavity_H_20/postProcessing/linesampling/10/horizontalMid.csv")
data_h_30_h = pd.read_csv("cavity_H_30/postProcessing/lineSampling/10/horizontalMid.csv")
data_h_40_h = pd.read_csv("cavity_H_40/postProcessing/lineSampling/10/horizontalMid.csv")
data_h_50_h = pd.read_csv("cavity_H_50/postProcessing/linesampling/10/horizontalMid.csv")
data_h_100_h = pd.read_csv("cavity_H_100/postProcessing/linesampling/10/horizontalMid.csv")
data_h_200_h = pd.read_csv("cavity_H_200/postProcessing/linesampling/10/horizontalMid.csv")
data_h_300_h = pd.read_csv("cavity_H_300/postProcessing/linesampling/9.9999/horizontalMid.csv")

# Loading x axis mesh wise

x_h_10_h = data_h_10_h["x"]
x_h_20_h = data_h_20_h["x"]
x_h_30_h = data_h_30_h["x"]
x_h_40_h = data_h_40_h["x"]
x_h_50_h = data_h_50_h["x"]
x_h_100_h = data_h_100_h["x"]
x_h_200_h = data_h_200_h["x"]
x_h_300_h = data_h_300_h["x"]

# Loading U-y data mesh wise

u_y_h_10_h = data_h_10_h["U_y"]
u_y_h_20_h = data_h_20_h["U_y"]
u_y_h_30_h = data_h_30_h["U_y"]
u_y_h_40_h = data_h_40_h["U_y"]
u_y_h_50_h = data_h_50_h["U_y"]
u_y_h_100_h = data_h_100_h["U_y"]
u_y_h_200_h = data_h_200_h["U_y"]
u_y_h_300_h = data_h_300_h["U_y"]

# Plotting the Vertical Profile

y = [0, 0.015, 0.085, 0.089]
x = [0, -0.2, 0.2, 0.4]

plt.figure(figsize = (10, 10))
plt.plot(u_x_h_10, y_h_10, 'k-', linewidth = 2, label = "U_x_h_10", color = "red")
#plt.plot(u_x_h_20, y_h_20, 'k-', linewidth = 2, label = "U_x_h_20", color = "green")
#plt.plot(u_x_h_30, y_h_30, 'k-', linewidth = 2, label = "U_x_h_30", color = "blue")
plt.plot(u_x_h_40, y_h_40, 'k-', linewidth = 2, label = "U_x_h_40", color = "orange")
#plt.plot(u_x_h_50, y_h_50, 'k-', linewidth = 2, label = "U_x_h_50", color = "black")
plt.plot(u_x_h_100, y_h_100, 'k-', linewidth = 2, label = "U_x_h_100", color = "brown")
plt.plot(u_x_h_200, y_h_200, 'k-', linewidth = 2, label = "U_x_h_200", color = "cyan")
plt.plot(u_x_h_300, y_h_300, 'k-', linewidth = 2, label = "U_x_h_300", color = "violet")
plt.plot(x, y, '-o', linewidth = 2, label = "Analytical/Numerical (Dummy)", color = "skyblue")
plt.grid(True)
plt.legend()
plt.title("Vertical Centerline (How horizontal velocities varies from bottom to top)")
plt.xlabel("u velocity")
plt.ylabel("y")
plt.minorticks_on()
#plt.xticks(np.arange(0,0.1, 0.02))

plt.savefig('vertical_Profile.png', dpi = 300, bbox_inches = 'tight')

plt.show()

# Plotting the Horizontal Profile

x1 = [0, 0.01, 0.045, 0.085]
y1 = [0, 0.025, 0, -0.3]

plt.figure(figsize = (8, 8))
plt.plot(x_h_10_h, u_y_h_10_h, 'k-', linewidth = 2, label = "U_y_h_10", color = "red")
#plt.plot(x_h_20_h, u_y_h_20_h, 'k-', linewidth = 2, label = "U_y_h_20", color = "green")
#plt.plot(x_h_30_h, u_y_h_30_h, 'k-', linewidth = 2, label = "U_y_h_30", color = "blue")
plt.plot(x_h_40_h, u_y_h_40_h, 'k-', linewidth = 2, label = "U_y_h_40", color = "orange")
#plt.plot(x_h_50_h, u_y_h_50_h, 'k-', linewidth = 2, label = "U_y_h_50", color = "black")
plt.plot(x_h_100_h, u_y_h_100_h, 'k-', linewidth = 2, label = "U_y_h_100", color = "brown")
plt.plot(x_h_200_h, u_y_h_200_h, 'k-', linewidth = 2, label = "U_y_h_200", color = "cyan")
plt.plot(x_h_300_h, u_y_h_300_h, 'k-', linewidth = 2, label = "U_x_h_300", color = "violet")
plt.plot(x1, y1, '-o', linewidth = 2, label = "Analytical/Numerical (dummy)", color = "skyblue")
plt.grid(True)
plt.legend()
plt.title("Horizontal Centerline (Vertical Velocities from left to right)")
plt.xlabel("x")
plt.ylabel("y velocity")
plt.minorticks_on()
plt.savefig('horizontal_Profile.png', dpi = 300, bbox_inches = 'tight')
plt.show()
