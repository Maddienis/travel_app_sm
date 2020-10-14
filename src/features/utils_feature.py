import pandas as pd
import numpy as np
from sklearn import preprocessing as pp
import src.data.db_connect as db


def buildLabelEncoder():
    
    cities = db.get_df('cities')
    new_row = {'id': 200, 'city': 'Zx', 'country': 'None'}
    cities = cities.append(new_row, ignore_index=True)
    
    le = pp.LabelEncoder()
    le.fit(cities.city)
    
    return le