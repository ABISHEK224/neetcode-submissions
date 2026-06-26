class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashMap = {}
        maxcount=0
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            
        for i in range(len(nums)):
            if nums[i]-1 not in hashMap:
                count=0
                while nums[i]+count in hashMap:
                    count+=1
                    continue
                maxcount = max(count,maxcount)
        return maxcount
        