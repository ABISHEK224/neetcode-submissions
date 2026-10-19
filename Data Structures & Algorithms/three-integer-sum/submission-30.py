class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print("sorted",nums)
        n = len(nums)
        result = []
        for i in range(len(nums)):
            current = nums[i]
            if i>0 and nums[i-1] == current:
                continue
            left = i+1
            right = len(nums)-1
            # print("before while",current,left,right)
            while left <right:
                value = current +nums[left] +nums[right]
                if value == 0:
                    # print("inside",current,nums[left],nums[right])
                    result.append([current,nums[left],nums[right]])
                    prevLeft = nums[left]
                    while left+1< n and nums[left]!=prevLeft:
                        left+=1
                    prevRight = nums[right]
                    while right-1>0 and prevRight==nums[right]:
                        right-=1
                elif value > 0:
                    right-=1
                else:
                    left+=1
                


        return result



        