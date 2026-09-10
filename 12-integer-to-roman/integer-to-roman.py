class Solution:
    def intToRoman(self, num: int) -> str:
    # Map values to their Roman numeral symbols in descending order
        value_map = [ 
            (1000, "M"), 
            (900, "CM"), 
            (500, "D"), 
            (400, "CD"),
            (100, "C"), 
            (90, "XC"), 
            (50, "L"), 
            (40, "XL"),
            (10, "X"), 
            (9, "IX"), 
            (5, "V"), 
            (4, "IV"), 
            (1, "I")
            ]
        result = []
        for value, symbol in value_map:
            # Stop early if the number becomes 0
            if num == 0:
                break
            # Determine how many times this symbol fits into the number
            count = num // value
            if count > 0:
                result.append(symbol * count)
                num %= value  # Update the remaining number
                
        return "".join(result)
