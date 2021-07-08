def sort(arr):
    N = len(arr)
    for i in range(N): #outer loop
        for j in range(N-1, i, -1):
            if arr[j] < arr[j-1]:
            #swaps two elements
                arr[j], arr[j-1] = arr[j-1], arr[j]
        # print("1...")
        # print(arr[0:i+1]) #are in sorted order and contain smallest keys of the entire array
        # print("2...")
        # print(arr[N-i-1:N]) #are not in sorted order and does not contain largets keys of the entire array
    return arr

if __name__ == '__main__':
    arr = [4,5,3,2,4,1]
    print(sort(arr))

