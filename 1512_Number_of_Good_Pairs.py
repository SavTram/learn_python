class Solution(object):
    def numIdenticalPairs(self,nums):  
        di = {}
        count =0
        for i in nums:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        pair = 0
        for i in di:
            value = di[i] * (di[i] - 1) // 2
            pair += value
        return pair
    
