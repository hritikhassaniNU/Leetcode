def maxProfit(prices):
    n = len(prices)
    maxProfit = 0

    for i in range(n):
        for j in range(i + 1, n):

            buyPrice = prices[i]
            sellPrice = prices[j]

            profit = sellPrice - buyPrice

            maxProfit = max(maxProfit, profit)

    return maxProfit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))