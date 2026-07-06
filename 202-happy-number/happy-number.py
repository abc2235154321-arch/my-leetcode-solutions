class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            ans = 0

            while num != 0:
                temp = num % 10
                num //= 10
                ans += temp ** 2

            return ans

        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            n = get_next(n)

        return True