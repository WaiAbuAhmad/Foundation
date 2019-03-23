def print_formatted(number):

    # your code goes here
    lenght= len('{0:b}'.format(number))
    for x in range(number) :
        print (str((x+1)).rjust(lenght) ,str('{0:o}'.format(x+1)).rjust(lenght) ,str( format(x+1, '2X')).rjust(lenght) ,str('{0:b}'.format(x+1)).rjust(lenght) )


