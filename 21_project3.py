while True:
    print("\n================ MAIN MENU ================")
    print("Press 1 for Course Management")
    print("Press 2 for Batch Management")
    print("Press 3 for Subject Management")
    print("Press 4 for Teacher Management")
    print("Press 5 for Lecture Management")
    print("Press 6 for Payout Management")
    print("Press 7 for Report Management")
    print("Press 0 for Exit")


    choice = int(input("Enter your choice: "))

    if choice < 0 or choice > 7:
        print("Invalid choice! Please try again.")
    else:
        # 1. Course Management
        if choice == 1:
            while True:
                print("\n--- Course Management ---")
                print("Press 1 to Insert course")
                print("Press 2 to Update course")
                print("Press 3 to Delete course")
                print("Press 4 to Select/view courses")
                print("Press 5 to Search course")
                print("Press 0 to Exit to main menu")
                
                course_choice = int(input("Enter your choice: "))
                
                if course_choice < 0 or course_choice > 5:
                    print("Invalid choice")
                else:
                    if course_choice == 1:
                        print("Let us insert new course")
                    elif course_choice == 2:
                        print("Let us update course")
                    elif course_choice == 3:
                        print("Let us delete course (Update operation)")
                    elif course_choice == 4:
                        print("Let us select all courses")
                    elif course_choice == 5:
                        print("Let us search course")
                    else:
                        print("Exit to main menu")
                        break

        # 2. Batch Management
        elif choice == 2:
            while True:
                print("\n--- Batch Management ---")
                print("Press 1 to Insert batch")
                print("Press 2 to Update batch")
                print("Press 3 to Delete batch")
                print("Press 4 to Select/view batches")
                print("Press 5 to Search batch")
                print("Press 0 to Exit to main menu")
                
                batch_choice = int(input("Enter your choice: "))
                
                if batch_choice < 0 or batch_choice > 5:
                    print("Invalid choice")
                else:
                    if batch_choice == 1:
                        print("Let us insert new batch")
                    elif batch_choice == 2:
                        print("Let us update batch")
                    elif batch_choice == 3:
                        print("Let us delete batch (Update operation)")
                    elif batch_choice == 4:
                        print("Let us select all batches")
                    elif batch_choice == 5:
                        print("Let us search batch")
                    else:
                        print("Exit to main menu")
                        break

        # 3. Subject Management
        elif choice == 3:
            while True:
                print("\n--- Subject Management ---")
                print("Press 1 to Insert subject")
                print("Press 2 to Update subject")
                print("Press 3 to Delete subject")
                print("Press 4 to Select/view subjects")
                print("Press 5 to Search subject")
                print("Press 0 to Exit to main menu")
                
                subject_choice = int(input("Enter your choice: "))
                
                if subject_choice < 0 or subject_choice > 5:
                    print("Invalid choice")
                else:
                    if subject_choice == 1:
                        print("Let us insert new subject")
                    elif subject_choice == 2:
                        print("Let us update subject")
                    elif subject_choice == 3:
                        print("Let us delete subject (Update operation)")
                    elif subject_choice == 4:
                        print("Let us select all subjects")
                    elif subject_choice == 5:
                        print("Let us search subject")
                    else:
                        print("Exit to main menu")
                        break

        # 4. Teacher Management
        elif choice == 4:
            while True:
                print("\n--- Teacher Management ---")
                print("Press 1 to Insert teacher")
                print("Press 2 to Update teacher")
                print("Press 3 to Delete teacher")
                print("Press 4 to Select/view teachers")
                print("Press 5 to Search teacher")
                print("Press 0 to Exit to main menu")
                
                teacher_choice = int(input("Enter your choice: "))
                
                if teacher_choice < 0 or teacher_choice > 5:
                    print("Invalid choice")
                else:
                    if teacher_choice == 1:
                        print("Let us insert new teacher")
                    elif teacher_choice == 2:
                        print("Let us update teacher")
                    elif teacher_choice == 3:
                        print("Let us delete teacher (Update operation)")
                    elif teacher_choice == 4:
                        print("Let us select all teachers")
                    elif teacher_choice == 5:
                        print("Let us search teacher")
                    else:
                        print("Exit to main menu")
                        break

        # 5. Lecture Management
        elif choice == 5:
            while True:
                print("\n--- Lecture Management ---")
                print("Press 1 to Insert lecture")
                print("Press 2 to Select/view lectures")
                print("Press 0 to Exit to main menu")
                
                lecture_choice = int(input("Enter your choice: "))
                
                if lecture_choice < 0 or lecture_choice > 2:
                    print("Invalid choice")
                else:
                    if lecture_choice == 1:
                        print("Let us insert new lecture")
                    elif lecture_choice == 2:
                        print("Let us select all lectures")
                    else:
                        print("Exit to main menu")
                        break

        # 6. Payout Management
        elif choice == 6:
            while True:
                print("\n--- Payout Management ---")
                print("Press 1 to Generate payout of specific teacher between dates")
                print("Press 2 to Generate PDF file & send email to admin and teacher")
                print("Press 0 to Exit to main menu")
                
                payout_choice = int(input("Enter your choice: "))
                
                if payout_choice < 0 or payout_choice > 2:
                    print("Invalid choice")
                else:
                    if payout_choice == 1:
                        print("Let us generate specific teacher's payout between given dates")
                    elif payout_choice == 2:
                        print("Let us generate PDF and send email notification")
                    else:
                        print("Exit to main menu")
                        break

        # 7. Reports Management
        elif choice == 7:
            while True:
                print("\n--- Reports Management ---")
                print("Press 1 to Generate batch wise lecture detail between given date")
                print("Press 2 to Generate batch wise lecture detail with total amount")
                print("Press 0 to Exit to main menu")
                
                report_choice = int(input("Enter your choice: "))
                
                if report_choice < 0 or report_choice > 2:
                    print("Invalid choice")
                else:
                    if report_choice == 1:
                        print("Let us generate batch wise lecture details between dates")
                    elif report_choice == 2:
                        print("Let us generate batch wise lecture details with total amount")
                    else:
                        print("Exit to main menu")
                        break

        # 0. Exit from Program
        else:
            print("Thank you for using Lecture's Payment Management System. Exit successful!")
            break