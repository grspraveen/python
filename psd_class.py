
class circle(object):
    def __init__(self, radius=3):
        self.radius=radius
     
    def area(self,radius):
        return(3.14*radius*radius)


class rectangle(object):
    def __init__(self,length, width):
        self.length=length
        self.width=width
        
    def area(self,length,width):
        return(length*width)


c1=circle(12)
print(c1)


