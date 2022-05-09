import math

class Triangle():
    def __init__(self,a,b,c)
        self.length1 = a
        self.lenght2 = b
        self.lenght3 = c
    
    def perimeter(self):
        return self.length1 + self.lenght2 + self.lenght3
    
    def area(self):
        s = (self.length1+self.lenght2+self.lenght3)/2
        return math.sqrt(s*(s-self.length1)*(s-self.lenght2)*(s-self.lenght3)) 
    
    def scale(self, scale_factor)
        return (scale_factor*self.length1,scale_factor*self.lenght2,scale_factor*self.lenght3)
    
    def is_valid(self):
        if (self.length1+self.lenght2)>self.lenght3 and (self.lenght2+self.lenght3)>self.length1 and (self.length1+self.lenght3)>self.lenght2:
            return True
        else:
            return False

    def is_right(self):
        if (pow(self.lenght1,2)+pow(self.lenght2,2)==pow(self.lenght3) or pow(self.lenght2,2)+pow(self.lenght3,2)==pow(self.lenght1) or pow(self.lenght1,2)+pow(self.lenght3,2)==pow(self.lenght2):
            return True
        else:
            return False

    
t = Triangle(3,3,5) 
print("Perimeter = %d" % t.perimeter())
print("Area = &d" % t.area())

q=t.scale(2)
print (t.length1,t.lenght2,t.lenght3)