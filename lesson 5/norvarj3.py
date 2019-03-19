import pandas as pd
import matplotlib.pyplot as plt
dzaynner = {'anunov':['soprano', 'bass', 'alt'],
'tverov':[15, 16, 17]}
a = pd.DataFrame(dzaynner)
print(a)
b= pd.DataFrame(dzaynner, index=['one','two','three'])
a.plot.bar()
b.plot()
plt.show()