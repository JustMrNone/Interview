




def main():
    arr = [10,2,5,3]
    print(isitx(arr))




def isitx(values):
    if not values and len(values) < 1:
        return None
    n = len(values)
    for i in range(n):
        for j in range(n):
            if i != j and values[i] == 2 * values[j]:
                return True
    return False

main()