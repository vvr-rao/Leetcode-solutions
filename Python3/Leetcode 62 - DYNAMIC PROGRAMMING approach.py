'''
compute number of unique paths in a grid. Robot can only more DOWN or RIGHT
Using DYNAMIC PROGRAMMING with Bottom-Up Approach.
Assume the sum of ways to get to any square can be got by adding the squares immediately above and too the left 


TIME COMPLEXITY - O(m * n) - you traverse through all elements in the gris
SPACE COMPLEXITY - O(n) - this is because I only store 2 rows for the compute

'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Base Case 1 - first row (row 0)is 1 for all columns
        lastEvenRow = [1 for i in range(n)]    #store the values for each odd row - 0,2,4,6       
        lastOddRow = [None for i in range(n)]     #store the values for each odd row - 1,3,5,7
        currRow = [0 for c in range(n)]
        #print (lastEvenRow)
        
        if (m ==0) or m==1:   # Edge Case
            return m
        #Base Case 2 - first column is 1 for all rows
        
        for i in range(1, m):  
            currRow = [0 for c in range(n)]
            currRow[0] = 1  #Base Case 2
            for j in range(1, n):
                if (i % 2) == 1:  # Curr Row is Odd Row
                    currRow[j] = currRow[j-1] + lastEvenRow[j]
                else:               # Curr Row is Even
                    currRow[j] = currRow[j-1] + lastOddRow[j]
            if (i % 2) == 1:  # Curr Row is Odd Row
                lastOddRow = currRow
            else:   # Curr Row is Even
                lastEvenRow = currRow
            #print(currRow)
        return currRow[n-1]
        
