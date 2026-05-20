
from preprocessing.utlities import Preprocess
from preprocessing.Connection import DBConnect


path = "dataset/Ecomm.xlsx"

Preprocess.Data_SaveToDatabase(path)


sql = "SELECT o.*,cname,state,city,gender,orderdate FROM orders o JOIN customers c ON o.cid=c.cid"

conn = DBConnect.getconnection()

cur = conn.cursor()
cur.execute(sql)
data = cur.fetchall()
cur.close()
conn.close()

































