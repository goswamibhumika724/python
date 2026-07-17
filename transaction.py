import connection as database
import tour as t 

def Addtransaction():
    t.viewtour()
    tourid = input("Enter Tour ID :")
    amount = float(input("Enter Amount :"))

    flag = int(input("Enter Transaction Type (1=income,2=expense) :"))

    description = input("Enter Description : ")
    challano = input("Enter Challa No : ")
    trandate = input("Enter Transaction Date (YYYY-MM-DD) : ")

    sql = "INSERT INTO transaction (tourid,amount,flag,description,challano,trandate,is_deleted) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    values = [tourid, amount, flag, description, challano, trandate, 0]

    cursor = database.connect.cursor()
    cursor.execute(sql, values)
    database.connect.commit()

    print("Transaction Added Successfully")
    key = input("Press any key to continue")

def Searchtransaction():
    description = input("Enter Transaction Description : ")

    sql = '''
        SELECT id, tourid, amount, flag, description, challano, trandate
        FROM transaction
        WHERE description LIKE %s
        AND is_deleted = 0
        ORDER BY id
    '''

    cursor = database.connect.cursor(dictionary=True)

    cursor.execute(sql, (f"%{description}%",))

    table = cursor.fetchall()

    if len(table) == 0:
        print("No transaction found")
    else:
        print(f"{'id':<5} {'tourid':<8} {'amount':<10} {'type':<10} {'description':<25} {'challano':<12} {'date':<12}")
        print("_" * 100)

        for row in table:
            print(
                f"{row['id']:<5} "
                f"{row['tourid']:<8} "
                f"{row['amount']:<10} "
                f"{row['flag']:<10} "
                f"{row['description']:<25} "
                f"{row['challano']:<12} "
                f"{str(row['trandate']):<12}"
            )

        print("_" * 100)

    input("Press any key to continue")
def Displaytransaction():
    sql = """
    SELECT id, tourid, amount, flag, description, challano, trandate
    FROM transaction
    WHERE is_deleted = 0
    ORDER BY id
    """

    # create cursor
    cursor = database.connect.cursor(dictionary=True)

    # run sql command
    cursor.execute(sql)

    # fetch all records
    table = cursor.fetchall()

    if len(table) == 0:
        print("No transaction found")
    else:
        print(f"{'id':<5} {'tourid':<8} {'amount':<12} {'type':<10} {'description':<30} {'challano':<12} {'date':<12}")
        print("_"*100)

        TotalIncome = 0
        TotalExpense = 0
        Count = 0

        for row in table:

            if row['flag'] == 1:
                type = "Income"
                TotalIncome += row['amount']
            else:
                type = "Expense"
                TotalExpense += row['amount']

            print(f"{row['id']:<5} {row['tourid']:<8} {row['amount']:<12} {type:<10} {row['description']:<30} {row['challano']:<12} {str(row['trandate']):<12}")

            Count += 1

        print("_"*100)

        Balance = TotalIncome - TotalExpense

        print(f"Total Transaction = {Count}")
        print(f"Total Income      = {TotalIncome}")
        print(f"Total Expense     = {TotalExpense}")
        print(f"Balance           = {Balance}")

    key = input("Press any key to continue")
def Deletetransaction():
    Displaytransaction()

    id = int(input("Enter Transaction id to delete : "))

    cursor = database.connect.cursor()

    # check id exists
    sql1 = "SELECT COUNT(id) FROM transaction WHERE id = %s AND is_deleted = 0"

    cursor.execute(sql1, [id])

    count = cursor.fetchone()[0]

    if count == 0:
        print("Transaction id not found")
    else:
        sql = "UPDATE transaction SET is_deleted = 1 WHERE id = %s"

        cursor.execute(sql, [id])

        database.connect.commit()

        print("Transaction deleted successfully")

    key = input("Press any key to continue")