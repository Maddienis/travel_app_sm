import sqlite3

try:
	conn = sqlite3.connect('places_data.db')
	print('Opened database')

except Exception as e:
	print('Error durring connection: ', str(e))


results = conn.execute("SELECT name FROM all_food")

for row in results:
	print(row)


conn.close()

