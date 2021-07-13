def caesarCipher(s, k):
    # Write your code here
    result = ""
    for char in s:
        if char.isalpha():
            currentVal = ord(char.lower()) - ord('a')
            newVal = (currentVal + k)%26
            newChar = chr(ord('a') + newVal)
            if char.isupper():
                result += newChar.upper()
            else:
                result += newChar
        else:
            result += char
    
    return result


if __name__ == '__main__':
    s = "Aishwarya-Ravichandran"
    k = 2
    result = caesarCipher(s, k)
    print(result)
    print(caesarCipher('wxyz',3))
    