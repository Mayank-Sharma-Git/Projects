#Importing Libraries 

import pandas as pd
import openpyxl
from preprocessing.Connection import DBConnect 





class Preprocess:

    def load_data(path):

        customer = pd.read_excel(path, sheet_name='CustomerDetail')
        orders = pd.read_excel(path,sheet_name='Jan')

        return customer,orders
    
    def  data_cleaning(path):

        customer,orders = Preprocess.load_data(path)
        customer = customer.drop( columns = ['CustomerID','Month','DateInText','MonthName','Gender.1','Gender'])
        customer = customer.rename( columns = {'CustomerID.1':'Customer','Gender.2':'Gender'}) 
        customer = customer.dropna()
        customer['Order Date']  = pd.to_datetime(customer['Order Date'])

        orders = orders.rename( columns = {'Quantity ordered n':'Quantity'})
        orders = orders.dropna()

        customer.to_csv('dataset/customer.csv')
        orders.to_csv('dataset/orders.csv')

        return customer,orders

    def Data_SaveToDatabase(path):
        conn = DBConnect.getconnection()
        cur = conn.cursor()

        path = "dataset/Ecomm.xlsx"
        customer,orders = Preprocess.data_cleaning(path)
        for i in range(0,customer.shape[0]):
            cus = list(customer.loc[i])
            sql = "INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s)"
            data = (int(cus[0]),cus[2],cus[3],cus[4],cus[5],cus[1])
            cur.execute(sql,data)

        for i in range(0,orders.shape[0]):
            ord = list(orders.loc[i])
            sql = "INSERT INTO orders VAlUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            data = (int(ord[0]),int(ord[1]),float(ord[2]),float(ord[3]),int(ord[4]),ord[5],ord[6],ord[7])
            cur.execute(sql,data)

        conn.commit()
        cur.close()
        conn.close()

    






