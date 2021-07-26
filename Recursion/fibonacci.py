def fibonacciMemo(n, fib_dict):
    if n in fib_dict:
        return fib_dict[n]
    else:
        result = fibonacciMemo(n-1, fib_dict) + fibonacciMemo(n-2, fib_dict)
        fib_dict[n] = result
        return result

def fibonacciBottomUp(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]   #nth index

if __name__ == '__main__':
    fib_dict = {0:1,1:1}
    for i in range(2,12):
        print(fibonacciMemo(i, fib_dict))
        print(fibonacciBottomUp(i))