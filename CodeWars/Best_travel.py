from itertools import combinations

def choose_best_sum(t, k, ls):
    sum_list=[]
    sutable_list=[]
    ls2=list(combinations(ls,k))
    for item in ls2:
        sum_list.append(sum(item))
    for item in sum_list:
        if item <= t :
            sutable_list.append(item)

    if sutable_list == []:
        return None
        
    else : 
        return max(sutable_list)