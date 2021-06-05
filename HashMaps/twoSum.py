
#Given a list of integers, return the indexes of two numbers in the list, if they sum to a given target
def twoSum(nums, target):

    #O(N) runtime - since it goes through all the numbers in the given list.
    #O(N) space, in case no two numbers sum up to a given target

    #create a hashmap
    map = {}
    for i, value in enumerate(nums):
        remainder = target - value
        #check if the remainder exists in the hashmap. If it exists, get its index(ie value) from the hashmap 
        # and return with the current value's index (i)
        if remainder in map:
            return map[remainder], i
        # else add the value and the index in the hashmap as key-val pair
        else:
            map[value] = i
    return None, None

if __name__ == '__main__':
    nums = [2,5,8,12]
    target = 13
    result = twoSum(nums, target)
    print(result) #(1,2)


