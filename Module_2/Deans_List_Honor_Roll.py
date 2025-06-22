#Deans_List_Honor_Roll.py
#Created by: Johnathan Dostal
#This is a program that capture input to create a new record for each student that contains the first name, last name and GPA. It will also check if the GPA is above 3.25 and print a message stating the student is on the Honor Roll. It will also check if the GPA is above 3.5 and print a message stating the student is on the Dean's List.
#Variables used include a list to store the records, a control variable to keep the loop running, a string variable to concatenate the input for storage in the list, strings for the student's first and last name, and a float for the student's gpa.


student_list = []
student_record = ""
student_gpa = 0.0
student_first_name = ""
student_last_name = ""
keep_looping = True

while keep_looping == True:
    student_last_name = input("Please enter the student's last name. \nTo exit the program, enter \"ZZZ\". \nTo list previously entered students, enter \"zzz\". ")

    if student_last_name == "ZZZ":
        keep_looping = False
        print("Thank you for using the program. Goodbye!\n")

    elif student_last_name == "zzz":
        print(student_list)
        print("\n")

    else:
        student_first_name = input("Please enter the student's first name: ")
        student_gpa = float(input("Please enter the student's GPA as a decimal value: "))

        student_record = student_last_name + "," + student_first_name + ":"+ str(student_gpa)
        student_list.append(student_record)

        if student_gpa >= 3.5:
            print("Congratulations! This student has made the Dean's List!\n")
        elif student_gpa >= 3.25:
            print("Congratulations! This student has made the Honor Roll!\n")
        else:
            print("Student information entered successfully!\n")
    
