from typing import List

def diagonalSum(mat: List[List[int]]) -> int:
    n = len(mat)
    total_sum = 0

    for i in range(n):
        # Add the primary diagonal element
        total_sum += mat[i][i]
        # Add the secondary diagonal element only if it's not the same as the primary diagonal element
        if i != n - i - 1:
            total_sum += mat[i][n - i - 1]

    return total_sum

# Example matrices
mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat2 = [ 
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

mat3 = [
    [5]
]

# Test the function
print(diagonalSum(mat1))  # Output: 25
print(diagonalSum(mat2))  # Output: 8
print(diagonalSum(mat3))  # Output: 5
