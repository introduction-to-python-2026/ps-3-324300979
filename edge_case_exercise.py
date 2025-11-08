def move(my_list, direction=None):
    # Finds the index of the one in the list
    index_of_one = my_list.index(1)

    # Move the one to the left or to the right
    if direction == 'right' and len(my_list)-1 != index_of_one: 
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1
    elif direction == 'left' and index_of_one != 0:
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

    return my_list
