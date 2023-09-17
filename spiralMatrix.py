def spiralOrder(matrix):
    result = []

    while matrix:
        result.extend(matrix[0])  # Add the first row
        print('result', result)
        # Rotate the remaining matrix counterclockwise
        matrix = list(zip(*matrix[1:]))[::-1]
        print("matrix", matrix)

    return result


spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
