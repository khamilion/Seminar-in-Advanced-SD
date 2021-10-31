from main import *
from main import olympic_data
import sqlite3

# call the main function in the main module
main()

# create a connection to the database
con = sqlite3.connect('sports.db')

cur = con.cursor()

cur.execute('''CREATE TABLE olympics
            (name text, country text, position text, gold text, silver text, bronze text, total text)''')

con.commit()


for olympics in olympic_data.keys():
    #print(f"{olympics} \n")

    for country in olympic_data[olympics].keys():
        #print(f"{country}")

        cur.execute("INSERT INTO olympics VALUES (:name, :country, :position, :gold, :silver, :bronze, :total)",
                    {'name': olympics, 'country': country, 'position': olympic_data[olympics][country]['position'],
                     'gold': olympic_data[olympics][country]['gold'], 'silver': olympic_data[olympics][country]['silver'],
                     'bronze': olympic_data[olympics][country]['bronze'], 'total': olympic_data[olympics][country]['total']})
        con.commit()


for row in cur.execute('SELECT * FROM olympics'):
    print(row)
