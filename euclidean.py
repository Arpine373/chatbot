import  math
a='aiopyu'
b='aiop'
ord('g')
aitverivektor=[]
bitverivektor=[]
for  simvol  in a:
    aitverivektor.append(ord(simvol))
print('tpum  em  ai  tveri  vektor',aitverivektor)
for simvol  in  b:
    bitverivektor.append(ord(simvol))
print('tpum  em  bi  vektor',bitverivektor)
erkarutyun=0
if  len(a)<len(b):
    erkarutyun=len(a)
else:
    erkarutyun=len(b)
sum=0
for  index  in  range(erkarutyun):
   sum=sum+ (bitverivektor[index]-aitverivektor[index])**2
print('tpum  em  gumary ',sum)
result=math.sqrt(sum)
print('tpum em  ardyunq ',result)