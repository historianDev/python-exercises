class Solution(object):
    def romanToInt(self, symbol: str):
        # dictionariy with roman number and its respective value
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

# reverse the string
        integer = 0
        last = "I"

        for i in symbol[::-1]:
            if roman_values[i] < roman_values[last]:
                integer -= roman_values[i]
            else:
                integer += roman_values[i]
            last = i

        return integer

    def print_number(self, ):
        roman = input('enter the roman number you want to translate: ')
        symbol = roman
        return symbol


my_solution = Solution()  # Create an instance of the Solution class
# Call the romanToInt method on the created instance
# Call the print_number() function
symbol = my_solution.print_number()
my_number = my_solution.romanToInt(symbol)
print(my_number)  # Print the result
