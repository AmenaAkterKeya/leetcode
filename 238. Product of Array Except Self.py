class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [None for _ in range(len(nums))]

        leftP= 1
        for i in range(len(nums)):
            res[i] = leftP
            leftP *= nums[i]

        rightP =1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= rightP
            rightP *= nums[i]
        return res
        