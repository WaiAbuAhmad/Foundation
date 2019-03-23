def count_substring(string, sub_string):
    counter=0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string[i:i+(len(sub_string))] ==sub_string:
                counter+=1
    return counter
