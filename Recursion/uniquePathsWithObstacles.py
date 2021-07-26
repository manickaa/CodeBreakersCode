#paths m*n matrix = [[0,0,0],
#                   [0,1,0],
#                   [0,0,0]]
#startPos = (0,0)
#finishPos=(m,n)
#If obstacles, paths[i][j] == 1
#Output: 2 => 2 paths are possible to reach the finishPos 
def uniquePathsWithObstacles(paths):
    if not paths or paths[0][0] == 1:
        return 0
    memo = [[-1] * len(paths[0]) for _ in range(len(paths))]
    return _uniquePathHelper(paths, 0, 0, memo)

def _uniquePathHelper(paths, row, col, memo):
    #base case:
    #if the position is the finishPos, return 1
    if row == len(paths)-1 and col == len(paths[0])-1:
        return 1
    #check memo if the position has been computed before
    if memo[row][col] != -1:
        return memo[row][col]
    #Initialize count
    count = 0
    #For each possible direction
    direction = [(0,1),(1,0)] #right, down
    #Count the number of possibilities to reach the finishPos
    for x, y in direction:
        newRow= row+x
        newCol = col+y
        if 0 <= newRow < len(paths) and 0 <= newCol < len(paths[0]) and paths[newRow][newCol] != 1:
            count += _uniquePathHelper(paths, newRow, newCol, memo)
    memo[row][col] = count
    # print(memo)
    return count


if __name__ == '__main__':
    paths = [[0,0,0],[0,1,0],[0,0,0]]
    print(uniquePathsWithObstacles(paths))
