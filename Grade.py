grade = float(input("Grade :"))
if(grade>=90 and grade<=100):
    print("A class")
elif(grade>=80 and grade<90):
    print("B class")
elif(grade>=70 and grade<80):
    print("C class")
elif(grade<70):
    print("D class")
else:
    print("You entered wrong marks.")