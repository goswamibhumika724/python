import tour as t
import transaction as tr

while True:
    print("\nPress 1 for tour management")
    print("Press 2 for tansaction management")
    print("Press 3 for Report management")
    print("Press 0 for Exit")

    choice = int(input("enter your choice: "))

    if choice < 0 or choice > 3:
        print("invalid choice")
    else:
        if choice == 1:
            while True:
                # insert, update, Delete(update operation), View tours
                print("\nPress 1 to insert new tour")
                print("Press 2 to update tour")
                print("Press 3 to delete tour")
                print("Press 4 to view tour")
                print("Press 0 to exit to main menu")
                
                tour = int(input("enter your choice: "))
                
                if tour < 0 or tour > 4:
                    print("invalid choice")
                else:
                    if tour == 1:
                        t.Addtour()
                    elif tour == 2:
                        t.Viewtour()
                        t.Updatetour()
                    elif tour == 3:
                        t.Viewtour()
                        t.Deletetour()
                    elif tour == 4:
                        t.Viewtour()
                    else:
                        print("exit to main menu")
                        break  # break inner loop

        elif choice == 2:
            while True:
                # insert transaction,view transaction,delete(update operation),search transaction
                print("\nPress 1 to insert tour_name to transaction")
                print("Press 2 to view all transaction")
                print("Press 3 to delete tour_name from transaction")
                print("Press 4 to search tour_name in transaction")
                print("Press 0 to exit to main menu")
                
                transaction = int(input("enter your choice: "))
                
                if transaction < 0 or transaction > 4:
                    print("invalid choice")
                else:
                    if transaction == 1:
                        tr.Addtransaction()
                    elif transaction == 2:
                        tr.Displaytransaction()
                    elif transaction == 3:
                        tr.Deletetransaction()
                    elif transaction == 4:
                        tr.Searchtransaction()
                    else:
                        print("exit to main menu")
                        break  # break inner loop

        elif choice == 3:
            while True:
                # monthly report,quarter report,year report,tour wise income expense report (tour id will be given by user),tour wise income expense report(all tour)
                print("\nPress 1 to generate monthly report")
                print("Press 2 to generate quarter report")
                print("Press 3 to generate year report")
                print("Press 4 to generate specific tour report(tour id will be given by user)")
                print("Press 5 to generate all tours report")
                print("Press 0 to exit to main menu")
                
                report = int(input("enter your choice: "))
                
                if report < 0 or report > 5:
                    print("invalid choice")
                else:
                    if report == 1:
                        print("let us generate monthly report")
                    elif report == 2:
                        print("let us generate quarter report")
                    elif report == 3:
                        print("let us generate year report")
                    elif report == 4:
                        print("let us generate specific tour  report")
                    elif report == 5:
                        print("let us generate all tours report")
                    else:
                        print("exit to main menu")
                        break  # break inner loop

        else:
            print("exit from program")
            break

        


    