import time

####### Recursive / Top-Down / Memoization #######
def coinChange1(coins, amount):
    dp = [0] * (amount + 1)
    coinChangeDP(coins, amount, dp)
    return dp[amount]

def coinChangeDP(coins, amount, dp):
    # When we've reached the bottom of the tree
    if amount == 0:
        return 0

    # If we've solved this subproblem already
    if dp[amount] != 0:
        return dp[amount]

    # Initialize Min to max value possible as a placeholder
    Min = amount + 1

    # Min will be set to the minimum number of coins needed for amount
    for coin in coins:
        if coin <= amount:
            result = coinChangeDP(coins, amount - coin, dp)
            if result < Min:
                Min = result + 1

    # If could not find a solution, return -1
    dp[amount] = -1 if Min == amount + 1 else Min
    return dp[amount]
    
###### Iterative / Bottom-Up / Tabulation ########
def coinChange2(coins, amount):
    # Initialize dp array to max value possible as a placeholder
    max_amount = amount + 1
    dp = [max_amount] * max_amount

    # Amount of coins needed for amount is 0
    dp[0] = 0

    # Iterates from 0 to amount and solves subproblem bottom-up
    for i in range(max_amount):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    # If could not find a soultion, return -1
    return -1 if dp[amount] == max_amount else dp[amount]

coins = [2,5,10]
amt = 18
times = []

for i in range(100):
    prev = time.time()
    coinChange1(coins,amt)
    after = time.time()
    times.append(after-prev)

avg_time = sum(times) / 100
print("Average runtime for memoization algorithm: %f" %avg_time)
times.clear()

for i in range(100):
    prev = time.time()
    coinChange2(coins,amt)
    after = time.time()
    times.append(after-prev)

avg_time = sum(times) / 100
print("Average runtime for tabulation algorithm: %f" %avg_time)