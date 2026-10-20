class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        countArr = [[] for n in range(len(nums)+1)]
        for n in nums:
            if n in hashMap:
                hashMap[n]+=1
            else:
                hashMap[n]=1

        for (key,value) in hashMap.items():
            countArr[value].append(key)

        result = []
        i=len(nums)
        while k>0 and i >0:
            if len(countArr[i]):
                for e in countArr[i]:
                    result.append(e)
                    k-=1
                if k==0:
                    break
            i-=1
        return result








        