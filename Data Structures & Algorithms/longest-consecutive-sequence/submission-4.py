class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        minimum = nums[0]
        hashMap = {}
        count = 0
        for i in range(len(nums)):
            hashMap[nums[i]] = 1
        maxSeq = 0
        for i in range(len(nums)):
            count=0
            if nums[i]-1 not in hashMap:
                minimum = nums[i]
                while minimum in hashMap:
                    count+=1
                    minimum+=1
                maxSeq = max(maxSeq,count)
            else:
                minimum = nums[i]        
            
        return maxSeq
        