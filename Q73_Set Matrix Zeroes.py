class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if matrix is None:
            return None
        zeromark = []
        m = len(matrix)
        n = len(matrix[0])
        for col in range(0,m):
            for roe in range(0,n):
                if matrix[col][roe] == 0:
                    zeromark.append([col,roe])
        for i in zeromark:
            for j in range(0,m):
                matrix[j][i[1]] = 0
            for k in range(0,n):
                matrix[i[0]][k] = 0
                    
