def linear_search(array, target):
    index = 0
    found = False
    
    while index < len(array) and not found:
        if target == array[index]:
            found = True
            print(array[index], 'found at position', index+1)
        else:
            index += 1

states = ['Johor', 'Selangor', 'Perak', 'Penang', 'Kedah', 'Terengganu', 'Kelantan']
state = 'Penang'
linear_search(states, state)
