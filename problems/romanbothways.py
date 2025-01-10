

class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        res = ""
        romans = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        if val > 4000 or val < 1:
            return None
        for value in sorted(romans.keys(), reverse=True):
            while val >= value:
                res += romans[value]
                val -= value 
        return res
                
    @staticmethod
    def from_roman(roman_num : str) -> int:
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        anse = 0
        for i in range(len(roman_num) - 1):
            if romans[roman_num[i]] < romans[roman_num[i + 1]]:
                anse -= romans[roman_num[i]]
            else:
                anse += romans[roman_num[i]]
        
        anse += romans[roman_num[-1]]
        return anse 