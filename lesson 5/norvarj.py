import pandas as pd
orer = {'anunov':['Monday', 'Thuesday', 'Wednesday'],
'tverov':[15, 16, 17]}
a = pd.DataFrame(orer)
print(a)
b= pd.DataFrame(orer, index=['one','two','three'])
print(b.loc['two'])
print(b.iloc[0])