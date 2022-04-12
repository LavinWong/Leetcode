class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        # PART 2:
        #
        # Here we are "sinking" the island by traversing the grid DFS
        # 
        # We are checking if:
        #   - The row is within range of the rows (len(grid))
        #   - The cols is within range of the cols (len(grid[0]))
        #   - Is this land ("1") or water ("0") ?
        # 
        # If the point is on the grid and its land we need to check all the cardinal
        # directions to see if the land extends further
        #
		# North = dfs(r, c - 1)
		# South = dfs(r, c + 1)
		# East = dfs(r + 1, c)
        # West = dfs(r - 1, c)
        #
        # This will run recursivley till we have hit all water or out of bounds of the grid
        # PS: make sure you are checking and marking as strings and not integers
        # the grid is strings
        def dfs( r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return None
            
            grid[r][c] = "0"
            dfs(r, c - 1)
            dfs(r, c + 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
            
        # PART 1:
        #
        # The approach for this problem is as follows, if we run into the string 1
        # we are on an island and need to increment our counter (res).
        #
        # Now that we know we are on an island we need to sink it, sinking it means
        # we will set the current and all the neighboring positions to the string 0 so that we know
        # once we get there that it is not a new island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r,c)
        
        # Return out counter
        return res
        
