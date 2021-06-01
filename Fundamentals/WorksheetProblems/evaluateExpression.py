def evaluateRPN(tokens):
    '''
    Thoughts:

    We can go through all the tokens in the array. If the token is an integer, we can push it to a stack
    If it is a operator, we can pop out the top two elements and perform the operation on them.
    We can push the result back to the stack and continue
    At the end, the result will be at top of the stack

    Pseudocode:

    1. Initialize a stack
    2. Go through all the tokens in the tokens array
    3.      If it is an integer, push it to stack
    4.      Else, pop out the top two elements and perform operation with the token(operator)
    5.            push the result back into the stack
    6. Result will at the top of stack. Pop and return it

    '''
    stack = []
    operators = {'*', '+', '/', '-'}
        
    for char in tokens:
        if char not in operators:
            stack.append(char)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if char == '+':
                result = a + b
            elif char == '*':
                result = a * b
            elif char == '/':
                result = int(b/a)
            else:
                result = b - a
                print(result)
            
            print(result)
            stack.append(result)
    
    return stack.pop()

#Time complexity - Go through the tokens array only once. If there are N tokens, then the time complexity is O(N)
#Space complexity - In worst case, if the numbers in the array are together, we will be pushing it all, before operating any of them
#                  Atmost half of the tokens are operands -  O(N//2) => O(N)