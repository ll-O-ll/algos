def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    # float("inf")
    minNumOfCoins = [float("inf")] * (n + 1) # 0 1 2 3 ...
    minNumOfCoins[0] = 0
    for denom in (denoms):
        for amount in range(len(minNumOfCoins)):
            if denom <= amount:
                minNumOfCoins[amount] = min(minNumOfCoins[amount], minNumOfCoins[amount-denom] + 1)	
    return minNumOfCoins[n] if minNumOfCoins[n] != float("inf") else -1

if __name__ == "__main__":
    print(minNumberOfCoinsForChange(9,[3,5]))