def factorial(n):
    if n==0 or n==1:
        return 1
    return factorial(n-1) * n


if __name__ == '__main__':
    print(factorial(100))
    print(factorial(3))
    print(factorial(0))