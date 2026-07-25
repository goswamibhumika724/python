import connection as database

def Addbatch():
    # SQL query with placeholders matching database schema
    sql = "INSERT INTO batch (courseid, startdate, enddate, classtime, is_deleted) VALUES (%s, %s, %s, %s, %s)"
    
    # Accept inputs from user
    courseid = int(input("Enter course ID: "))
    startdate = input("Enter start date (YYYY-MM-DD): ")
    enddate = input("Enter end date (YYYY-MM-DD): ")
    classtime = input("Enter class time (e.g., 09:00:00): ")
    
    values = [courseid, startdate, enddate, classtime, 0]
    
    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()
    
    print("\nBatch inserted successfully!")
    input("Press any key to continue...")

def Selectbatch(SQLCommand=None, courseid=None):
    cursor = database.connect.cursor(dictionary=True)
    
    if SQLCommand is None:
        sql = "SELECT id, courseid, startdate, enddate, classtime FROM batch WHERE is_deleted = 0 ORDER BY id DESC"
        cursor.execute(sql)
    else:
        sql = SQLCommand
        cursor.execute(sql, (courseid,))
        
    table = cursor.fetchall()
    
    print("\n" + "_"*100)
    print(f"{'id':<8} {'courseid':<12} {'startdate':<15} {'enddate':<15} {'classtime':<20}")
    print("-"*100)
    
    count = 0
    for row in table:
        print(f"{row['id']:<8} {row['courseid']:<12} {str(row['startdate']):<15} {str(row['enddate']):<15} {str(row['classtime']):<20}")
        count += 1
        
        if count == 25:
            input("\nPress any key to see more records...")
            count = 0
            
    print("_"*100)
    input("\nPress any key to continue...")

def Updatebatch():
    sql = "UPDATE batch SET courseid=%s, startdate=%s, enddate=%s, classtime=%s WHERE id=%s AND is_deleted=0"
    
    id = int(input("Enter batch id to update: "))
    courseid = int(input("Enter new course ID: "))
    startdate = input("Enter new start date (YYYY-MM-DD): ")
    enddate = input("Enter new end date (YYYY-MM-DD): ")
    classtime = input("Enter new class time (e.g., 09:00:00): ")
    
    values = [courseid, startdate, enddate, classtime, id]
    
    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()
    
    if cursor.rowcount != 0:
        print("\nBatch updated successfully!")
    else:
        print("\nBatch not found or no changes made.")
    input("Press any key to continue...")

def Deletebatch():
    sql = "UPDATE batch SET is_deleted = 1 WHERE courseid = %s"

    courseid = int(input("Enter Course ID to delete: "))

    cursor = database.connect.cursor()
    cursor.execute(sql, (courseid,))
    database.connect.commit()

    if cursor.rowcount != 0:
        print("\nbatch deleted successfully (Soft Delete)!")
    else:
        print("\ncourseid not found in batch table.")

    input("Press any key to continue...")
def Searchbatch():
    courseid = int(input("Enter course ID to search batches: "))
    
    sql = """
        SELECT id, courseid, startdate, enddate, classtime 
        FROM batch 
        WHERE courseid = %s AND is_deleted = 0 
        ORDER BY id DESC
    """
    
    # Redirecting to Selectbatch with custom query
    Selectbatch(SQLCommand=sql, courseid=courseid)