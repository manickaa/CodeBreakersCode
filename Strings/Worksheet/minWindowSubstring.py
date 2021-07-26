from collections import Counter
# S = "ADOBECODEBANC", T = "ABC"
# S = "AONEUABCIYERBC", T = "ABC"
# S = "ABCDAB" T="ABC"
# S = "ABBBBBAAAAAA" T="A"
# S = "A" T="ABC"
# S = "A" T="AA"

class Solution:
    def minWindowSubstring(self, s, t):
        #O(S+T) time and space
        if not s or not t:
            return ""
        t_dict = Counter(t)
        ans = (float('inf'), None, None)
        l=r=0
        window_dict = {}
        formed = 0
        while r < len(s):
            char = s[r]
            if char in window_dict:
                window_dict[char] += 1
            else:
                window_dict[char] = 1
            if char in t_dict and window_dict[char] == t_dict[char]:
                formed += 1
            while l<=r and formed == len(t_dict):
                ch = s[l]
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)
                window_dict[ch] -= 1
                if ch in t_dict and window_dict[ch] < t_dict[ch]:
                    formed -= 1
                l+=1
            r+=1
        
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
if __name__ == "__main__":
    soln = Solution()
    print(soln.minWindowSubstring("ADOBECODEBANC", "ABC"))
    print(soln.minWindowSubstring("AONEUABCIYERBC", "ABC"))
    print(soln.minWindowSubstring("ABCDAB", "ABC"))
    print(soln.minWindowSubstring("ABBBBBAAAAAAAA", "A"))
    print(soln.minWindowSubstring("A", "ABC"))
    print(soln.minWindowSubstring("A", "AAA"))