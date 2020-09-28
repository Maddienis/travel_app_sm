import pandas as pd
import numpy as np


def format_city_for_url(city_list):
	city_list.replace(' ', '+', regex=True, inplace=True)

	return city_list

def find_table_name(query_dict, query):
    table_name = (list(query_dict.keys())[list(query_dict.values()).index(query)])
    
    return table_name
