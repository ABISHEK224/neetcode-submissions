class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0 , len(nums)-1
        mid = (left+right)//2
        res=nums[0]
        while left<=right:
            
            if(nums[left] < nums[right]):
                res = min(res,nums[left])
                break
            res = min(res,nums[mid])
            if nums[left] <= nums[mid]:
                left = mid+1
            if nums[right] > nums[mid]:
                right = mid-1
            mid = (left+right)//2
            
        return res
            
                
            


        