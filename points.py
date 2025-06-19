import math

def espelhar_ponto(x,y, quadrante):
   

    if quadrante == 1:
        return( abs(x), abs(y))
    elif quadrante == 2:
        return( -abs(x), abs(y))
    elif quadrante == 3:
        print(x, y, quadrante)
        return (-abs(x), -abs(y))
    elif quadrante == 4:
        return (abs(x), -abs(y))
    else:
        print("Quadrante inválido!")
        return None

def rotacionar_ponto(x, y, angulo):

    rad = math.radians(angulo)

    x_rot = x * math.cos(rad) - y * math.sin(rad)
    y_rot = x * math.sin(rad) + y * math.cos(rad)

    return (round(x_rot, 5), round(y_rot, 5))

def calcular_distancia(x1, y1, x2, y2):
   

    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distancia, 5)

import sys

def main():
    type = sys.argv[len(sys.argv) - 1]
    resultado = 0
    match type:
        case "espelhar":
           resultado=  espelhar_ponto(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        case "rotacionar":
          resultado=  rotacionar_ponto(int(sys.argv[1]),int(sys.argv[2]), int(sys.argv[3]))
        case "distancia":
           resultado= calcular_distancia(int(sys.argv[1]),int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
        case _:
            print("Comando desconhecido")
   
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
