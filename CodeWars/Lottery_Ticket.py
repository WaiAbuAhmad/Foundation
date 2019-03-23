def bingo(ticket,win):
    mini_win = 0
    for i in range (len(ticket)):
        for j in range (len(ticket[i][0])):
            if ord(ticket[i][0][j]) == ticket[i][1] :
                
                
                mini_win +=1
                break
    if mini_win >= win :
        return "Winner!"
    else :
        return "Loser!"
    