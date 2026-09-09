class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        freq=[[] for i in range(len(nums)+1)]
        for n in nums:
            hashMap[n] = hashMap.get(n,0)+1
        for num,count in hashMap.items():
            count = hashMap[num]
            freq[count].append(num)
        result = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        return []
        
            










        