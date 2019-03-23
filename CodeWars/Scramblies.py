def scramble(s1,s2):
    for letter in set(s2): # after we convert the s2 to a set() , we limit the loop for max 26 letters instead of going through and each letter in a time!
        if s1.count(letter) < s2.count(letter):
            return False
    return True