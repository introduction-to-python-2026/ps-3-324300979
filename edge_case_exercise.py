def move(my_list, direction=None):
    index_of_one = my_list.index(1)
    if direction == 'right' and len(my_list) - 1 != index_of_one: 
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1
    elif direction == 'left' and index_of_one != 0:
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1
    return my_list
