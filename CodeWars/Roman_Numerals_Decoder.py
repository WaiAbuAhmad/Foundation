def solution(roman):
    Roman_dic_value ={
    "I"       :      1,
    "IV"     :      4,
    "V"      :      5,
    "IX"      :      9,
    "X"       :     10,
    "XL"      :     40,
    "L"       :     50,
    "XC"      :     90,
    "C"      :    100,
    "CD"      :    400,
    "D"      :    500,
    "CM"      :    900, 
    "M"      :    1000 }
        
    
    
    decimal_value = 0
    i = 0
    while i < (len( roman)) :
        if roman[i:i+2] in Roman_dic_value.keys() :
            decimal_value += Roman_dic_value[roman[i:i+2]]
            i = i+2
        
        
        else :
            decimal_value +=Roman_dic_value[roman[i]]
            i += 1
    return decimal_value
    