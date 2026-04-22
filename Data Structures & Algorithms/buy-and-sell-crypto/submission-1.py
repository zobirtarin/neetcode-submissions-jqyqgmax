class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = 0
        maxProfit = 0

        for i in range(len(prices)):
            if i == 0:
                lowestPrice = prices[i]
            if prices[i] < lowestPrice:
                lowestPrice = prices[i]
            if prices[i] - lowestPrice > maxProfit:
                maxProfit = prices[i] - lowestPrice
        return maxProfit
        