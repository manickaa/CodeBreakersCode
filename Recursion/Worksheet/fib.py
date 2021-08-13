class Solution:
    #time - O(N)
    #space - O(N)
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1}
        return self.helper(memo, n)
    
    def helper(self, memo, n):
        if n in memo:
            return memo[n]
        result = self.helper(memo, n-1) + self.helper(memo, n-2)
        memo[n] = result
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.fib(0))
    print(sol.fib(1))
    print(sol.fib(4))
    print(sol.fib(11))