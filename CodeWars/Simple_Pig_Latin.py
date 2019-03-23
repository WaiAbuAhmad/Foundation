def pig_it(text):
    #your code here
    sentence = text.split()
    new_sentence = []
    for i in range (len(sentence)) :
        if sentence[i].isalpha() :
            new_sentence.append(sentence[i][1:] + sentence[i][0] + "ay")
        else :
            new_sentence.append(sentence[i])
    return " ".join(new_sentence)