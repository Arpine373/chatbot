import matplotlib.pyplot as plt
fig = plt.figure() #sarqel Figure tipi obekt
ax1 = fig.add_subplot(211) #avelacnum  em Axis  tipi obyekt figin
ax1.plot([6, 2, 0, 4], [9, 20, 15, 18], color='lightblue', linewidth=3)
ax1.set_xlim(0.5, 4.5)
ax2 = fig.add_subplot(212)
ax2.scatter([0.3, 4.9, 1.2, 2.5], [1, 5, 9, 2], color='darkgreen', marker='^')
ax2.set_xlim(1.5, 3.5)
plt.show()
plt.savefig("one.png")
