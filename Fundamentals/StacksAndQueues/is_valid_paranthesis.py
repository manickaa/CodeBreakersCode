#Given a string containing just the characters '(',')', determine if the input is valid

#input string is valid if:
#   1. Each paranthesis is closed by a matching right parentheses
#   2. We may not have a right parenthesis without a matching left parentheses. 

# Example 1: Input: "()" Output: true

# Example 2: Input: "(())()" Output: true

# Example 3: Input: "(()" Output: false because there are more "(" than ")"

# Example 4: Input: "())(" Output: false because the second ")" does not match any "("


#function to handle string with characters '( , )' only
def isValidParanthesis(string):
    
    #O(N) time and space
    #in worst case, s = '(((((((((......', everything gets added to the stack - so O(N)

    stack = []
    
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # Check if the stack is empty. If empty, then return false since 
			# we have more ")" than "("
            if len(stack) == 0 or stack.pop() != '(':
                return False
        #Otherwise we have a non-paren character which returns False.
        else:
            return False
    
    # If the stack is not empty, then we have more "(" to match and return False
    # Otherwise it's valid!
    return True if len(stack) == 0 else False

#function to handle string with characters '( , ), [, ], {, }'
def isValidParans(string):
    
    #O(N) time and space
    
    paranthesis = ['(',')','[',']','{','}']
    stack = []
    
    for char in string:
        index = paranthesis.index(char)
        if index %2 == 0:
            stack.append(char)
        else:
            # Check if the stack is empty. If empty, then return false since 
			# we have more ")" than "("
            if len(stack) == 0 or stack.pop() != paranthesis[index-1]:
                return False

    # If the stack is not empty, then we have more "(" to match and return False
    # Otherwise it's valid!
    return True if len(stack) == 0 else False

print(isValidParanthesis("()"))
print(isValidParanthesis('(())()'))
print(isValidParanthesis('(()'))
print(isValidParanthesis('())('))
print(isValidParanthesis(""))

print(isValidParans("()"))
print(isValidParans("(){}[]"))
print(isValidParans("{{(([]"))
