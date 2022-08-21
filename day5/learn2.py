student_heights = input("enter a list of student heights").split()
for n in range(0 ,len(student_heights)):
#تحويل قيم اطوال الطلاب من سترينق الى انت 
    student_heights[n] = int(student_heights[n])
print(student_heights)
######
#علشان اقدر  احفظ القيم داخل متغير
total_height=0
for hegiht in student_heights:
    total_height=total_height+hegiht
print(total_height)
####
number_of_student=0
for number in student_heights:
    number_of_student=number_of_student+1
print(number_of_student)  
####
result=round(total_height/number_of_student)
print(result)

