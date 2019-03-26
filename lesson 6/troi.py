import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
ax.plot([1,2],[3,4], color='lightblue',label='Arpi')
plt.show()
plt.savefig('one.png')