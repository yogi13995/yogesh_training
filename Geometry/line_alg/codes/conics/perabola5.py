# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
# Create the vectors X and Y
x = np.linspace(-5,5,300)
y = 6*x ** 2  -7*x - 3

P1= np.array([1.5, 0])
Q1 = np.array([-0.33, 0])
plt.plot(P1[0],P1[1],'o')
plt.text(P1[0]*(1+0.1), P1[1]*(1-0.1), '\u03B1')
plt.plot(Q1[0],Q1[1],'o')
plt.text(Q1[0]*(1-0.2), Q1[1]*(1), '\u03B2')

# Create the plot
plt.plot(x,y,label='y =6*x ** 2  -7*x - 3')

# Add a title
plt.title('')

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=1,linestyle='--')

# Add a Legend
plt.legend()
plt.savefig('../../figures/conics/perabola5.eps')
# Show the plot
plt.show()
