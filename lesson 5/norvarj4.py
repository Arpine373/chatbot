import pandas as pd
mazer = {'anunov':['erkar', 'karj', 'mijin'],
'tverov':[1105, 1206, 1327]}
a = pd.DataFrame(mazer)
print(a)
b= pd.DataFrame(mazer, index=['one','two','three'])
a.to_csv('file.csv')
pd.read_csv('file.csv',sep=',')