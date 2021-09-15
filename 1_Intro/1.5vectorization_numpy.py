''' Vectorizing alg '''
from numpy import sqrt,sin,arange
from math import pi
import matplotlib.pyplot as plt
x = arange(0.0, 1.001*pi, 0.01*pi)
y = sqrt(x)*sin(x)
print(y)
plt.plot(x,y)
plt.show()
