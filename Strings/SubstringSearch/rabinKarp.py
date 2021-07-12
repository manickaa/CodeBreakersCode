
prime = 101

def rabinKarp(text, pattern):
    n = len(text)
    m = len(pattern)
    
    patternHash = regularHash(pattern, m-1)
    print(patternHash)
    textHash = regularHash(text, m-1)
    
    for i in range(1, n-m+2):
        if(patternHash == textHash):
            if checkEqual(text[i-1:i+m-1], pattern[0:]):
                return i-1
        if i < n-m+1:
            textHash = recalculateHash(text, i-1, i+m-1, textHash, m)
    return -1 #pattern match not found

def checkEqual(str1, str2):
    if len(str1) != len(str2):
        return False
    i = 0
    j = 0
    for i, j in zip(str1, str2):
        if i != j:
            return False
    return True


def regularHash(pattern, end):
    hash = 0
    for i in range(0, end+1):
        hash += ord(pattern[i]) * pow(prime, i)
    return hash

def recalculateHash(text, oldIndex, newIndex, oldHash, patternLen):
    newHash = oldHash - ord(text[oldIndex])
    newHash = newHash/prime
    newHash += ord(text[newIndex]) * pow(prime, patternLen-1)
    return newHash

if __name__ == '__main__':
    text = "abdcsabc"
    pattern = "abc"
    print(rabinKarp(text, pattern))
