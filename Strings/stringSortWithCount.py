def stringSort(string):
    alphabets = 26
    counts = [0] * alphabets

    for char in string.replace(" ", ""):
        counts[ord(char) - ord('a')] += 1

    sorted_string = ""
    for i, count in enumerate(counts):
        sorted_string += chr(ord('a') + i) * count
    
    return sorted_string

if __name__ == '__main__':
    string = 'hotdog'
    print(stringSort(string))
    string = 'i am a software developer'
    print(stringSort(string))