class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #O(NM) time
        #O(1) space
        result = 0 
        multiplicand = 1
        for i in range(len(num1)-1,-1,-1):
            remainder = 0
            stepSum = 0
            stepMultiplicand = 1
            for j in range(len(num2)-1,-1,-1):
                
                #print(stepSum, remainder, multiplicand)
                n1 = ord(num1[i]) - ord("0")
                n2 = ord(num2[j]) - ord("0")
                p = n1 * n2
                #print(p)
                stepSum += ((p%10)  + remainder) * stepMultiplicand
                stepMultiplicand *= 10
                remainder = p//10
                
            if remainder > 0:
                stepSum += (remainder * stepMultiplicand)
            result += (stepSum * multiplicand)
            multiplicand *= 10
        
        return str(result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.multiply("2","3"))
    print(sol.multiply("123","456"))
    print(sol.multiply("12","123"))
    print(sol.multiply("10","100"))
    print(sol.multiply("0","2"))