import sqlite3
con = sqlite3.connect("StudentRecord.db")
cur = con.cursor()
# cur.execute("CREATE TABLE students(id, name, age, major)")
res = cur.execute("SELECT name FROM sqlite_master;")
res.fetchone()
('students',)

cur.execute("INSERT INTO students VALUES ('id1', 'Martha', '16', 'Biology'), ('id2', 'Greg', '20', 'business'), ('id3', 'Lizzie', '32', 'Chemistry'), ('id4', 'Richie', '50', 'Criminal Justice'), ('id5', 'Taylor', '25', 'Art History')")
res = cur.execute("SELECT name FROM students")
# res.fetchall()
for row in cur.execute("SELECT major, name, age FROM students ORDER BY id"):
    print(row)

s_id = input('id')
s_name = input('name')
s_age = input('age')
s_major = input('major')
cur.execute("INSERT INTO students(id, name, age, major) VALUES (?,?,?,?)", (s_id, s_name, s_age, s_major))
con.commit ()
print('Data entered successfully.')
con.close ()
if (con):
    con.close()
    print("\nThe SQLite connection is closed.")