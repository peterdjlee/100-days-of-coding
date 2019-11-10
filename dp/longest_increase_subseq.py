def lis(arr):
    n = len(arr)

    # Initialize table to remember answers to subproblems.
    dp = [1] * n
    # Have to keep track of maximum answer.
    ans = 1
    # Solve subproblem of subarray starting from the back of the array.
    for i in range(n - 1, -1, -1):
        if i != n - 1: # Last subarray will always have longest subsequence of 1
            found = False
            j = i + 1
            # Loop through the rest of the array until a bigger element is found.
            # Answer to the subarray starting from that element + 1 is the new answer.
            while not found and j < n:
                if arr[j] > arr[i]:
                    dp[i] += dp[j]
                    found = True
                j += 1
            # Keep track of the maximum value so far.
            ans = max(ans, dp[i])

    return ans

arr = [3, 10, 2, 1, 20]
print(lis(arr))