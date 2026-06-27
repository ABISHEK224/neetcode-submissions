class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not nums:
            return []
        nums.sort()
        for i in range(len(nums)):
            firstElement = nums[i]
            if(firstElement > 0):
                continue
            if i>0 and nums[i] == nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                sum = firstElement + nums[j] + nums[k]
                if sum < 0:
                    j+=1
                elif sum > 0:
                    k-=1
                else:
                    result.append([firstElement, nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
        return result