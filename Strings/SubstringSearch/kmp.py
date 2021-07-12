def kmpSubstringSearch(text, pattern):
    m = len(pattern)
    n = len(text)

    #create table for length of suffix which is also a prefix of the string from index 0 to index i (inclusive)

    table = [0] * m
    computeLPSTable(table, pattern, m)
    
    #For each char in the text, check if that is the start for the matching pattern
    #If yes, increment to the next char and check if those char in the text and pattern match
    #If all chars match, return the starting index where the pattern matches in the text
    i = 0   #pointer for text
    j = 0   #pointer for pattern

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:  #if the last char of the pattern matches, then we found an entire match
            print('Found pattern at index' + str(i-j))
            return i-j
            j = table[j-1]
        
        #If there is a mismatch after j matches
        #do not start matching the 0 to j-1 chars again, since they already match
        #start from the longest suffix that is also a prefix from the table
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = table[j-1]
            else:
                 i+=1

    


def computeLPSTable(table, pattern, m):
    table[0] = 0 #first val is always zero
    i = 0
    j = 1

    while j < m:
        if pattern[i] == pattern[j]:
            table[j] = i+1
            i += 1
            j += 1
        else:
            if i != 0:
                i = table[i-1]
            else:
                table[j] = 0
                j+=1

if __name__ == "__main__":
    txt = "baaaaaacaaaa"
    pat = "aaacaaaa"
    print(kmpSubstringSearch(txt, pat))


    