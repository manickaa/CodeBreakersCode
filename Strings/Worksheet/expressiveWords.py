from collections import defaultdict
class Solution:
    #O(N*M) time
    #O(1) space
    def expressiveWords(self, s: str, words) -> int:
        
        if len(s) == 0 or len(words) == 0:
            return 0
        
        total = 0
        #N words
        for word in words:
            if len(word) > len(s):
                continue
            result = self.isStretchy(s, word)
            if result:
                total += 1
        return total
    
    def isStretchy(self, s, word):
        
        ptr_s = 0
        ptr_w = 0
        
        #Let M be the word in words or string, s with maximum characters
        while(ptr_s < len(s) and ptr_w < len(word)):
            #If the letters dont match, return False
            if s[ptr_s] != word[ptr_w]:
                return False
            
            count_s = 0
            letter = s[ptr_s]
            while(ptr_s < len(s) and s[ptr_s] == letter):
                count_s += 1
                ptr_s += 1
            
            letter = word[ptr_w]
            count_w = 0
            while(ptr_w < len(word) and word[ptr_w] == letter):
                count_w += 1
                ptr_w += 1
            
            if count_w > count_s:
                return False
            if count_s > count_w and count_s < 3:
                return False
        
        if ptr_s < len(s):
            return False
        else:
            return True


if __name__ == '__main__':
    soln = Solution()
    s = 'heeellooo'
    words = ["hello","hi","helo"]
    print(soln.expressiveWords(s, words))
