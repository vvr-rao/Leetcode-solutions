'''
Leetcode 46 - simpler version of Leetcode 47
using dfs and backtracking
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 0:  #Edge case
            return []
    
        counter = {}
        for item in nums:
            counter[item] = 1
    
        #print(counter)
    
        def dfs(currOutput, currCounter):
            if len(currOutput) == len(nums):  #base case
                result.append(currOutput.copy())
            for i in currCounter:
                if currCounter[i] > 0:
                    currCounter[i] -= 1
                    currOutput.append(i)
                    dfs(currOutput, currCounter)
                    currCounter[i] += 1
                    currOutput.pop()
    
        dfs([], counter)
        return(result)