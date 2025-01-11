def expanded_form(num):
    numbs = [i for i in str(num)]
    expanded = []
    for i in range(len(numbs)):

        expanded_part = numbs[i] + '0' * ((len(numbs) - 1) - i)
        if expanded_part != '0' * len(expanded_part):
            expanded.append(expanded_part)
    
    return ' + '.join(expanded)

number = 210
print(expanded_form(number))  