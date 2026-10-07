class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        output = []
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1

        while top<=bottom and left<=right:

            for i in range(left, right+1):
                output.append(matrix[top][i])
            top+=1
            for j in range(top, bottom+1):
                output.append(matrix[j][right])
            right-=1
            if top<=bottom:
                for k in range(right, left-1, -1):
                    output.append(matrix[bottom][k])
                bottom-=1
            if left<=right:
                for l in range(bottom, top-1, -1):
                    output.append(matrix[l][left])
                left+=1

        return output

'''
Approach
Use four boundaries to keep track of the unvisited portion of the matrix:
- top → topmost remaining row
- bottom → bottommost remaining row
- left → leftmost remaining column
- right → rightmost remaining column
Traverse the matrix in four directions:
1. Left → Right across the top row, then top += 1
2. Top → Bottom down the right column, then right -= 1
3. Right → Left across the bottom row, then bottom -= 1
4. Bottom → Top up the left column, then left += 1
The process continues while:
top <= bottom and left <= right


The extra boundary checks prevent already-visited rows or columns from being traversed again.
Algorithm
1. Initialize top, bottom, left, and right.
2. While the boundaries are valid:
   - Traverse the top row from left to right.
   - Move top inward.
   - Traverse the right column from top to bottom.
   - Move right inward.
   - If a bottom row remains, traverse it from right to left.
   - Move bottom inward.
   - If a left column remains, traverse it from bottom to top.
   - Move left inward.
3. Return output.
Time Complexity
O(m × n)
Every element of the matrix is visited exactly once.
Where:
- m = number of rows
- n = number of columns
Space Complexity
O(m × n)
The output list stores all m × n elements.
Auxiliary space: O(1) — apart from the output list.

'''