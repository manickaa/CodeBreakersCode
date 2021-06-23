#Given a string s, find the length of the longest substring 
# without repeating characters.

def lengthOfLongestSubstring(self, s: str) -> int:
    #O(N) time
    #O(K) space - k is the number of unique characters in the given string
    hashmap = {}
    start = 0
    count = 0
    for i in range(0, len(s)):
        character = s[i]
        if character in hashmap:
            start = max(start, hashmap[character]+1)
        count = max(count, i-start+1)
        hashmap[character] = i
    return count


