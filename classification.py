class Song:
    '''This  class  describe  song'''
    def __init__(self,thename,thelength,thejanr):
        self.name=thename
        self.length=thelength
        self.janr=thejanr
jazz=Song('Blues',10,'jaz')
rockandroll=Song('Elvis',25,'rock and roll')
def  stugel(song):
    if song.name[0]=='B'  and song.length>=2 and song.janr[0]=='j':
        print('It  is  jazz')
    elif song.name[0]=='E' and song.length>=3  and song.janr[0]=='r':
        print(' It  is  rockandroll')
    else:
        print('other  janr')
stugel(jazz)
stugel(rockandroll)