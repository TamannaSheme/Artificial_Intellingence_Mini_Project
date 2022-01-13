import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#first creating the grid with x values and y values running from -200 to 200
x = np.linspace(-200, 200)
y = np.linspace(-200, 200)
#get x,y values from the grid
x, y = np.meshgrid(x, y)

#plot the x and Y axis
plt.axhline(0, alpha=.1)
plt.axvline(0, alpha=.1)

#set a and b value according to the hyperbolic equation
a =49
b =32

#plot hyperbolic equation
plt.contour(x, y,(y**2/a**2 - x**2/b**2) ,[1])
#add title
plt.title("HYPERBOLA\n\nEquation : y^2/49^2 - x^2/3^2 = 1")
#display the plot
plt.show()
