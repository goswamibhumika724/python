import connection as database

def Addlecture():
    cursor = database.connect.cursor(dictionary=True)

    teacherid = int(input('enter teacher id :'))
    subjectid = int(input('enter subject id :'))
    batchid = int(input('enter batch id :'))
    duration = int(input('enter lecture duration (in minutes):'))
    lecturedate = input('enter lecture date (yyyy-mm-dd):')

    cursor.execute('select per_hour_rate from subject where id = %s and is_deleted = 0',(subjectid,))
    subject_row = cursor.fetchone()

    if not subject_row:
        print('\n[-] invalid subject id or subject is deleted. cannot insert lecture.\n ')
        return
    
    per_hour_rate = subject_row['per_hour_rate']
    amount = (duration / 60) * float(per_hour_rate)

    sql = 'insert into lecture (teacherid, subjectid, batchid, duration_in_minutes, amount,lecturedate, paymentid) values (%s, %s, %s, %s, %s, %s, 0)'

    values = [teacherid,subjectid,batchid,duration,amount,lecturedate]

    cursor.execute(sql,values)
    database.connect.commit()
    
    print(f'\n[+] lecture inserted successfully! calculated amount: {amount:.2f}\n')
    input("Press any key to continue...")

def Selectlecture(SQLCommand=None, search_val=None):
    cursor = database.connect.cursor(dictionary=True)
    
    if SQLCommand is None:
        # Fetch all records sorted by ID in descending order
        sql = "SELECT id, teacherid, subjectid, batchid, duration_in_minutes, amount, lecturedate, paymentid FROM lecture ORDER BY id DESC"
        cursor.execute(sql)
    else:
        sql = SQLCommand
        cursor.execute(sql, (search_val,))
        
    table = cursor.fetchall()
    
    # Table headers alignment and sizing
    print("\n" + "_"*115)
    print(f"{'id':<6} {'teacherid':<11} {'subjectid':<11} {'batchid':<9} {'duration(m)':<13} {'amount':<12} {'date':<12} {'paymentid':<10}")
    print("-"*115)
    
    count = 0
    for row in table:
        print(f"{row['id']:<6} {str(row['teacherid']):<11} {str(row['subjectid']):<11} {str(row['batchid']):<9} {str(row['duration_in_minutes']):<13} {str(row['amount']):<12} {str(row['lecturedate']):<12} {str(row['paymentid']):<10}")
        count += 1
        
        # Pause execution after printing every 25 records
        if count == 25:
            input("\nPress any key to see more records...")
            count = 0
            
    print("_"*115)
    input("\nPress any key to continue...")