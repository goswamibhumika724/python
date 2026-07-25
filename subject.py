import connection as database

def Addsubject():
    # SQL query to insert new subject matching exact table structure
    sql = "INSERT INTO subject (courseid, title, per_hour_rate, is_deleted) VALUES (%s, %s, %s, %s)"
    
    # Inputs from user
    courseid = int(input("Enter course ID: "))
    title = input("Enter subject title: ")
    per_hour_rate = float(input("Enter per hour rate: "))
    
    values = [courseid, title, per_hour_rate, 0]
    
    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()
    
    print("\nSubject inserted successfully!")
    input("Press any key to continue...")

def Selectsubject(SQLCommand=None, courseid=None):
    cursor = database.connect.cursor(dictionary=True)
    
    if SQLCommand is None:
        sql = "SELECT id, courseid, title, per_hour_rate FROM subject WHERE is_deleted = 0 ORDER BY id DESC"
        cursor.execute(sql)
    else:
        sql = SQLCommand
        cursor.execute(sql, (courseid,))
        
    table = cursor.fetchall()
    
    print("\n" + "_"*85)
    print(f"{'id':<8} {'courseid':<12} {'title':<30} {'per_hour_rate':<15}")
    print("-"*85)
    
    count = 0
    for row in table:
        print(f"{row['id']:<8} {row['courseid']:<12} {str(row['title']):<30} {str(row['per_hour_rate']):<15}")
        count += 1
        
        if count == 25:
            input("\nPress any key to see more records...")
            count = 0
            
    print("_"*85)
    input("\nPress any key to continue...")

def Updatesubject():
    sql = "UPDATE subject SET courseid=%s, title=%s, per_hour_rate=%s WHERE id=%s AND is_deleted=0"
    
    id = int(input("Enter subject id to update: "))
    courseid = int(input("Enter new course ID: "))
    title = input("Enter new subject title: ")
    per_hour_rate = float(input("Enter new per hour rate: "))
    
    values = [courseid, title, per_hour_rate, id]
    
    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()
    
    if cursor.rowcount != 0:
        print("\nSubject updated successfully!")
    else:
        print("\nSubject not found or no changes made.")
    input("Press any key to continue...")

def Deletesubject():
    sql = "UPDATE subject SET is_deleted = 1 WHERE id = %s"

    id = int(input("Enter course ID to delete: "))

    cursor = database.connect.cursor()
    cursor.execute(sql, (id,))
    database.connect.commit()

    if cursor.rowcount != 0:
        print("\nSubject deleted successfully (Soft Delete)!")
    else:
        print("\ncourse ID not found in subject table.")

    input("Press any key to continue...")

def Searchsubject():
    courseid = int(input("Enter course ID to search subjects: "))
    
    sql = """
        SELECT id, courseid, title, per_hour_rate 
        FROM subject 
        WHERE courseid = %s AND is_deleted = 0 
        ORDER BY id DESC
    """
    
    # Redirecting to Selectsubject with custom query
    Selectsubject(SQLCommand=sql, courseid=courseid)