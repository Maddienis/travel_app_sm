import sqlite3

try:
	conn = sqlite3.connect('places_data.db')
	print('Opened database')

except Exception as e:
	print('Error durring connection: ', str(e))


results = conn.execute("SELECT name FROM all_food LIMIT 3")

for row in results:
	print(row)



def add_venues(conn, df):
	sql = ''' INSERT INTO all_food(country, city, name, address, price_level,
	rating, user_ratings_total, types, latitude, longitude, place_id)
	VALUES(?,?,?,?,?,?,?,?,?,?,?) '''

	conn.executemany(sql, df.to_records(index=False))
	conn.commit
	return 

conn.close()

