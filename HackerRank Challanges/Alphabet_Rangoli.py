def print_rangoli(size):
    
    string = "abcdefghijklmnopqrstuvwxyz"
    shape_list=[]
    # loop creates  the middle letter string and append it to a list
    string = string[:size]

    for i in range(size):
        string_shape = string[i:size]
        shape_list.append("-".join((string_shape[:0:-1]+string_shape[:])).center(4*size-3,"-"))
    #a loop that prints the shape_list starting from the last item , and then after reaching the first item , it starts again printing from the first item till the one before the last
    for i in range(2*size-1):
        if i < size:
            print(shape_list[size-i-1])
        else :
            print(shape_list[i-size+1])
            
    



