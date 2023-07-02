import cv2 as cv #importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
lambd = cv.imread('moon.tif') #performing MLE on moon.tif file can be found here:https://people.math.sc.edu/Burkardt/data/tif/tif.html
lambd = cv.cvtColor(lambd, cv.COLOR_BGR2GRAY)/255
T = 100
lambdT = np.repeat(lambd[:, :, np.newaxis], T, axis = 2)
x = stats.poisson.rvs(lambdT)
y = (x>=1).astype(float)
lambdhat = -np.log(1-np.mean(y,axis=2))
plt.imshow(lambdhat, cmap='gray')
#plt.show()
plt.savefig('05b-mle-moon-env.png') #Saving the figure 