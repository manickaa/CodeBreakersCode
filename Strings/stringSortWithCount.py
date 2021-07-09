def stringSort(string):
    alphabets = 26
    counts = [0] * alphabets

    for char in string:
        counts[ord(char) - ord('a')] += 1

    sorted_string = ""
    for i, count in enumerate(counts):
        sorted_string += chr(ord('a') + i) * count
    
    return sorted_string

if __name__ == '__main__':
    string = 'hotdog'
    print(stringSort(string))