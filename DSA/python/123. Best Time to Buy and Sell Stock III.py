class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfitSoFarFromLeft = [0 for i in range(len(prices))]
        leftMin, leftMax = 0, 0
        maxProfitSoFarFromRight = [0 for i in range(len(prices))]
        rightMin, rightMax = len(prices)-1, len(prices)-1

        for i in range(1, len(prices)):
            if prices[i] >= prices[leftMin]:
                leftMax = i
                maxProfitSoFarFromLeft[i] = max(prices[leftMax] - prices[leftMin], maxProfitSoFarFromLeft[i-1])
            else:
                leftMin = i
                maxProfitSoFarFromLeft[i] = maxProfitSoFarFromLeft[i-1]
            
            if prices[n-1-i] <= prices[rightMax]:
                rightMin = n-1-i
                maxProfitSoFarFromRight[n-1-i] = max(prices[rightMax] - prices[rightMin], maxProfitSoFarFromRight[n-i])
            else:
                rightMax = n-1-i
                maxProfitSoFarFromRight[n-1-i] = maxProfitSoFarFromRight[n-i]

        
        maxProfit = 0
        for i in range(len(prices)-1):
            maxProfit = max(maxProfit, maxProfitSoFarFromLeft[i] + maxProfitSoFarFromRight[i])
        print(maxProfitSoFarFromLeft, maxProfitSoFarFromRight)
        return maxProfit


            

