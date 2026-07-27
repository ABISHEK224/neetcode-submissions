class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = []
        suffixArray = []
        n = len(nums)
        result = []
        for i in range(len(nums)):
            if not len(prefixArray):
                prefixArray.append(1)
            else:
                prefixArray.append(prefixArray[-1]*nums[i-1])
        for i in range(len(nums)-1,-1,-1):
            if not len(suffixArray):
                suffixArray.append(1)
            else:
                suffixArray.append(suffixArray[-1]*nums[i+1])
        for i in range(len(nums)):
            result.append(prefixArray[i]*suffixArray[n-i-1])
        return result
        