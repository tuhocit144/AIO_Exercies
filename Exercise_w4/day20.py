import sqlite3
# Tạo kết nối tới CSDL có tên là product_d20_sqlite
# 
connection = sqlite3.connect ('product_d20_sqlite')
cursor = connection.cursor ()
#c1

# create table STOCK :
cursor.execute ("""
    CREATE TABLE STOCK (
    ID INTEGER PRIMARY KEY ,
    NAME TEXT NOT NULL ,
    BUY INTEGER NOT NULL,
    INVESTOR TEXT NOT NULL          
    );"""
)
#c2
# Insert data 
cursor.execute ("""
INSERT INTO STOCK (ID , NAME , BUY, INVESTOR )
VALUES
(1,'ACB',29.45,'Nguyen') ,
(2 ,'VIC',44.55,'Nguyen'),
(3,'GMD',74.30,'Nguyen'),
(4,'ACB',28.45,'Vinh') ,
(5 ,'VIC',40.55,'Vinh'),
(6,'GMD',60.30,'Vinh');
""")

connection.commit ()
#c3
import pandas as pd
# Lấy tất cả data từ bảng PRODUCT
data = pd.read_sql_query ("SELECT sum(buy) FROM stock", connection )
print ( f'Ket qua tong gia ban la :{data}' )
#c3: IN RA GIA BUY LON NHAT THEO TUNG NHA DAU TU
data = pd.read_sql_query ("""SELECT ID, NAME, MAX(BUY) 
                FROM STOCK
                GROUP BY INVESTOR""", connection )
print ( data )
