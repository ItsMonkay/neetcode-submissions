class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x = prices[0]
        bestprof = 0
        for i in prices:
            if x < i: 
                if (i - x) > bestprof:
                    bestprof = i - x
            else:
                x = i
        return bestprof