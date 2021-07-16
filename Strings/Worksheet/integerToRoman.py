class Solution:
    def intToRoman(self, num: int) -> str:
        possibleRomanNumerals = [("M",1000),("CM",900),("D",500),("CD",400),("C",100),("XC",90),("L",50),("XL",40),("X",10),("IX",9),("V",5),("IV",4),("I",1)]

        result = []

        for numeral, value in possibleRomanNumerals:

	        if num == 0:

		        break

	        count = num//value

	        num = num % value

	        result.append(numeral * count)

        return "".join(result)
    

if __name__ == "__main__":
    soln = Solution()
    print(soln.intToRoman(1))
    print(soln.intToRoman(4))
    print(soln.intToRoman(9))
    print(soln.intToRoman(3999))
    print(soln.intToRoman(58))
    print(soln.intToRoman(1994))