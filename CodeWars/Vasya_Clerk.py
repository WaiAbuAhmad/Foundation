def tickets(people):
    
    bills={25 : 0 , 50 : 0 , 100 : 0}

    for i in range(len(people)):
        if people[i] == 25 :
            bills[25]+=1
            
        elif people[i] == 50 :
            if bills[25] > 0:
                bills[50]+=1
                bills[25] -=1
            else:
                return "NO"
        elif people[i] == 100:
            if bills[25]>0 :
                if bills[50]>0:
                    bills[50] -=1
                    bills[25] -=1
                elif bills[25] >= 3:
                    bills[25] -=3
                else:
                    return "NO"
            else:
                return"NO"
                
        
    return "YES"