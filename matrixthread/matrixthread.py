import threading

matrixA = [[1, 2], [3, 4]]
matrixB = [[5, 6], [7, 8]]


def calculate_element(row, col):
    result = 0

    for i, item in enumerate(row):
        result += item * col[i]
    return result


def calculate_row(rowA, matrixB):
    cols = [[row[i] for row in matrixB] for i in range(len(matrixB[0]))]
    result = list(map(lambda x: calculate_element(rowA, x), cols))
    print(result)
    return result


for row in matrixA:
    threading.Thread(target=calculate_row, args=(row, matrixB)).start()