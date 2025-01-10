class Roman:
    def __init__(self, strin: str):
        # Initialize with Roman numeral string
        self.strin = strin 

    def toint(self) -> int:
        # Dictionary mapping Roman numerals to integer values
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # Initialize the result variable
        ans = 0
        
        # Iterate through the string, converting and summing values
        for i in range(len(self.strin) - 1):
            # If current value is less than next value, subtract it
            if romans[self.strin[i]] < romans[self.strin[i + 1]]:
                ans -= romans[self.strin[i]]
            else:
                # Otherwise, add it
                ans += romans[self.strin[i]]
        
        # Add the last value
        ans += romans[self.strin[-1]]
        
        return ans

def main():
    # Get input and convert to uppercase
    myroman = input().upper()
    # Create Roman object
    romaninit = Roman(myroman)
    # Convert to integer
    ans = romaninit.toint()
    # Print the result
    print(ans)
    
if __name__ == "__main__":
    main()