def maxProfit(prices):
    if not prices:
        return 0
    
    out = 0
    
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            out += prices[i] - prices[i-1]
    print(out)

stock = [1,9,8,5,5]

maxProfit(stock)