def narcissistic( value ):
    # Code away
    value_str = str(value)
    narcissitic_sum = 0
    for i in range (len(value_str)):
        narcissitic_sum += int(value_str[i])**int(len(value_str))
    if narcissitic_sum == value :
        return True
    else :
        return False
        