class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        '''
        Will use DFS to check for BiPartition
        Time Complexity O(n+e)
        Space Complexity:
        
        Example Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
        '''
        
        adjList = {i:[] for i in range(1,n+1)}
        for i in range(len(dislikes)):
            adjList[dislikes[i][0]].append(dislikes[i][1])
            adjList[dislikes[i][1]].append(dislikes[i][0])
        
        #added - 0 if not added. If not I will assign groups of -1 or 1
        added = {i:0 for i in range(1, n+1)}
        visited = {i:False for i in range(1, n+1)}
        
        def dfs(curr, grp): #grp = -1 or 1
            added[curr] = grp
            visited[curr] = True
            
            for ngb in adjList[curr]:
                if added[ngb] == grp:   #found neighbor in same loop
                    return False
                else:
                    if visited[ngb] == False:
                        if dfs(ngb, -1*grp) == False:
                            return False
            visited[curr] = False
            adjList[curr] = []  # VERY IMPORTANT!!
            return True
        
        for i in range(1, n+1):
            if added[i] == 0:
                if dfs(i,1) == False:
                    return False
        
        return True
                
                
                
                
                
            