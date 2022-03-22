'''
LeetCode 47:
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Time Complexity of Solution: O(n*n!)
Number fo Nodes is NOT the size of the array. You would need to go through each permutation at least once so n! nodes
Internal nodes: O[n!] to search through each node + O[1] to append item to array
Leaf nodes: O[n] to copy the array to result* (n!+1)/2 leaf nodes

Space Complexity: O(n)-AUX, O(n*n!)-OUTPUT
Aux Space: O(n) to hold the counter (worst case) + O(n) to hold the currOutput (we just and and pop these)
Output Space: we will have n! output arrays of size n each
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 0:  #Edge case
            return []
    
        counter = {} # holds a dictionary with each item and count of each item
    
        for item in nums:
            if item in counter:
                counter[item] += 1
            else:
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
        