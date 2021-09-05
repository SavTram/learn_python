class Solution(object):
    def numIdenticalPairs(self,nums):  
        di = {}
        count =0
        for i in nums:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1
        list = []
        for i in di:
            x= di[i]
            value = x * (x-1) // 2
            list.append(value)
        return sum(list)
