class Solution:
    def romanToInt(self, s: str) -> int:

        # Initialize the roman values
        rv = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        sum = 0
        
        for i in range(len(s)):
            if i+1 < len(s) and rv[s[i]] < rv[s[i+1]]:
                sum -= rv[s[i]]
            else:
                sum += rv[s[i]]
            
        # Return the sum
        return sum




