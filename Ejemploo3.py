

def rectangulo(ancho, largo):
    resultado_rectangulo = ancho * largo
    return resultado_rectangulo

def triangulo(base_triangulo, altura_triangulo):
    resultado_triangulo = 0.5 * base_triangulo * altura_triangulo
    return resultado_triangulo


def principal():
    base_rectangulo = 4
    altura_rectangulo = 6
    print(f"\n Área del rectángulo:", rectangulo(base_rectangulo,altura_rectangulo))

    base_triangulo = 5
    altura_triangulo = 8
    print("\n Área del triángulo:", triangulo(base_triangulo,altura_triangulo))

principal()

