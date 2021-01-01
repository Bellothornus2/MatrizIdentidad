# Dada una lista de lista representando una matriz n*n:
# Define una rutina que devuelve True si la entrada es una matriz indentidad
# y False en otro caso.

# Una matriz identidad es una matriz cuadrada en la que todos los elementos
# en la diagonal principal son 1 y el resto de elementos fuera de la
# diagonal principal son 0. 
# (Una matriz cuadrada es una matriz con el numero de filas
# igual al numero de columnas)
from src.code import es_matriz_identidad

# Casos test:
def test_simple_correcto():
    matrix1 = [[1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]]
    assert(es_matriz_identidad(matrix1)==True)
    #>>>True

def test_simple_incorrecto():
    matrix2 = [[1,0,0],
            [0,1,0],
            [0,0,0]]

    assert (es_matriz_identidad(matrix2) == False)
    
    #>>>False

def test_dos_incorrecto():
    matrix3 = [[2,0,0],
            [0,2,0],
            [0,0,2]]

    assert(es_matriz_identidad(matrix3) ==False)
    #>>>False

def test_no_diagonal_incorrecto():
    matrix6 = [[1,0,0,0],  
            [0,1,0,2],  
            [0,0,1,0],  
            [0,0,0,1]]

    assert(es_matriz_identidad(matrix6) == False)
    #>>>False

def test_uno_negativo_incorrecto():
    matrix7 = [[1, -1, 1],
            [0, 1, 0],
            [0, 0, 1]]
    assert(es_matriz_identidad(matrix7) == False)
    #>>>False           


# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert):

def test_no_cuadrado():
    matrix4 = [[1,0,0,0],
            [0,1,1,0],
            [0,0,0,1]]

    assert(es_matriz_identidad(matrix4) == AssertionError)
    #>>>False

def test_matriz_linear():
    matrix5 = [[1,0,0,0,0,0,0,0,0]]

    assert(es_matriz_identidad(matrix5) == AssertionError or False)
    #>>>False           