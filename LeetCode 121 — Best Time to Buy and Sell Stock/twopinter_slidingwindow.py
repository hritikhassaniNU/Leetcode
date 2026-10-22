def maxProfit(prices):
    left = 0
    right = 1

    maxProfit = 0

    while right < len(prices):

        buyPrice = prices[left]
        sellPrice = prices[right]

        profit = sellPrice - buyPrice

        if profit > 0:
            maxProfit = max(maxProfit, profit)

        else:
            left = right

        right += 1

    return maxProfit