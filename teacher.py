import connection as database

def Addteacher():
    
    sql = """
        INSERT INTO teacher (name, mobile, email, gender, qualification, experience, is_deleted) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    
    name = input("Enter teacher name: ")
    mobile = input("Enter mobile number: ")
    email = input("Enter email address: ")
    gender = input("Enter gender (Male/Female): ")
    qualification = input("Enter qualification: ")
    experience = float(input("Enter experience (in years): "))
    
    values = [name, mobile, email, gender, qualification, experience, 0]
    
    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()
    cursor.close()
    
    print("\nTeacher inserted successfully!")
    input("Press any key to continue...")

def Selectteacher(SQLCommand=None, search_val=None):
    cursor = database.connect.cursor(dictionary=True)
    
    if SQLCommand is None:
        sql = "SELECT id, name, mobile, email, gender, qualification, experience FROM teacher WHERE is_deleted = 0 ORDER BY id DESC"
        cursor.execute(sql)
    else:
        sql = SQLCommand
        cursor.execute(sql, (search_val,))
        
    table = cursor.fetchall()
    
    
    print("\n" + "_"*125)
    print(f"{'id':<6} {'name':<22} {'mobile':<13} {'email':<25} {'gender':<8} {'qualification':<20} {'experience':<10}")
    print("-"*125)
    
    count = 0
    for row in table:
        print(f"{row['id']:<6} {str(row['name']):<22} {str(row['mobile']):<13} {str(row['email']):<25} {str(row['gender']):<8} {str(row['qualification']):<20} {str(row['experience']):<10}")
        count += 1
        
        if count == 25:
            input("\nPress any key to see more records...")
            count = 0
            
    print("_"*125)
    input("\nPress any key to continue...")

def Updateteacher():
    sql = """
        UPDATE teacher 
        SET name=%s, mobile=%s, email=%s, gender=%s, qualification=%s, experience=%s 
        WHERE id=%s AND is_deleted=0
    """
    
    id = int(input("Enter teacher ID to update: "))
    name = input("Enter new name: ")
    mobile = input("Enter new mobile: ")
    email = input("Enter new email: ")
    gender = input("Enter new gender: ")
    qualification = input("Enter new qualification: ")
    experience = float(input("Enter new experience: "))
    
    values = [name, mobile, email, gender, qualification, experience, id]
    
    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()
    cursor.close()
    
    if cursor.rowcount != 0:
        print("\nTeacher updated successfully!")
    else:
        print("\nTeacher ID not found or no changes made.")
    input("Press any key to continue...")

def Deleteteacher():
    sql = "UPDATE teacher SET is_deleted = 1 WHERE id = %s"

    id = int(input("Enter teacher ID to delete: "))
    values = [id]

    cursor = database.connect.cursor()
    cursor.execute(sql,values)
    database.connect.commit()
    

    if cursor.rowcount != 0:
        print("\nTeacher deleted successfully (Soft Delete)!")
    else:
        print("\nTeacher ID not found.")

    input("Press any key to continue...")

def Searchteacher():
    name = input("Enter teacher name to search: ")
    
    search_val = f"%{name}%"
    sql = """
        SELECT id, name, mobile, email, gender, qualification, experience 
        FROM teacher 
        WHERE name LIKE %s AND is_deleted = 0 
        ORDER BY id DESC
    """
    
    Selectteacher(SQLCommand=sql, search_val=search_val)