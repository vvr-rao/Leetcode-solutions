'''
Topological Sort

Time Complexity - O(N+E)
Space - O(N+E)
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #create Adjacency List
        adjList = {i:[] for i in range(numCourses)}
        for s,d in prerequisites:
            adjList[s].append(d)
        
        
        visited = {i:0 for i in range(numCourses)}
        added = {i:0 for i in range(numCourses)}
        output = []
        def dfs(s):
            if visited[s] == 1:     #found a loop in current dfs loop
                return False
            if added[s] == 1:    #found a node which has already been added
                return True
            
            visited[s] = 1
            for ngb in adjList[s]:
                if dfs(ngb) == False:
                    return False        #just return False up the chain. will return an empty array atthe root
            output.append(s)
            visited[s] = 0
            added[s] = 1
            adjList[s] = []
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return[]
            
        return output