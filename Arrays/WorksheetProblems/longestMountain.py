# Given an integer array arr, return the length of the longest subarray, 
# which is a mountain. Return 0 if there is no mountain subarray.

def longestMountain(self, arr) -> int:
    #O(N) runtime
    #O(1) space
    length = 0
    base = 0
    N = len(arr)
    
    while(base < N):
        end = base
        #if the end is a left side valley
        if(end+1 < N and arr[end] < arr[end+1]):
            #find peak by going uphill
            while end+1 < N and arr[end] < arr[end+1]:
                end += 1
            
            #if peak
            if end+1 < N and arr[end] > arr[end+1]:
                #downhill to find right side valley
                while end+1 < N and arr[end] > arr[end+1]:
                    end += 1
                length = max(length, end-base+1)
        
        base = max(end, base + 1)
    
    return length