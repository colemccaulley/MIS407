import sqlite3

sqlite_file = 'dbsample.sqlite'
table_name = 'person'  # name of the table access

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

print("The Greats of Hockey DB.")

lname = str(input("Last Name = "))
c.executescript("SELECT * FROM {v1} WHERE lname='{v2}';".
                format(v1=table_name, v2=lname))

all_rows = c.fetchall()
print('1):', all_rows)
print(type(all_rows))

conn.commit()
conn.close()
