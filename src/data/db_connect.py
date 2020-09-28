import sqlite3
import pandas as pd

try:
	conn = sqlite3.connect('/Users/tristannisbet/Documents/travel_app/places.db')
	print('Opened database')

except Exception as e:
	print('Error durring connection: ', str(e))


# Where does my connnection function have to be?
def write_db(table_name, df):
    try:
        conn = sqlite3.connect('/Users/tristannisbet/Documents/travel_app/places.db')

    except Exception as e:
        print('Error durring connection: ', str(e))

    try:
        df.to_sql(table_name, con=conn, if_exists="append", index=False)
        
    except sqlite3.DatabaseError as er:
        print('Database Error:', er)

    return 


def get_city():
	city_df = pd.read_sql_query("select * from city_country;", conn)

	return city_df

def check_db(table_name, city):
    try:
        conn = sqlite3.connect('/Users/tristannisbet/Documents/travel_app/places.db')

    except Exception as e:
        print('Error durring connection: ', str(e))

    cur = conn.cursor()
    try:
        cur.execute("""SELECT city from {} where city = '{}'""".format(table_name, city))
        result = cur.fetchone()
    except sqlite3.DatabaseError as er:
        print(er)
        result = []
 
    return result


def get_df(table_name):
    try:
        conn = sqlite3.connect('/Users/tristannisbet/Documents/travel_app/places.db')

    except Exception as e:
        print('Error durring connection: ', str(e))
    
    sql = """select * from {}""".format(table_name)
    df = pd.read_sql_query(sql, conn)

    return df


