class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)       # now rows
        n = len(obstacleGrid[0])    # num cols
        lastEvenRow = [0]*n
        lastOddRow = [None for i in range(n)]
        fstRwBlk = False
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                if m==1:
                    return 0
                break;
            else:
                lastEvenRow[i] = 1
                
        print(lastEvenRow)
        #print(lastOddRow)
        
        if (m==0):
            return m
        if m==1:
            return 1

        
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        
        currRow = [0]*n
        FstColBlk = False
        for i in range(1,m):    #iterate through rows
            currRow = [0]*n
            lft, rgt = 0, 0
            if obstacleGrid[i][0] == 1:
                FstColBlk = True
            if FstColBlk == False:
                currRow[0] = 1
            for j in range(1,n):    #iterate through columns
                if obstacleGrid[i][j-1] == 0:
                    lft = currRow[j-1]
                else:
                    lft = 0
                if obstacleGrid[i-1][j] == 1:
                    rgt = 0
                else:
                    if (i % 2) == 1:  # Curr Row is Odd Row
                        rgt = lastEvenRow[j]
                    else:
                        rgt = lastOddRow[j]
                currRow[j] = lft + rgt
            
            
            if (i % 2) == 1:  # Curr Row is Odd Row
                lastOddRow = currRow
            else:   # Curr Row is Even
                lastEvenRow = currRow
            
        return currRow[n-1]
        