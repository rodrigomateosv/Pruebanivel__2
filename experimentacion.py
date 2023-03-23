import database as db
import helpers


def main():

    helpers.limpiar_pantalla()

    print("Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla")
    A = db.Punto(2, 3)
    B = db.Punto(5, 5)
    C = db.Punto(-3, -1)
    D = db.Punto(0, 0)
    print(" A{}, B{}, C{}, D{}".format(A,B,C,D))

    print("Imprime por pantalla el cuadrante al que pertenece el punto A, B, C y D")
    print(A.cuadrante())
    print(B.cuadrante())
    print(C.cuadrante())
    print(D.cuadrante())

    print("Crea los vectores AB y BA e imprimelos por pantalla")
    A.vector(B)
    B.vector(A)

    print("Distancia entre  los vectores A y B, B y A e imprimelos por pantalla")
    A.distancia(B)
    B.distancia(A)

    print(" Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0)")
    if A.distancia(D) > B.distancia(D) and A.distancia(D) > C.distancia(D):
        print("A es el punto más lejano")
    if B.distancia(D) > A.distancia(D) and B.distancia(D) > C.distancia(D):
        print("B es el punto más lejano")
    if C.distancia(D) > A.distancia(D) and C.distancia(D) > B.distancia(D):
        print("C es el punto más lejano")
    
    print("Crea el rectángulo de vértices A y B e imprimelo por pantalla")
    rectangulo = db.Rectangulo(A, B)
    print(rectangulo)

    print("consulta la base, altura y area del rectangulo")
    print(rectangulo.base())
    print(rectangulo.altura())
    print(rectangulo.area())