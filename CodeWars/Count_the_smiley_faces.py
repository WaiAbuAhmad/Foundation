ef count_smileys(arr):
    count =0 
    
    for item in arr:
        if len(item) == 2 :
            if (item[0] == ":" or item[0] == ";") and (item[-1] == ")" or item[-1] =="D"):
                count +=1
        elif len(item)<4 :
            if (item[0] == ":" or item[0] == ";") and (item[-1] == ")" or item[-1] == "D") and (item[1] =="" or item[1]=="~" or item[1] =="-"):
                count +=1
            
    return count #the number of valid smiley faces in array/list