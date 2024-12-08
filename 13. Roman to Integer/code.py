class Solution:
    def romanToInt(s: str) -> int:

        # Initialize the roman values
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # Initialize the sum
        sum = 0

        # Loop through the string
        for i in range(len(s)):
            sum += roman_values[s[i]]

            # If there is no next number, break the loop
            if i+1 == len(s):
                break

            # If the current number is I, check if the next number is V or X
            if s[i] == "I":
                if s[i+1] == "V" or s[i+1] == "X":
                    sum -= 2

            # If the current number is X, check if the next number is L or C
            if s[i] == "X":
                if s[i+1] == "L" or s[i+1] == "C":
                    sum -= 20

            # If the current number is C, check if the next number is D or M
            if s[i] == "C":
                if s[i+1] == "D" or s[i+1] == "M":
                    sum -= 200

        # Return the sum
        return sum

    
Solution.romanToInt("IVI")



