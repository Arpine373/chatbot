class Mtqer:
    '''This  class  describe mtqer'''
    def __init__(self,thexeloq,theankap,thefantazianer):
        self.xeloq=thexeloq
        self.ankap=theankap
        self.fantazianer=thefantazianer
    def __str__ (self):
        return  str(self.fantazianer)

    __repr__= __str__
mitq1=Mtqer('change the  world','dont  worry  be  happy','flying')
mitq2=Mtqer('be thankfull','be critic','climbing')
mtqer=[]
mtqer.append(mitq1)
mtqer.append(mitq2)
def  xmbavorel(mtqer):
    xumb1=[]
    xumb2=[]
    for mitq in  mtqer:
        if mitq.xeloq[0]=='c':
            xumb1.append(mitq)
        else:
            xumb2.append(mitq)
     
    print('xumb1: ', xumb1)
    print('xumb2: ', xumb2)

xmbavorel(mtqer)
