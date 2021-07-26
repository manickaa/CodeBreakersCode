class Solution:
    def isValid(self, s: str) -> bool:
        #O(N) time
        #O(N) space if all characters are expect 'c'
        if len(s) < 3:
            return False
        stack = []
        for char in s:
            if char != 'c':
                stack.append(char)
            elif char == 'c':
                if stack and stack[-1] == 'b':
                    stack.pop()
                if stack and stack[-1] == 'a':
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid("aabcbc"))
    print(sol.isValid("abcabcababcc"))
    print(sol.isValid("acabcb"))
    print(sol.isValid("abccba"))
    print(sol.isValid("a"))
