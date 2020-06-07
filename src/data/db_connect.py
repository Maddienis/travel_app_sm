import sqlite3
import pandas as pd

try:
	conn = sqlite3.connect('/Users/tristannisbet/Documents/travel_app/notebooks/test.db')
	print('Opened database')

except Exception as e:
	print('Error durring connection: ', str(e))


# Where does my connnection function have to be?
# Change db 
def write_db(table_name, df):
    try:
        conn = sqlite3.connect('/Users/tristannisbet/Documents/travel_app/notebooks/test.db')

    except Exception as e:
        print('Error durring connection: ', str(e))

    try:
        df.to_sql(table_name, con=conn, if_exists="append", index=False)
        
    except sqlite3.DatabaseError as er:
        print('er:', er.message)

    return 


def get_city():
	city_df = pd.read_sql_query("select * from city_country limit 3;", conn)

	return city_df

df = get_city()
print(df)
#conn.close()

