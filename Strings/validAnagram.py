
def isValidAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    count = [0] * 26

    for c1, c2 in zip(str1, str2):
        count[ord(c1) - ord('a')] += 1
        count[ord(c2) - ord('a')] += 1
    
    for c in count:
        if (c%2) != 0:
            return False
    return True

if __name__ == '__main__':
    str1 = 'brainy'
    str2 = 'binary'
    print(isValidAnagram(str1, str2))

    str1 = 'acting'
    str2 = 'actor'
    print(isValidAnagram(str1, str2))

    str1 = 'anagram'
    str2 = 'nagarama'
    print(isValidAnagram(str1, str2))