# Enter your code here. Read input from STDIN. Print output to STDOUT


N=(input()).split()

shape1 = ".|."
shape2 = "-"
shape3 = "WELCOME"

for  n in range((int(N[0])//2)) :
    multi=int((int(N[1])-(3*(2*int(n)+1)))/2)
    print (multi*shape2 + shape1*((2*n)+1) + multi*shape2   )

print (  int((int(N[1])-len(shape3))/2)*shape2 +shape3+ int((int(N[1])-len(shape3))/2)*shape2 )

for  n in range((int(N[0])//2)-1,-1,-1) :
    multi=int((int(N[1])-(3*(2*int(n)+1)))/2)
    print (multi*shape2 + shape1*((2*n)+1) + multi*shape2   )
