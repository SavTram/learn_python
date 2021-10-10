class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li = []
        di = [[]]*len(strs)
        index =0
        for i in strs:
            for j in range(len(i)):
                li.append(i[j])
            di[index] = li
            index +=1
            li = []
        for i in range(len(di)):
            di[i].sort()
        result = []
        t = []
        mid = []
        i=0
        while i in range(len(di)):
            if di[i] not in t:
                t.append(di[i])
                mid.append(strs[i])
                result.append(mid)
                mid=[]
            else:
                for j in range(len(t)):
                    if di[i] == t[j]:
                        result[j].append(strs[i])
            i +=1
        return result
