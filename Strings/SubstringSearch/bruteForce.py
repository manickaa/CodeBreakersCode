
#Let string = 'codebreakers' be of length n
#Let pattern = 'break' be of length m

#we have to find the patter/target string in the given string and return the indices.

#BruteForce approach : O(N*M) runtime


def bruteForcePatternFind(string, pattern):

    #if the length of pattern is greater than string, return -1 (False)
    if len(pattern) > len(string):
        return -1

    output = []

    for i in range(0, len(string) - len(pattern)):
        if pattern == string[i:i+len(pattern)]:
            output.append(i)
    return output

if __name__ == '__main__':
    string = "CODEBREAKERS CODERS"
    pattern = "CODE"
    print(bruteForcePatternFind(string, pattern))

