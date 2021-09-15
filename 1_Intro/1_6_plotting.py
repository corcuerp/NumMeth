''' 1.6 Plotting with matplotlib.pyplot '''
import matplotlib.pyplot as plt
from numpy import arange,sin,cos

x = arange(0.0,6.2,0.2)
plt.plot(x,sin(x),'o-',x,cos(x),'^-') # Plot with specified
                                      # line and marker style
plt.xlabel('x')                       # Add label to x-axis
plt.legend(('sine','cosine'),loc = 0) # Add legend in loc. 3
plt.grid(True)                        # Add coordinate grid
plt.savefig('testplot.png',format='png') # Save plot in png
                                         # format for future use
plt.show()                            # Show plot on screen          

# more than one plot in a figure
plt.subplot(2,1,1)
plt.plot(x,sin(x),'o-')
plt.xlabel('x');plt.ylabel('sin(x)')
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(x,cos(x),'^-')
plt.xlabel('x');plt.ylabel('cos(x)')
plt.grid(True)
plt.show()
    
