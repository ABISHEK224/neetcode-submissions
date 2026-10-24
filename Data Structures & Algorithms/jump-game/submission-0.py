class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = len(nums)-1
        goal = len(nums)-1
        while current >= 0:
            if current + nums[current] >= goal:
                goal = current
            current-=1
        return  True if goal==0 else False
        