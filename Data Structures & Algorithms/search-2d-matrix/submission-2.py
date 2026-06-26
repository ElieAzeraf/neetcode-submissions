class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        b1, e1 = 0, len(matrix) - 1
        while e1 >= b1:
            m1 = (b1 + e1) // 2

            if target == matrix[m1][0] or target == matrix[m1][-1]:
                return True

            elif target > matrix[m1][0] and target < matrix[m1][-1]:
                c = m1
                break

            elif target > matrix[m1][0]:
                c = m1 + 1
                b1 = m1 + 1

            else:
                e1 = m1 - 1

        
        b2, e2 = 0, len(matrix[c]) - 1
        while e2 > b2:
            m2 = (b2 + e2) // 2
            if matrix[c][m2] == target:
                return True

            elif matrix[c][m2] < target:
                b2 = m2 + 1
            
            else:
                e2 = m2 - 1

        return False
                
        