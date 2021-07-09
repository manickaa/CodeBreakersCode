def stringSort(string):
    #O(A*N) time => O(N) time
    #space => O(N) for result. Constant extra space
    alphabets = 26
    counts = [0] * alphabets

    for char in string.replace(" ", ""): #runs N times
        counts[ord(char) - ord('a')] += 1

    sorted_string = ""
    for i, count in enumerate(counts): #runs A times in worst case
        sorted_string += chr(ord('a') + i) * count
    
    return sorted_string

if __name__ == '__main__':
    string = 'hotdog'
    print(stringSort(string))
    string = 'i am a software developer'
    print(stringSort(string))