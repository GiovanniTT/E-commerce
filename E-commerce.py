import pandas as pd
import glob
import os
import numpy as np

data_path = r"C:\Users\gi-to\OneDrive\Documentos\Área de Trabalho\E-commerce\archive (1)"

customers = pd.read_csv(f"{data_path}\\customers.csv")
geolocation = pd.read_csv(f"{data_path}\\geolocation.csv")
order_items = pd.read_csv(f"{data_path}\\order_items.csv")
payments = pd.read_csv(f"{data_path}\\payments.csv")
orders = pd.read_csv(f"{data_path}\\orders.csv")
products = pd.read_csv(f"{data_path}\\products.csv")
sellers = pd.read_csv(f"{data_path}\\sellers.csv")
orders = pd.read_csv(f"{data_path}\\orders.csv")

col_data = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]

orders[col_data] = orders[col_data].apply(pd.to_datetime, errors='coerce')

# Verificar tipos
#print("\nOrders:\n", orders.info())
#print("\nProducts:\n", products.info())
#print("\nOrder Items:\n", order_items.info())
#print("\nPayments:\n", payments.info())
#print("\nCustomers:\n", customers.info())
#print("\nGeolocation:\n", geolocation.info())
#print("\nSellers:\n", sellers.info())

dataframes = {
    'orders': orders,
    'products': products,
    'order_items': order_items,
    'payments': payments,
    'customers': customers,
    'geolocation': geolocation,
    'sellers': sellers
}

for name, df in dataframes.items():
    print("Valores nulos")
    print(f"{name}:\n", df.isnull().sum())
