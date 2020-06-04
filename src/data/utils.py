import pandas as pd


def format_city(city_list):
    city_list.replace(' ', '+', regex=True, inplace=True)
    return city_list