class Converter:
    def __init__(self, intromans: dict):
        self.intromans = intromans

    def int_to_roman(self, number: int) -> str:
        if number > 3999 or number < 1:
            return "Invalid number"

        result = ""
        
        for value in sorted(self.intromans.keys(), reverse=True):
            while number >= value:
                result += self.intromans[value]
                number -= value
        return result

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

converter = Converter(romans)
print(converter.int_to_roman(1987))  # Example usage
