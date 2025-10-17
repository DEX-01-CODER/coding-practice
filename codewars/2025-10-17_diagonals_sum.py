# Date: 2025-10-17
# Platform: Codewars
# Problem: Diagonals Sum (7 kyu)
# Link: https://www.codewars.com/kata/diagonals-sum
# Category: Matrix / Algorithms
# Approach: One-pass O(n) iteration over both diagonals

def sum_diagonals(matrix):
    j = len(matrix)
    main_diagonal = 0
    secondary_diagonal = 0
    for i in range(len(matrix)):
        main_diagonal += matrix[i][i]
        secondary_diagonal += matrix[i][j - 1 - i]
    return main_diagonal + secondary_diagonal


# Sample test
print(sum_diagonals([[1,2,3],[4,5,6],[7,8,9]]))  # Expected 30
