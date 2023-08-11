class Solution:
    memo: List[List[int]]

    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1

        self.memo = [[-1 for _ in range(amount + 1)]
                     for _ in range(len(coins))]
        coins.sort(key=lambda x: -x)
        for i in range(len(coins)):
            if amount >= coins[i]:
                return self.dfs(i, amount, coins)
        return 0

    def dfs(self, idx: int, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if self.memo[idx][amount] != -1:
            return self.memo[idx][amount]

        ret = 0
        for i in range(idx, len(coins)):
            if amount >= coins[i]:
                ret += self.dfs(i, amount - coins[i], coins)
        self.memo[idx][amount] = ret
        return ret