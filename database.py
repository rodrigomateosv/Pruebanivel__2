import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return 0
        
    def vector(self, punto):
        
        coordenada_x = punto.x - self.x
        coordenada_y = punto.y - self.y
        print("El vector entre {} y {} es ({} , {})").format(self,punto,punto.x-self.x,punto.y-self.y)
              
    def distancia(self, punto):
       d= math.sqrt( (punto.x-self.x)**2 + (punto.y-self.y )**2)
       print("La distancia entre {} y {} es {}").format(self,punto,d) 

class Rectangulo:
    def __init__(self, p1=Punto(), p2=Punto()):
        self.p1 = p1
        self.p2 = p2

    def base(self):
        return abs(self.p1.x - self.p2.x)

    def altura(self):
        return abs(self.p1.y - self.p2.y)

    def area(self):
        return self.base() * self.altura()
    
A= Punto(2,3)
B= Punto(5,5)
C= Punto(-3,-1)
D= Punto(0,0)
