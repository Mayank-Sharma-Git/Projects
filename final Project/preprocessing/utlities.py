#Importing Libraries 

import pandas as pd
import openpyxl

class Preprocess:

    def load_data(path):

        customer = pd.read_excel(path, sheet_name='CustomerDetail')
        orders = pd.read_excel(path,sheet_name='Jan')
        return customer,orders
    
    def  data_cleaning():
        path = "../dataset/Ecomm.xlsx"
        customer,orders = Preprocess.load_data(path)
        customer = customer.drop( columns = ['CustomerID','Month','DateInText','Gender.1','Gender'])
        customer = customer.rename( columns = {'CustomerID.1':'Customer','Gender.2':'Gender'}) 
        customer = customer.dropna()
        orders = orders.rename( columns = {'Quantity ordered n':'Quantity'})
        orders = orders.dropna()
        customer.to_csv('../dataset/customer.csv')
        orders.to_csv('../dataset/orders.csv')
        return customer,orders










