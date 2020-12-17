import sqlite3
import pandas as pd
import mysql.connector
import os
#from flaskext.mysql import MySQL


if 'RDS_HOTNAME' in os.environ:
    DATABASE ={
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT']
    }

else:
    DATABASE ={
        'NAME': os.getenv('RDS_DB_NAME'),
        'USER': os.getenv('RDS_USERNAME'),
        'PASSWORD': os.getenv('RDS_PASSWORD'),
        'HOST': os.getenv('RDS_HOSTNAME'),
        'PORT': os.getenv('RDS_PORT')
    }



#Old code to check if table already exits, if not write it to database. Used when hitting google api
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


def get_df_old(table_name):
    try:
        conn = sqlite3.connect('/Users/tristannisbet/Documents/travel_app/places.db')

    except Exception as e:
        print('Error durring connection: ', str(e))
    
    sql = """select * from {}""".format(table_name)
    df = pd.read_sql_query(sql, conn)

    return df

def get_df(table_name):
    try:
        db_connect = mysql.connector.connect(host= DATABASE['HOST'],
                    user = DATABASE['USER'],
                    passwd = DATABASE['PASSWORD'],
                    db = DATABASE['NAME'])
    except Exception as e:
        print('Error durring connection: ', str(e))
    
    sql = """select * from {}""".format(table_name)
    df = pd.read_sql(sql, db_connect)

    return df


def get_country(city_name):
    try:
        db_connect = mysql.connector.connect(host= DATABASE['HOST'],
                    user = DATABASE['USER'],
                    passwd = DATABASE['PASSWORD'],
                    db = DATABASE['NAME'])
    except Exception as e:
        print('Error durring connection: ', str(e))


    cursor = db_connect.cursor()

    sql = """select country from cities where city = '%s'"""%  (city_name)
    cursor.execute(sql)

    country = cursor.fetchone()
    country_txt = str(country)
    country_txt = country_txt.strip("()'',")
    return country_txt




