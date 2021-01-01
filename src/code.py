def es_matriz_identidad(matriz):
    try:
        assert len(matriz[0]) == len(matriz) and isinstance(matriz, list)
    except AssertionError:
        return AssertionError

    length_matriz_row = len(matriz)
    acumulator = 0
    answer = None

    for i in range(length_matriz_row**2):
        matriz_index = int(i/length_matriz_row)
        result = matriz[matriz_index][acumulator]
        if matriz_index == acumulator and result == 1 or matriz_index != acumulator and result == 0:
            answer = True
        #elif matriz_index == acumulator and result != 1 or matriz_index != acumulator and result != 0:
        else:
            answer = False
            break
        acumulator += 1
        if acumulator == length_matriz_row:
            acumulator = 0
    return answer
        