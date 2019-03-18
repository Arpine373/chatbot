import pandas as pd
organner = {'anunov':['sirt', 'uxex', 'toq'],
'tverov':[15, 16, 17]}
a = pd.DataFrame(organner)
print(a)
print(a.sum())
b= pd.DataFrame(organner, index=['one','two','three'])
print(b.loc['two'])
print(b.iloc[1])