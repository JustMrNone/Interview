def spin_words(sentence):
    # Your code goes here
    individual = sentence.split()
    for i in range(len(individual)):
        if len(individual[i]) > 5:
            individual[i] = individual[i][::-1]
    
    x = str(" ".join(individual))
    print(x)
    


s = "Hey fellow warriors"

spin_words(s)