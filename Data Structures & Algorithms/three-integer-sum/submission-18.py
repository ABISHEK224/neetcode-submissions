class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result= []
        nums.sort()
        i=0
        while i<len(nums):
            if i>0 and nums[i]== nums[i-1]:
                i+=1
                continue

            current = nums[i]
            left = i+1
            right=len(nums)-1
            while left<right:
                sumvalue = current + (nums[left]+nums[right])
                if sumvalue < 0:
                    left=left+1
                elif sumvalue > 0:
                    right=right-1
                else:
                    result.append([current,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<len(nums)-1 and nums[left] ==nums[left-1]:
                        left+=1
            i=i+1
                
        return result
        