from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list)
        for word in strs:
            count = [0]*26
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1
            hashmap[tuple(count)].append(word)
        
        return hashmap.values()


if __name__ == '__main__':
    soln = Solution()
    print(soln.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print(soln.groupAnagrams([""]))
    print(soln.groupAnagrams(["a"]))
    print(soln.groupAnagrams(["x","b","xe","ex"]))
    print(soln.groupAnagrams(["ear","tea","ban","can","tan","hea","its"]))