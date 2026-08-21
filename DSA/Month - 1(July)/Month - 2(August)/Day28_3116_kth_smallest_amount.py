class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        left = min(coins)
        right = min(coins)*k
        def count(x):
            total = 0

            for mask in range(1, 2 ** len(coins)):
                lcm = 1
                bits = 0

                for i in range(len(coins)):
                    if mask & (1 << i):
                        lcm = math.lcm(lcm, coins[i])
                        bits += 1

                if bits % 2 == 1:
                    total += x // lcm
                else:
                    total -= x // lcm

            return total

        while left<right:
            mid = (left + right)//2
            if count(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

        