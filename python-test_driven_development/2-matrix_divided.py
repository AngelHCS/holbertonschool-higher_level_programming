#!/usr/bin/python3
#2-matrix_divided.py
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
matrix (list of lists): The matrix to be divided. Each element of the matrix
                                must be an integer or a float.
div (int or float): The divisor by which to divide all elements of the matrix.

    Returns:
list of lists: A new matrix where each element is the result of dividing the
corresponding element in the original matrix by the divisor.
The result is rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a list of lists of integers or floats,
    if each row of the matrix does not have the same size, or
    if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    if not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
