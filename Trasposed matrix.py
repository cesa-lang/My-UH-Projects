matrix = [[1,2,3],[4,5,6],[7,8,9]]

trasposed_matrix = [[matrix[fila][componente]for fila in range(len(matrix))] for componente in range(len(matrix))]

trasposed_matrix = []

for fila in range(len(matrix)):
    new_list = []
    for componente in range(len(matrix)):
        new_list.append(matrix[componente][fila])
    trasposed_matrix.append(new_list)

print(trasposed_matrix)