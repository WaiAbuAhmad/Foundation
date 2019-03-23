def alphabet_position(text):
    str1=[]
    for letter in text.lower():
        if letter.isalpha():
            str1.append(str(ord(letter)-96))
    return " ".join(str1)
            