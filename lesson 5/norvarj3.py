import pandas as pd
dzaynner = {'anunov':['soprano', 'bass', 'alt'],
'tverov':[15, 16, 17]}
a = pd.DataFrame(dzaynner)
print(a)
b= pd.DataFrame(dzaynner, index=['one','two','three'])
print(a.plot.bar())
print(b.plot())