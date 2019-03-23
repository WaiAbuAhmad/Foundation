def iq_test(numbers):
    position_odd = 0
    position_even = 0
    even= 0
    odd = 0
    num = numbers.split()

    for i in range(len(num)) :
        if int(num[i]) % 2 == 0:
            even += 1
            even_position = i+1
        else :
        
            odd += 1
            odd_position = i+1
    if even > odd :
        return odd_position
    else :
        return even_position