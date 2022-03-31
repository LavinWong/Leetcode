class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
         def spiralOrder(self, matrix):
        col_len = len(matrix[0])
        row_len = len(matrix)
        i,j,result = 0,0,[]
        result.append(matrix[i][j])
        matrix[i][j] = 101
        process = True
        while process:
            process = False
            
            # Move right
            while(j+1<col_len and matrix[i][j+1] != 101):
                j+=1
                result.append(matrix[i][j])
                matrix[i][j] = 101
                process = True
                
            # Move down
            while(i+1<row_len and matrix[i+1][j] != 101):
                i+=1
                result.append(matrix[i][j])
                matrix[i][j] = 101
                process = True
                
            # Move left
            while(j-1>=0 and matrix[i][j-1]!=101):
                j-=1
                result.append(matrix[i][j])
                matrix[i][j] = 101
                process = True
                
            # Move up
            while(i-1>=0 and matrix[i-1][j]!=101):
                i-=1
                result.append(matrix[i][j])
                matrix[i][j] = 101
                process = True
            
        return result
