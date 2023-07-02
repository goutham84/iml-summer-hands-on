#if importing libraries shows error then install the library using pip
import numpy as np  #importing the requireed libraries
import matplotlib.pyplot as plt

N=50 #number of points
S=np.arange(1,N+1) #s values from 1 to 50
theta=np.linspace(0.1,0.9,100) #100 values of theta between 0.1 to 0.9
s_gird,theta_grid=np.meshgrid(S,theta)
L= s_gird * np.log(theta_grid)+(N-s_gird)*np.log(1-theta_grid) #funtion defination for plot
fig=plt.figure() #to plot in figure
ax=fig.add_subplot(111, projection='3d')
s=ax.plot_surface(s_gird, theta_grid, L,cmap='jet')
ax.set_xlabel('S') #labelling the axses
ax.set_ylabel("theta")
ax.set_zlabel("L(theta|S")
ax.view_init(65,15)   #initialise angle of view
#plt.show()
plt.savefig('03-mle-python-s-theta-L.png') ##Saving the figure 

