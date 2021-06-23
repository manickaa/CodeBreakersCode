#nums = [2,3,1,1,4] each element represent maximum jump length from that index
#start index = 0
#Determine whether we can reach the last index

#Output: true
#Explanation: Jump 1 position from index 0 to index 1. Then jump 3 positions from index 1 to 4
#              Last index is reached, so return true

'''
Greedy approach

Keep track of the best index that can be reached from each position. 
At that end, if that best index is exceeded by any index, return False
Else, return True

Example:
nums = [2,3,1,1,4]
#bestIndexPossible = 0  2   4
#from index 0, 0+2 = 2      2>0
#from index 1, 1+3 = 4      4>2 
#from index 2, 2+1 = 3      3<4 X
#from index 3, 3+1 = 4      4==4  X
#for index 4, 4+4 = 8       8>4 
# End of loop -> return True

'''
def canJump(nums):
    #O(1) space
    #O(N) time
    bestJumpLength = 0
    for i, num in enumerate(nums):
        if i > bestJumpLength:
            return False
        bestJumpLength = max(i+num, bestJumpLength)
    return True

nums = [2,3,1,1,4]
print(canJump(nums)) #true
nums = [3,2,1,0,4]
print(canJump(nums)) #false
nums=[0,2]
print(canJump(nums)) #false
nums=[2,0]
print(canJump(nums)) #true

