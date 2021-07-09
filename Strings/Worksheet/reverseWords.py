from collections import deque
def reverseWords(s: str) -> str:
    #O(N) time
    #O(N) space - for deque
    queue = deque()
    left = 0
    right = len(s) -1
    
    while left <= right and s[left] == ' ':
        left += 1
    while left <= right and s[right] == ' ':
        right -= 1
    word = []
    
    while left <= right:
        if s[left] == ' ' and word:
            queue.appendleft(''.join(word))
            word = []
        elif s[left] != ' ':
            word.append(s[left])
        left += 1
    queue.appendleft(''.join(word))
    return ' '.join(queue)

if __name__ == '__main__':
    s = '   the sky is   blue!    '
    print(reverseWords(s))
