import connection as database

def Addtour():
    #create sql statement 
    sql = "insert into tour (title,detail,start_date,days,adult_rate,child_rate) values (%s,%s,%s,%s,%s,%s)"
    # %s is called placeholder 

    #accept input from user 
    title = input("Enter tour title:")
    detail = input("Enter tour detail:")
    start_date = input("Enter date(yyyy-mm-dd):")
    days = int(input('enter number of days:'))
    adult_rate = float(input('enter adult rate:'))
    child_rate = float(input('enter child rate:'))

    #create list whose size must be equal to total placeholder 
    values = [title,detail,start_date,days,adult_rate,child_rate]
    #create cursor 
    cursor = database.connect.cursor()

    #run sql statement 
    cursor.execute(sql,values)

    #save changes 
    database.connect.commit()

    print("product inserted")
def Viewtour(SQLCommand=None, title=None):
    # create cursor
    cursor = database.connect.cursor(dictionary=True)

    if SQLCommand == None:
        # create sql statement
        sql = "SELECT id, title, detail, start_date, days, adult_rate, child_rate FROM tour WHERE is_deleted=0  ORDER BY id DESC"
        cursor.execute(sql)
    else:
        sql = SQLCommand
        cursor.execute(sql, (f"%{title}%",))

    # fetch and display all rows
    table = cursor.fetchall()

    print(f"{'id':<5} {'title':35} {'detail':45} {'start_date':20} {'days':10} {'adult_rate':10} {'child_rate':10}")
    print("-"*140)

    count = 0

    for row in table:
        print(f"{row['id']:<5} {row['title']:<35} {row['detail'][:42]:<45} {str(row['start_date']):<20} {row['days']:<10} {row['adult_rate']:<10} {row['child_rate']:<10}")

        count += 1

        if count == 26:
            input("Press any key to continue")
            count = 0
def Deletetour():
    #create sql statement 
    sql = "update tour set is_deleted=1 where id=%s"

    #accept input 
    id = int(input("Enter product id: "))
    #create list 
    values = [id]

    #create cursor 
    cursor = database.connect.cursor()

    #run sql command
    cursor.execute(sql,values)

    #save changes
    database.connect.commit()
    if cursor.rowcount!=0:
        print("product deleted")
    else:
        print("product not found")

def Updatetour():
        #create sql statement 
    sql = "update tour set title=%s,detail=%s,start_date=%s,days=%s, adult_rate=%s,child_rate=%s where id=%s"

    #accept input from user 
    id = int(input("enter product id:"))
    title = input("Enter tour title:")
    detail = input("Enter tour detail:")
    start_date = input("Enter date(yyyy-mm-dd):")
    days = int(input('enter number of days:'))
    adult_rate = float(input('enter adult rate:'))
    child_rate = float(input('enter child rate:'))

    
    #create list 
    values = [title,detail,start_date,days,adult_rate,child_rate,id]

    #create cursor 
    cursor = database.connect.cursor()

    #execute sql 
    cursor.execute(sql,values)

    #save changes 
    database.connect.commit()
    if cursor.rowcount !=0:
        print("product updated")
    else:
        print("Product not found")
