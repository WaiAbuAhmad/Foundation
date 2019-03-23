def swap_case(s):
    s1=""
    for letter in s:
            if letter.isupper():
                s1 +=letter.lower()
            else:
                s1 += letter.upper()

    return s1
