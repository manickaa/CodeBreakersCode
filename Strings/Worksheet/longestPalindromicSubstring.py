def longestPalindrome(s: str) -> str:
        if len(s) <= 1:
            return s
        maxLen = 0
        start = end = 0
        for i in range(0, len(s)):
            len1 = expand(s, i, i) #single middle element i
            len2 = expand(s, i, i+1)  #double middle element i, i+1 For eg: "abba" has two middle element b,b
            maxLen = max(len1, len2)
            if maxLen > (end-start):
                start = i - (maxLen-1) // 2
                end = i + (maxLen) // 2
        
        return s[start:end+1]
    
def expand(string, left, right):
    l = left
    r = right
    while(l >= 0 and r < len(string) and string[l] == string[r]):
        l -= 1
        r += 1
    
    return r-l-1


if __name__ == '__main__':
    print(longestPalindrome(""))
    print(longestPalindrome("a"))
    print(longestPalindrome("ac"))
    print(longestPalindrome("ababd"))
    print(longestPalindrome("bbccbbdd"))
    print(longestPalindrome("cbbd"))
