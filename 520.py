from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-1.75,1.75,1000)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.xlim(-2,2)
plt.ylim(-1.5,2.5)
plt.ion()
for i in range(1,1000):
    y = np.sin(i/10 * np.pi * (x)) * np.e / 3 * (np.pi -x**2) ** 0.5 + np.abs(x) ** (2/3)
    lines = ax.plot(x,y)
    plt.pause(0.05)
    plt.title("surprise")
    ax.lines.remove(lines[0])

