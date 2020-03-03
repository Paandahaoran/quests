def maxSubArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_ = nums[0]
        start = 0
        dp = [nums[0]]
        for i in range(1,len(nums)):
            dp.append(nums[i] + (dp[i-1] if dp[i-1] > 0 else 0))
            print(dp[i])
        max_ = max(dp)
        return max_



print(maxSubArray([2,3,4,-2,5,-1,1,6,5,42,-1,-3,9]))
