import pandas as pd
import glob
import os


data_path = r"C:\Users\gi-to\OneDrive\Documentos\Área de Trabalho\E-commerce\archive"


customers = pd.read_csv(f"{data_path}\\olist_customers_dataset.csv")
geolocation = pd.read_csv(f"{data_path}\\olist_geolocation_dataset.csv")
orders = pd.read_csv(f"{data_path}\\olist_orders_dataset.csv")
order_items = pd.read_csv(f"{data_path}\\olist_order_items_dataset.csv")
payments = pd.read_csv(f"{data_path}\\olist_order_payments_dataset.csv")
reviews = pd.read_csv(f"{data_path}\\olist_order_reviews_dataset.csv")
products = pd.read_csv(f"{data_path}\\olist_products_dataset.csv")
sellers = pd.read_csv(f"{data_path}\\olist_sellers_dataset.csv")
category_translation = pd.read_csv(f"{data_path}\\product_category_name_translation.csv")
