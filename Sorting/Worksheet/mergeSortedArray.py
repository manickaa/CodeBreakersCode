
def mergeSortedArray(nums1, nums2, m, n):
    i = m-1
    j = n-1
    p = m+n-1

    while(i>=0 and j>=0):
        if nums1[i] > nums2[j]:
            nums1[p] = nums1[i]
            i -= 1
            p -= 1
        else:
            nums1[p] = nums2[j]
            j -= 1
            p -= 1
    nums1[:j+1] = nums2[:j+1]
    return

if __name__ == '__main__':
    nums1 = [1,3,5,0,0,0]
    nums2 = [2,4,6]
    mergeSortedArray(nums1, nums2, 3,3)
    print(nums1)