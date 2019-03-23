def solution(args):
    i = 0 
    final_str=""
    range_list =[]
    copied_args=[]
    
    while i < len(args)-1:
        
        if args[i]-args[i+1] == -1:
            k=i
            while args[i]-args[i+1] == -1 :
                
                i+=1
                
                if i == len(args)-1:
                    break
            for j in range(k,i+1):
                range_list.append(args[j])
            copied_args.append(range_list)
            range_list=[]
            i+=1
            
        else:
            
            copied_args.append([args[i]])
            
            i+=1
    if i != len(args) :
        copied_args.append([str(args[i])])
    
    for x in range(len(copied_args)):
        if len(copied_args[x]) >= 3:
            final_str += str(min(copied_args[x]))+"-"+str(max(copied_args[x]))
        
        else:
            for j in range(len(copied_args[x])):
                final_str += "".join(str(copied_args[x][j]))
                if  j != len(copied_args[x])-1:
                    final_str += ","
        if  x!=len(copied_args)-1:
            final_str += ","
        
    return final_str    
                       