class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(n, prefix1, prefix2):

            steps = 0

            while prefix1 <= n:

                steps += min(n + 1, prefix2) - prefix1

                prefix1 *= 10

                prefix2 *= 10

            return steps
        curr = 1
        k -= 1  # because we start at 1
        while k > 0:
            steps = count_steps(n, curr, curr + 1)
            if steps <= k:
                # skip this subtree
                curr += 1
                k -= steps
            else:
                # go deeper
                curr *= 10
                k -= 1
        return curr