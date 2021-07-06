#merge sort
#O(N log N) time
#O(N) space

def sortArray(nums):
    
    return divide(nums)
    

def divide(nums):
    if len(nums) > 1:
        mid = len(nums) // 2

        left = divide(nums[:mid])
        right = divide(nums[mid:])

        return merge(nums, left, right)
    return nums
    

def merge(nums, left, right):
    if len(left) == 0 and len(right) == 0:
        return []
    if len(left) == 0 or len(right) == 0:
        return left + right
    
    temp = []
    i = j = 0
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    while( i < len(left)):
        temp.append(left[i])
        i += 1
    while( j < len(right)):
        temp.append(right[j])
        j += 1
    
    return temp

if __name__ == '__main__':
    arr = [10,9,8,7,6,5,5,4,3,2,1]
    print(sortArray(arr))
    arr = [-10,9,8,7,6,5,-5,-4,3,3,2,1]
    print(sortArray(arr))
    arr = [5,5,4,3,2,1]
    print(sortArray(arr))
    arr = [5]
    print(sortArray(arr))