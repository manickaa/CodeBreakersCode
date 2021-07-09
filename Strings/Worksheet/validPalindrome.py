def isPalindrome(s: str) -> bool:
    #O(N) time
    #O(1) space
    if len(s) <= 1:
        return True
    p1 = 0
    p2 = len(s)-1
    
    while p1 < p2:
        #remove non alpha numeric characters
        while p1 < p2 and not s[p1].isalnum():
            p1 += 1
        while p1 < p2 and not s[p2].isalnum():
            p2 -=1
        #if characters at pointers does not match
        if s[p1].lower() != s[p2].lower():
            return False
        p1 += 1
        p2 -= 1
    
    return True

if __name__ == '__main__':
    s = '; ;.;,,,,      ;'
    print(isPalindrome(s))  #True
    s = 'a man a plan, a canal: panama'
    print(isPalindrome(s))  #True
    s = 'race a car'
    print(isPalindrome(s))  #False
    s = 'abcccba'
    print(isPalindrome(s))  #True
    s = 'AbCcBa'
    print(isPalindrome(s))  #True
    s = '1AbcBa1'
    print(isPalindrome(s))  #True
    s = ''
    print(isPalindrome(s))  #True
