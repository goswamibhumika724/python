import connection as database

def Addcourse():
    # SQL query with placeholders
    sql = "INSERT INTO course (title, fees, duration, description, is_deleted) VALUES (%s, %s, %s, %s, %s)"
    
    # Accept inputs from user
    title = input("Enter course title: ")
    fees = float(input("Enter course fees: "))
    duration = input("Enter course duration (Months): ")
    description = input("Enter course description: ")
    
    values = [title, fees, duration, description, 0]
    
    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()
    
    print("\nCourse inserted successfully!")
    input("Press any key to continue...")

def Selectcourse(SQLCommand=None, title=None):
    cursor = database.connect.cursor(dictionary=True)
    
    if SQLCommand is None:
        sql = "SELECT id, title, fees, duration, description FROM course WHERE is_deleted = 0 ORDER BY id DESC"
        cursor.execute(sql)
    else:
        sql = SQLCommand
        cursor.execute(sql, (f"%{title}%",))
        
    table = cursor.fetchall()
    
    print("\n" + "_"*110)
    print(f"{'id':<5} {'title':<30} {'fees':<12} {'duration':<15} {'description':<40}")
    print("-"*110)
    
    count = 0
    for row in table:
        print(f"{row['id']:<5} {row['title']:<30} {row['fees']:<12} {row['duration']:<15} {row['description'][:38]:<40}")
        count += 1
        
        if count == 25:
            input("\nPress any key to see more records...")
            count = 0
            
    print("_"*110)
    input("\nPress any key to continue...")

def Updatecourse():
    sql = "UPDATE course SET title=%s, fees=%s, duration=%s, description=%s WHERE id=%s AND is_deleted=0"
    
    id = int(input("Enter course id to update: "))
    title = input("Enter new course title: ")
    fees = float(input("Enter new course fees: "))
    duration = input("Enter new course duration: ")
    description = input("Enter new course description: ")
    
    values = [title, fees, duration, description, id]
    
    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()
    
    if cursor.rowcount != 0:
        print("\nCourse updated successfully!")
    else:
        print("\nCourse not found or no changes made.")
    input("Press any key to continue...")

def Deletecourse():
    # Soft delete logic (update operation)
    sql = "UPDATE course SET is_deleted = 1 WHERE id = %s"
    
    id = int(input("Enter course id to delete: "))
    values = [id]
    
    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()
    
    if cursor.rowcount != 0:
        print("\nCourse deleted successfully (Soft Delete)!")
    else:
        print("\nCourse not found.")
    input("Press any key to continue...")

def Searchcourse():
    title = input("Enter course title to search: ")
    
    sql = """
        SELECT id, title, fees, duration, description 
        FROM course 
        WHERE title LIKE %s AND is_deleted = 0 
        ORDER BY id DESC
    """
    
    # Redirecting to Selectcourse with custom query
    Selectcourse(SQLCommand=sql, title=title)