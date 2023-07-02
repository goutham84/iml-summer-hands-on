#Importing the required libraries
#if importing libraries shows error then install the library using pip
import numpy as np
import matplotlib.pyplot as plt

n = 50 #taking n=50
S = np.arange(1, n+1)
theta = np.linspace(0.1, 0.9, 100)  #theta 100 values between 0.1 and 0.9
s_grid, theta_grid = np.meshgrid(S, theta)
L = s_grid * np.log(theta_grid) + (n- s_grid) * np.log(1 - theta_grid) #L function defining

fig = plt.figure(figsize=(12, 5)) #figure size declaring

# plotting the 3D surface plot with plane at s=25
ax1 = fig.add_subplot(121, projection='3d')
s = ax1.plot_surface(s_grid, theta_grid, L, cmap='jet') #3D plot
ax1.set_xlabel('S')    #labelling the axis
ax1.set_ylabel('theta')
ax1.set_zlabel('L(theta|S)')
ax1.view_init(65, 15)  #the view angle for the 3d plot, current view angle can be changed later

# Creating the plane at s=25 between L and theta at s=25,
s_plane = np.ones_like(theta) * 25
ax1.plot(s_plane, theta, L[:, 24], color='black', linestyle='--') # the plane features with blackcolor

# theta vs L plot at s=25 
s_index = 24  # Index of s=25 in the S array (since it starts from 1)
L_s25 = L[:, s_index]
ax2 = fig.add_subplot(122)
ax2.plot(theta, L_s25)
ax2.set_xlabel('theta')
ax2.set_ylabel('L(theta|S)')
ax2.set_title('theta vs L at s=25')

plt.tight_layout()
plt.savefig('04a-mle-python-surface-bd-exr.png') ##Saving the figure 
#plt.show()
