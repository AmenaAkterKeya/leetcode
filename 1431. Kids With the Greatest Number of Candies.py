class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False for _ in range(len(candies))]

        presentGreatestCandies = max(candies)

        for i,presentCandies in enumerate(candies):
            if(presentCandies+extraCandies >= presentGreatestCandies ):
                res[i] = True
        
        return res