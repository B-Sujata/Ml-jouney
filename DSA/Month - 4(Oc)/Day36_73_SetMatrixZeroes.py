class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = []
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value==0:
                    zeroes.append((i,j))
        
        for i, j in zeroes:
                    
            for k in range(len(matrix[i])):
                matrix[i][k]=0
            for l in range(len(matrix)):
                matrix[l][j]=0

'''
Approach
The solution uses a two-phase approach:
1. Traverse the matrix and store the row and column indices of all original zeroes in a list.
2. Traverse the stored zero positions and set their entire corresponding rows and columns to zero.
This prevents newly-created zeroes from affecting the detection process.
Algorithm
1. Create an empty list `zeroes`.
2. Traverse every element of the matrix.
3. Whenever an element is 0, store its `(row, column)` position.
4. After completing the traversal, iterate through `zeroes`.
5. For every stored `(i, j)`:
   - Set every element in row `i` to 0.
   - Set every element in column `j` to 0.
6. Modify the matrix in-place.

Complexity
Let m = number of rows and n = number of columns.
Time Complexity: O(m × n)
- Finding all zeroes: O(m × n)
- Zeroing rows and columns: in the worst case, still O(m × n) overall.
Space Complexity: O(m × n)
In the worst case, every element could be zero, so zeroes could contain m × n positions.
Final:
	Complexity
Time	O(m × n)
Space	O(m × n)

'''