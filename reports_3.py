import connection as database
from reports import displayReport

# 6) Batch wise lecture detail between given date

def BatchWiseLectureBetweenDates():

    batch_id = input("Enter Batch ID: ")
    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    end_date = input("Enter End Date (YYYY-MM-DD): ")

    sql = """
    SELECT 
        l.id AS Lecture_ID,
        l.lecturedate AS Lecture_Date,
        b.id AS Batch_ID,
        s.title AS Subject_Name,
        t.name AS Teacher_Name,
        l.duration_in_minutes AS Duration_Mins,
        l.amount AS Amount
    FROM lecture l
    JOIN batch b ON l.batchid = b.id
    JOIN subject s ON l.subjectid = s.id
    JOIN teacher t ON l.teacherid = t.id
    WHERE l.batchid = %s
    AND l.lecturedate BETWEEN %s AND %s
    ORDER BY l.lecturedate ASC
    """

    displayReport(sql, (batch_id, start_date, end_date))


# 7) Batch wise lecture detail with total amount

def BatchWiseLectureTotalAmount():

    sql = """
    SELECT 
        b.id AS Batch_ID,
        c.title AS Course_Name,
        COUNT(l.id) AS Total_Lectures,
        COALESCE(SUM(l.duration_in_minutes), 0) AS Total_Duration_Mins,
        COALESCE(SUM(l.amount), 0) AS Total_Amount
    FROM batch b
    JOIN course c ON b.courseid = c.id
    LEFT JOIN lecture l ON b.id = l.batchid
    GROUP BY b.id, c.title
    ORDER BY b.id ASC
    """

    displayReport(sql)