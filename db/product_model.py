from db.database import get_product_db

with get_product_db() as conn:
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Products(Id INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT,Price Int,Quantity Int,Type TEXT)")


def additem(name,price,quantity,type):
    with get_product_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Products(Name,Price,Quantity,Type) VALUES(?,?,?,?)",(name,price,quantity,type))
        return "Added SUccessfully"

def getallitems():
    with get_product_db() as conn:
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Products")
        data=cursor.fetchall()
        return data

def getitemsbyid(id):
    with get_product_db() as conn:
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE Id = ? ",(id,))
        data=cursor.fetchone()
        return {"data":data}

def getitemsbytype(type):
    with get_product_db() as conn:
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Products WHERE Type = ? ",(type,))
        data=cursor.fetchall()
        return data
    
def updateitems(id,price=None,quantity=None):
        if id:
            with get_product_db() as conn:
                cursor = conn.cursor()
            if price and not quantity:
                cursor.execute("UPDATE Products SET Price = ? WHERE Id = ?",(id,price))
            elif not price and  quantity:
                cursor.execute("UPDATE Products SET Quantity = ? WHERE Id = ?",(id,quantity))
            elif price and  quantity:
                cursor.execute("UPDATE Products SET Price = ?, Quantity WHERE Id = ?",(id,quantity,price))
            else:
                return "No Updates Provided"
        else:
            return "No Id Provided"

def deleteitems(id):
    if id :
        with get_product_db() as conn:
            cursor=conn.cursor()
            cursor.execute("DELETE FROM Products WHERE Id = ?",(id,))
            return f"Deleted Successfully {id}"
    else:
        return "No Id Provided"