'''
Leetcode 269 - given an array of sorted words in an alien language, find the order of the letters


Approach
1) Use Topological SOrt with DFS to get the order
2) TO get that I needed to create an Adjacency List.  Looped through each pair of word in the input array - (array and immediate next word)
Pop the first letter in each word. If they do not match, add the to the adjacency list (e.g. "bac" and "adc" -> Adjacency list with "b" with an dedge to "a"
if they do, move on to the next letter


Time Complexity: O(sum of the length of all the words)
Space complexity: Same as above
'''



def find_order(words):
    """
    Args:
     words(list_str)
    Returns:
     str
    """
    adjList = {}
    for w in words:
        for c in w:
            if c not in adjList.keys():
                adjList[c] = set()
    
    
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        minLen = min (len(w1), len(w2))
        q1 = deque(w1)
        q2 = deque(w2)
        for i in range(minLen):
            c1 = q1.popleft()
            c2 = q2.popleft()
            if c1 != c2:
                adjList[c1].add(c2)
                break
    
    #print(adjList)
    output = []
    #topological sort using DFS
    
    visited = {i:False for i in adjList.keys()}
    added = {i:False for i in adjList.keys()}
    
    def dfs(s):
        if visited[s] == True:
            return False    # there is a loop
        if added[s] == True:
            return True         # not an error, just don't add again
        
        visited[s] = True
        for ngb in adjList[s]:
            if dfs(ngb) == False:
                return False
        visited[s] = False
        output.append(s)
        added[s] = True
        
    for i in adjList.keys():
        if dfs(i) == False:
            return ""
            
    output.reverse()
    return(("".join(output)))
        
        
        
        
        
        
        

