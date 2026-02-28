from db.database import get_admin_db

with get_admin_db() as conn:
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Admin(AdminId INTEGER PRIMARY KEY, Name TEXT, Password TEXT)")

def login_check(name):
    with get_admin_db() as conn:
        cursor=conn.cursor()
        cursor.execute("SELECT 1 FROM Admin WHERE Name = ?",(name,))
        isAdmin=cursor.fetchone()
        if isAdmin :
            cursor.execute("SELECT Password FROM Admin WHERE Name = ?",(name,))
            password=cursor.fetchone()
            return password[0]
        else:
            return None

def admin_signup(adid,name,password):
    with get_admin_db() as conn:
        cursor=conn.cursor()
        cursor.execute("INSERT INTO Admin VALUES(?,?,?)",(adid,name,password))
        rowcount=cursor.rowcount
        if rowcount == 0:
            return None
        else:
            return True