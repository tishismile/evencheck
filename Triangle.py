import math

class Triangle():
    def __init__(self,a,b,c):
        self.length1 = a
        self.length2 = b
        self.length3 = c
    
    def perimeter(self):
        return self.length1 + self.length2 + self.length3
    
    def area(self):
        s = (self.length1+self.length2+self.length3)/2
        return math.sqrt(s*(s-self.length1)*(s-self.length2)*(s-self.length3)) 
    
    def scale(self, scale_factor):
        return Triangle(scale_factor*self.length1,scale_factor*self.length2,scale_factor*self.length3)
    
    def is_valid(self):
        if (self.length1+self.length2)>self.length3 and (self.length2+self.length3)>self.length1 and (self.length1+self.length3)>self.length2:
            return True
        else:
            return False

    def is_right(self):
        if (pow(self.length1,2)+pow(self.length2,2)==pow(self.length3) or pow(self.length2,2)+pow(self.length3,2)==pow(self.length1) or pow(self.length1,2)+pow(self.length3,2)==pow(self.length2)):
            return True
        else:
            return False

    
t = Triangle(3,3,5) 
print("Perimeter = %d" % t.perimeter())
print("Area = %f" % t.area())

q=t.scale(2)
print (q.length1,q.length2,q.length3)