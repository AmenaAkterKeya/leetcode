class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num1,num2 = sys.maxsize, sys.maxsize

        for i in nums:
            if(i>num2):
                return True
            
            if(i<=num1):
                num1=i
            elif(i<=num2):
                num2 = i
        return False
