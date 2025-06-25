from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 初始化 DP 数组，dp[i] 表示凑齐金额 i 所需的最小硬币数
        # 默认值为正无穷，表示不可达
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 凑齐金额 0 需要 0 枚硬币

        # 遍历每个金额从 1 到 amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:  # 如果金额 i 足够扣除当前硬币值
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # 如果 dp[amount] 是初始值，表示无法凑齐
        return dp[amount] if dp[amount] != float('inf') else -1