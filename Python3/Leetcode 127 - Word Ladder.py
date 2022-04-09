'''
Time Complexity: 
	O(number of words * length of words) for creating the Adjacency List
	O(number or words - SQUARED * length of words) for BFS - simply because we may need to visit each word AFTER scanning the length of words

Space complexity: 
	O(number of words * length of words) to store the Adjacency List
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not (endWord in wordList):
            return 0
        
        if not (beginWord in wordList):
            wordList.append(beginWord)
        
        adjList = defaultdict(list)	#Note: Allows you to create a docitionary of lists
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + '*' + w[j+1:]
                adjList[pattern].append(w)
        
        #BFS
        q = deque()		# Note: allows double ended queue
        q.append((beginWord,1))
        
        visited = set()
        while q:
            curr, steps = q.popleft()
            visited.add(curr)
            #steps += 1
            if curr == endWord:
                return steps
            for j in range(len(curr)):
                pattern = curr[:j] + '*' + curr[j+1:]
                if pattern in adjList.keys():
                    for ngb in adjList[pattern]:
                        if ngb not in visited:	#IMPORTANT!
                            q.append((ngb, steps + 1))
                        
                            
        
        return 0