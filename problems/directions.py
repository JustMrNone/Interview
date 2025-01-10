def dirReduc(directions):
    opposite = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    stack = []
    
    for direction in directions:
        if stack and stack[-1] == opposite[direction]:
            stack.pop()  # Remove the last direction as it cancels with the current one
        else:
            stack.append(direction)
    
    return stack