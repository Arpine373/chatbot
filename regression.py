class  Organizm:
    '''This  class  describe  organizm'''
    def __init__(self,theheartbeat,theplastic,theage):
        self.heartbeat=theheartbeat
        self.plastic=theplastic
        self.age=theage
organizm1=Organizm(100,180,20)
organizm2=Organizm(80,90,30)
def stugel(organizm):
    a= (organizm.heartbeat+organizm.plastic+organizm.age)/3
    if a>=10:
        print('organizm  is  healthly')
    else:
        print('dimackun  chi')
stugel(organizm1)
stugel(organizm2)