def is_valid_walk(walk):
    # Check if the walk is exactly 10 minutes
    if len(walk) != 10:
        return False
    
    # Initialize counters for north-south and east-west
    ns = 0  # North-South displacement
    ew = 0  # East-West displacement

    # Calculate the net displacement
    for direction in walk:
        if direction == 'n':
            ns += 1
        elif direction == 's':
            ns -= 1
        elif direction == 'e':
            ew += 1
        elif direction == 'w':
            ew -= 1
    
    # Return True if both displacements are zero
    return ns == 0 and ew == 0