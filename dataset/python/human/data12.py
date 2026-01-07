#Grades
#jacob cook
#10/7/2019
print("whats your grade")

myGrade = int(input())
myLetterGrade = "Not Assigned"
if myGrade >= 90: 
     myLetterGrade = "A"
elif myGrade <= 89 or myGrade >= 80:
     myLetterGrade = "B"
elif myGrade <= 79 or myGrade >= 70:
     myLetterGrade = "c"
elif myGrade <= 69 or myGrade >= 60:
     myLetterGrade = "D"
elif myGrade <= 59 or myGrade >= 50:
     myLetterGrade = "F"

print("My grade is:", myLetterGrade)