'''
Time Complexity O(N+E)
	where N = number fo Nodes and E = Number of edges

Space complexity also O(N+E) as storing the Adjacency List
'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create Adjacency List
        adjList = {i:[] for i in range(numCourses)}
        
        for s, d in prerequisites:
            adjList[s].append(d)  #directed graph
        
        
        visited = {i:0 for i in range(numCourses)}

        def dfs(s):
            print(s)
            #base case
            if visited[s] == 1:     #indicates a loop in the dfs subtree
                return False
            if adjList[s] == []:    #indicates a course with no prerequisites so DFS of that subtree works
                return True
            
            visited[s] = 1
            for ngb in adjList[s]:  #loop through Fringe Edges
                if dfs(ngb) == False:
                    return False
            visited[s] = 0
            adjList[s] = []   #important as this ensures that we will not investigate a Node if it was investigated before
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True