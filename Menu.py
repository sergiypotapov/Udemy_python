import functions
import login



def Menu():

    print("""
    Hey Buddy. You have couple options:
[1] - Enter grades for existing name
[2] - Remove Student
[3] - Add Student
[4] - Calculate average grade for every student
[0] - Close the program

    """)
    users_choice = input("\n")
    print("choice", users_choice)

    if users_choice == '1':
        print("Choice is ", users_choice)
        functions.enter_grade()

    elif users_choice == '2':
        functions.remove_student()

    elif users_choice == '3':
        functions.add_student()
    elif users_choice == '4':
        functions.calculate_average()
    elif users_choice == '0':
        print("Thank you buddy, have a good day!")
        login.Exit()
