import sqlite3

try:
	conn = sqlite3.connect('places_data.db')
	print('Opened database')

except Exception as e:
	print('Error durring connection: ', str(e))


results = conn.execute("SELECT name FROM all_food LIMIT 3")

for row in results:
	print(row)



def write_db(table_name, df, conn):
    df.to_sql(table_name, conn, if_exists="append")


conn.close()

