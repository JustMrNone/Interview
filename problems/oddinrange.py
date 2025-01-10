def countOdds(low: int, high: int) -> int:
        myrange = [i for i in range(low, high + 1)]
        count = 0
        for i in range(len(myrange)):
            if myrange[i] % 2 != 0:
                count += 1
        return count   
            

lows = -2
highs = 10
print(countOdds(lows, highs))
