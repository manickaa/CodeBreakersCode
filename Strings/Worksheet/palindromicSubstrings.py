class Solution:
    #O(N^2) time because 2N-1 centers possible and each can expand to a length of N
    #O(1) space
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)):
            count += self.expandFromCenter(s, i, i)
            count += self.expandFromCenter(s, i, i+1)
        return count
    
    def expandFromCenter(self, s, left, right):
        c = 0
        l = left
        r = right
        while(l >= 0 and r < len(s)):
            if s[l] != s[r]:
                break
            l-=1
            r+=1
            c += 1
        return c

if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubstrings("abc"))
    print(sol.countSubstrings("aaa"))
    print(sol.countSubstrings("abcbad"))