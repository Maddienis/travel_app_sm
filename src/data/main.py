import pandas as pd
import api_functions


def pipeline(city, query):
	url = build_query(city, query)
    data = find_places_api(url)
    df = create_df(data, city)
    
    return df