from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    
    result = []
    top = 0
    bottom = len(matrix)
    left = 0
    right = len(matrix[0])
    
    while left < right and top < bottom:
        # Get every i in the top row
        for i in range(left, right):
            result.append(matrix[top][i])
        top += 1
        
        # Get every i in the rightmost column
        for i in range(top, bottom):
            result.append(matrix[i][right-1])
        right -= 1
        
        if not (left < right and top < bottom):
            break
            
        # Get every i in the bottom row
        for i in range(right-1, left-1, -1):
            result.append(matrix[bottom-1][i])
        bottom -= 1
        
        # Get every i in the leftmost column
        for i in range(bottom-1, top-1, -1):
            result.append(matrix[i][left])
        left += 1
    
    return result

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
matrix3 = [[1,2,3],[4,5,6],[7,8,9]]
matrix4 = [[1,2,3],[4,5,6],[7,8,9]]

ex1 = spiralOrder(matrix1)
print(ex1)


"""Wrong ans

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    ans = []
    for index, item in enumerate(matrix):
        
        if index % 2 == 0 or index == 0:
            for element in item:   
                    ans.append(element)
        if index % 2 != 0:
            for element in reversed(item):
                ans.append(element)
    return ans



"""

def spiralOrder1(matrix: List[List[int]]) -> List[int]:
    # Initialize result array
    ans = []
    
    # Continue while matrix has elements
    while matrix:
        # 1. Get top row: remove and add first row to result
        ans += (matrix.pop(0))
        
        # 2. Get right column: remove last element from each remaining row
        if matrix and matrix[0]:  # Check if matrix still has elements
            for row in matrix:
                ans.append(row.pop())  # Remove and add last element of each row

        # 3. Get bottom row: remove last row and add it in reverse
        if matrix:  # Check if matrix still has rows
            ans += (matrix.pop()[::-1])  # [::-1] reverses the list
        
        # 4. Get left column: remove first element from each remaining row (bottom to top)
        if matrix and matrix[0]:  # Check if matrix still has elements
            for row in matrix[::-1]:  # Traverse rows from bottom to top
                ans.append(row.pop(0))  # Remove and add first element of each row
                
    return ans

print(spiralOrder1(matrix1))




def spiralOrder2(matrix: List[List[int]]) -> List[int]:
    ans = []
    
    while matrix:
        ans += (matrix.pop(0))
        
        if matrix and matrix[0]:
            for row in matrix:
                ans.append(row.pop())
            
        if matrix:
            ans += (matrix.pop()[::-1])
        
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ans.append(row.pop(0))
    return ans
    
ex3 = spiralOrder2(matrix2)
print(ex3)

def spiral_order(matrix: List[List[int]]) -> list[int]:
    ans = []
    
    while matrix:
        ans += matrix.pop(0)
        
        if matrix and matrix[0]:
            for row in matrix:
                ans.append(row.pop())
        if matrix:
            ans += (matrix.pop()[::-1])
            
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ans.append(row.pop(0))
    return ans

print(spiral_order(matrix3))



def spiral(matrix: List[List[int]]) -> List[int]:
    ans = []
    
    while matrix:
        ans += (matrix.pop(0))
    
    if matrix and matrix[0]:
        for row in matrix:
            ans.append(row.pop())
    
    if matrix:
        ans += (matrix.pop(0)[::-1])
    
    if matrix and matrix[0]:
        for row in matrix[::-1]:
            ans.append(row.pop(0))
            
    return ans


matrix5 = [[1,2,3],[4,5,6],[7,8,9]]
def spiraldammit(matrix: List[List[List]]) -> List:
    ans = []
    while matrix:
        ans += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                ans.append(row.pop())
        if matrix:
            ans += matrix.pop()[::-1]
        
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ans.append(row.pop(0))
    return ans
print("Damn")
print(spiraldammit(matrix5))
                

