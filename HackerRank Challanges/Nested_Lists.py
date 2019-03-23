student_list=[]
lowest_score=100
second_lowest_score=100
student_lowest=[]

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name,score])


for n in range(len(student_list)):
    if lowest_score >= student_list[n][1]:
        lowest_score = student_list[n][1]
      

for n in range(len(student_list)):
    if second_lowest_score >= student_list[n][1] and student_list[n][1] != lowest_score:
        second_lowest_score = student_list[n][1]
       

for n in range(len(student_list)):
    if second_lowest_score == student_list[n][1] :
        student_lowest.append(student_list[n][0])

student_lowest.sort()
for n in student_lowest:
    print (n)

                                         
       
    

