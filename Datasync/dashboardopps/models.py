from django.db import models
import pandas as pd

# Create your models here.
class Removeduplicate():
    orders = pd.read_excel(r'C:\Users\oluwatosin.peters\Downloads\ZONAL_ARCHIVES_AND_BRANCHES_ACCOMODATED\SOUTH SOUTH ZONE ARCHIVES AND BRANCHES.xlsx')
#print(orders)
    orders.drop_duplicates()
