import connection as database


def displayReport(sql, params=None):

    cursor = database.connect.cursor(dictionary=True)

    if params:
        cursor.execute(sql, params)
    else:
        cursor.execute(sql)

    table = cursor.fetchall()
    cursor.close()

    if len(table) == 0:
        print("\nNo records found.")
    else:

        columns = list(table[0].keys())

        widths = {}

        for col in columns:
            widths[col] = max(
                len(col),
                max(len(str(row[col])) for row in table)
            )

        print()

        header = " | ".join(
            f"{col:<{widths[col]}}" for col in columns
        )

        print(header)
        print("-" * len(header))

        for row in table:
            print(
                " | ".join(
                    f"{str(row[col] if row[col] is not None else ''):<{widths[col]}}"
                    for col in columns
                )
            )

        print()


# 1) Month wise income expense report

def MonthWiseReport():

    year = input("Enter Year (YYYY): ")
    month = input("Enter Month (1-12): ")

    sql = """
    SELECT 
        SUM(CASE WHEN flag=1 THEN amount ELSE 0 END) AS Income,
        SUM(CASE WHEN flag=2 THEN amount ELSE 0 END) AS Expense,
        SUM(CASE WHEN flag=1 THEN amount ELSE -amount END) AS Balance
    FROM transaction
    WHERE YEAR(trandate)=%s
    AND MONTH(trandate)=%s
    AND is_deleted=0
    """

    displayReport(sql, (year, month))


# 2) Quarter wise income expense report

def QuarterWiseReport():

    year = input("Enter Year (YYYY): ")
    quarter = int(input("Enter Quarter (1-4): "))

    start_month = (quarter-1)*3 + 1
    end_month = start_month + 2

    sql = """
    SELECT 
        SUM(CASE WHEN flag=1 THEN amount ELSE 0 END) AS Income,
        SUM(CASE WHEN flag=2 THEN amount ELSE 0 END) AS Expense,
        SUM(CASE WHEN flag=1 THEN amount ELSE -amount END) AS Balance
    FROM transaction
    WHERE YEAR(trandate)= %s
    AND MONTH(trandate) BETWEEN %s AND %s
    AND is_deleted=0
    """

    displayReport(sql,(year,start_month,end_month))


# 3) Year wise income expense report

def YearWiseReport():

    year = input("Enter Year (YYYY): ")

    sql = """
    SELECT 
        SUM(CASE WHEN flag=1 THEN amount ELSE 0 END) AS Income,
        SUM(CASE WHEN flag=2 THEN amount ELSE 0 END) AS Expense,
        SUM(CASE WHEN flag=1 THEN amount ELSE -amount END) AS Balance
    FROM transaction
    WHERE YEAR(trandate)= %s
    AND is_deleted=0
    """

    displayReport(sql,(year,))


# 4) Tour wise report (single tour)

def TourWiseReport():

    tourid = input("Enter Tour ID : ")

    sql = """
    SELECT
        tourid,
        SUM(CASE WHEN flag=1 THEN amount ELSE 0 END) AS Income,
        SUM(CASE WHEN flag=2 THEN amount ELSE 0 END) AS Expense,
        SUM(CASE WHEN flag=1 THEN amount ELSE -amount END) AS Balance
    FROM transaction
    WHERE tourid=%s
    AND is_deleted=0
    GROUP BY tourid
    """

    displayReport(sql,(tourid,))


# 5) All tour wise report

def AllTourWiseReport():

    sql = """
    SELECT
        tourid,
        SUM(CASE WHEN flag=1 THEN amount ELSE 0 END) AS Income,
        SUM(CASE WHEN flag=2 THEN amount ELSE 0 END) AS Expense,
        SUM(CASE WHEN flag=1 THEN amount ELSE -amount END) AS Balance
    FROM transaction
    WHERE is_deleted=0
    GROUP BY tourid
    ORDER BY tourid
    """

    displayReport(sql)