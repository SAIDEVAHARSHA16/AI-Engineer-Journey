class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=prices[0]
        c=0
        for i in prices:
            if a>i:
                a=i
            if i-a >=c:
                c=i-a
        return c
