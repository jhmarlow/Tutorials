# Import the necessary packages and modules
import numpy as np
import matplotlib.pyplot as plt

# Prepare the data
array = np.random.random((36, 36))
array1 = np.random.random((36, 10))
x = [1,2,4,5,6]
y = [1,2,3,3,6]

myFile = np.genfromtxt('Stock.csv', delimiter=',')

plt.plot(x,y,'r')
plt.ylabel('Speed (m/s)')
plt.xlabel('Time (s)')

# Plot the data
fig = plt.figure()
fig.suptitle("Title for whole figure", fontsize=16)
ax = plt.subplot("311")
ax.set_title("Title for first plot")
ax.plot(x,y,'rx')

plt.subplot(312)
plt.plot(array[0],array[1],'rx')
plt.ylabel('some numbers')
plt.xlabel('some numbers')

plt.subplot(313)
plt.plot(x,y,'b--')
plt.ylabel('some numbers')
plt.xlabel('some numbers')

# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6 * np.pi, 300)
y = np.cos(x)
W = np.where( y > 0.5 )

plt.plot(x[W],y[W],'r-')

y1 = np.ma.masked_where(y > 0.7, y)

y2 = y.copy()
y2[y > 0.5] = np.nan

fig, axes = plt.subplots(nrows=3, sharex=True, sharey=True)
for ax, ydata in zip(axes, [y, y1, y2]):
    ax.plot(x, ydata)
    ax.axhline(0.5, color='red')
    ax.axhline(0.7, color='green')

axes[0].set_title('Original')
axes[1].set_title('Masked Arrays')
axes[2].set_title("Using NaN's")

fig.tight_layout()

plt.show()

x = [5,1,7,0,3,4]
print(x.index(7))