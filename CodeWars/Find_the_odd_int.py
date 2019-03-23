def find_it(seq):
    dict_of_repeated_numbers = { item : seq.count(item) for item in seq }
    
    for key,value in dict_of_repeated_numbers.items():
        if value%2 != 0 :
           return key