
class patrat:
    def __init__(self,muve_impuls,muve_stimul,
                 speed,size,x,y):
        self.muve_impuls=muve_impuls
        self.muve_stimul=muve_stimul

        self.color=((muve_impuls[0]+muve_impuls[1])/4*225,(muve_impuls[2]+muve_impuls[3])/4*225,muve_impuls[4]/2*225)
        self.speed=speed
        self.size=size
        self.x=x
        self.y=y

        
