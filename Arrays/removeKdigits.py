# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.


#Overall time complexity - O(N+N) => O(N)
#Space: O(N)
def removeKdigits(nums: str, k: int) -> str:
    stack = []

    #Both the loops run O(N+N) => O(2N) => O(N) times
    #Outer loop: runs N times
    for num in nums:
        #Inner loop :runs at most K times. When 0<k<=N, this loop can run at most N times.
        #Note: This is not multiplicative, since for each num, it does not run N times. It runs a maximum of N times in total
        while(stack and k and int(stack[-1]) > int(num)):   
            k -= 1
            stack.pop()
        stack.append(num)
    
    #Runs at most N times, if all the elements in nums are 0
    #So, O(N)
    #To remove leading zeros
    cur = 0
    while(cur < len(stack) and stack[cur] == '0'):
        cur += 1
    #O(N) - if cur is not 0
    stack = stack[cur:]
    
    #To remove trailing integers if k is still greater than 0
    #i.e we can still remove k more elements
    #O(N) - if -k does not represent last element (-1)
    if k:
        stack = stack[:-k]
    
    if not stack:
        return "0"
    return "".join(stack)

if __name__ == '__main__':
    nums = "12231459"
    k = 4
    print(removeKdigits(nums, k))
    nums = "0200"
    k = 0
    print(removeKdigits(nums, k))
    nums = "10200"
    k = 1
    print(removeKdigits(nums, k))
    nums = "9"
    k = 1
    print(removeKdigits(nums, k))
    nums = "123456789"
    k = 5
    print(removeKdigits(nums, k))
