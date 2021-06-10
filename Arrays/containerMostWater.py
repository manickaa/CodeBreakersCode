#      p1              p2
# arr [1,8,6,2,5,4,8,3,7]
def containerMostWater(arr):
    if len(arr) < 2:
        return -1
    p1 = 0
    p2 = len(arr) - 1
    maxArea = float('-inf')
    while(p1 < p2):
        area = min(arr[p1], arr[p2]) * (p2 - p1)
        if area > maxArea:
            maxArea = area
        if arr[p1] > arr[p2]:
            p2 -= 1
        else:
            p1 += 1
    return maxArea


arr = [1,8,6,2,5,4,8,3,7]
print(containerMostWater(arr)) #49
