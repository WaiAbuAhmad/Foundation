def minion_game(string):
  

    
    vowels = "AEIOU"
    Stuart = 0
    Kevin = 0 




    for I in range (int(len(string))):
        if string[I] in vowels:
            Kevin += (int(len(string))-I)
        else :
            Stuart += (int(len(string))-I)


    if Kevin > Stuart :
        print("Kevin {}".format(Kevin))
    elif Kevin < Stuart:
        print("Stuart {}".format(Stuart))
    else :

        print("Draw")

