def merge_the_tools(string, k):
    # your code goes here

    l=[]

    for i in range(0,(len(string)//k)):
        l.append(string[k*i:k*i+k])

    for item in l:
        u=""
        l_set = set(item)
        for letter in item:
            if letter in l_set:
                if letter not in u:
                    u +=letter
                
                
        print(u)

