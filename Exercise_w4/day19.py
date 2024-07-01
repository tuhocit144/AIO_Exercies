import pandas as pd
import sqlite3
# Tạo kết nối tới CSDL có tên là product.qlite

connection = sqlite3.connect('product.sqlite')
cursor = connection.cursor()
# c1

# create table PRODUCT :
cursor.execute("""
    CREATE TABLE PRODUCT (
    ID INTEGER PRIMARY KEY ,
    NAME TEXT NOT NULL ,
    PRICE INTEGER NOT NULL
    );"""
               )
# c2
# Insert data
cursor.execute("""
INSERT INTO PRODUCT (ID , NAME , PRICE )
VALUES
(1,'Iphone 15',18000000) ,
(2 ,'Galaxy Z-Fold 5',30000000) ;
""")

connection.commit()
# c3
# Lấy tất cả data từ bảng PRODUCT
data = pd.read_sql_query("SELECT * FROM product", connection)
print(data)
# c3: update price of Galaxy Z-Fold 5 to 50000000
cursor.execute("""
UPDATE PRODUCT set PRICE=50000000 WHERE NAME='Galaxy Z-Fold 5'
""")
data = pd.read_sql_query("SELECT * FROM product", connection)
print(data)
# c4: delete iphone 15
cursor.execute("""
DELETE FROM PRODUCT WHERE NAME='Iphone 15'
""")
data = pd.read_sql_query("SELECT * FROM product", connection)
print(data)
