def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    dp = [0] * (n+1) #at pos i it stores number of ways to make change for target amount i 
    dp[0] = 1
    for denom in denoms:
        for amount in range(1,len(dp)):
            if denom <= amount:
                dp[amount] += dp[amount-denom]
    return dp[n]
if __name__ == "__main__":
    print(numberOfWaysToMakeChange(25,[1,5,10,25]))