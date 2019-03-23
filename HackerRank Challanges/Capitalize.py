
def solve(s):
    s=s.split(" ")
    l=[]
    for word in s:
        l.append(word.capitalize())
    return " ".join(l)  