def get_matrix (n, m, value):
    matrix = []
    for i in range (n):
        matrix.append([])
        for j in range (m):
            matrix[i].append(value)
        #print (matrix)
    return matrix
result1 = get_matrix(2, 4, 6)
result2 = get_matrix(-2, 5, 42) # при значении аргумента <= 0 возвращается пустой список. Ч.т.д.
result3 = get_matrix(4, 1, "win")
print(result1)
print(result2)
print(result3)