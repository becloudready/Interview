def select_max(array):
    # write your function here
    # do NOT use the built-in max() function
    max_value = array[0]
    
    for i in array:
        if i>max_value:
            max_value = i
    return max_value


if __name__ == "__main__":
    # write your debug code here
    pass
