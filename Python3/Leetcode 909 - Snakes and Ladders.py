'''
Find the minimum number of moves to win a Snakes and Ladders game
BFS approach

Time Complexity - O(n+e) - where n = number of Cells and e = number of moves from each cell (potentially n*6 for a siz sided dice)
Space Complexity - O(n+e) as well since we might end up running through all solutions to get to optimal one
'''


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        numRows = len(board)            # problem statement is n x n board. Just making the code more generic
        numCols = len(board[0])
        maxCell = numRows * numCols
        
        board.reverse()
        
        def CellToCoord(cell):
            # takes a cell number and returns row, col coordinates
            r = (cell - 1) // numCols   # floor of cell numnber / number of cols
            if (r % 2) == 0:
                c = (cell -1) % numCols	# if an even row, simply do a Mod
            else:
                c = (numCols - 1 ) - ((cell -1) % numCols)  # if an even row Mod and flip
            return [r, c]
        
        
        visited = {i:0 for i in range(1, (maxCell + 1))}
        
        def bfs(cell, num_moves):
            q = deque()
            q.append([cell, num_moves])
            
            while q:
                c,m = q.popleft()
                visited[c] = 1
                for i in range(6): #roll a dice
                    newCell = c + i + 1
                    r1, c1 = CellToCoord(newCell)    # get the coordinates from our handy function
                    if not (board[r1][c1] == -1):     # snake or ladder
                        newCell = board[r1][c1]
                    if newCell == maxCell:
                        return (m+1)
                    if (visited[newCell] == 0):    # if we came here before, ignore  
                        q.append([newCell, m+1])
                    
            return -1
        
        ret = bfs(1, 0)   # start at cell 1 and no moves
        return (ret)
    