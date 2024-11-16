# 11.1 Create the file Zoo.py
def hours():
    print('Open 9-5 daily')

# use the interactive interpreter to import the zoo module and call its hours() function
>>> import zoo 
>>> zoo.hours()
open 9-5 daily 

# 11.2 Import the zoo module as menagerie and call its hours() function
>>> import zoo as menagerie
>>> menagerie.hours()
open 9-5 daily

# 16.1 - 16.8 

#16.1 
with open('books.csv', 'w') as file:
    file.write('author,boo\n')
    file.write('J R R Tolkien, The Hobbit\n')
    file.write('Lynne Truss, "Eats, Shoots & Leaves"\n')

#16.2 Use the CSV module and its DictReader method to read boooks.csv
import csv

with open('books.csv', 'r') as file:
    books = csv.Dictreader(file)
    for book in books:
        print(book)
# Yes, the DictReader handles the quotes and commas 

#16.3 Create a CSV file called books2.csv
with open('books2.csv', 'w') as file:
    file.write('title,author,year\n')
    file.write('The Weirdstone of Brisingamen, Alan Garner, 1960\n')
    file.write('Perdido Street Station, China Mieville, 2000\n')
    file.write('Thud!, Terry Pratchett, 2005\n')
    file.write('The Spellman FIles, Lisa Lutz, 2007\n')
    file.write('Small Gods, Terry Pratchett, 1992\n')

#16.4 Use the sqlite3 module to create a SQLite database and a table
import sqlite3 

conn = sqlite3.connect('books.db')
cur = cur.cursor()
cur.execute('''
            CREATE TABLE books (
               title TEXT,
               author TEXT,
               year INTEGER
    )
''')
conn.commit()
conn.close()

#16.5 Read books2.csv and insert its data into the books table
conn = sqlite3.connect('books.db') 
cur = conn.cursor()

with open('books2csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cur.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?,)'
                    (row['title'], row['author'], row['year']))
conn.commit()
conn.close()

# 16.6 select and print the title column from the books table in alphabetical order
conn = sqlite3.connect('books.db')
cur = conn.cursor()

cur.execute('SELECT title FROM books ORDER BY title') 
titles = cur.fetchall()
for title in titles:
    print(title[0])

conn.close()

#16.7 Select and print all columns from the books tables in order of publication
conn = sqlite3.connect('books.db')
cur = conn.cursor()

cur.execute('SELECT * FROM books ORDER BY year')
books = cur.fetchall()
for book in books:
    print(book)

conn.close()

from sqlalchemy import create_engine, select, MetaData, Table

engine = create_engine('sqlite:///books.db')
metadata = MetaData()
books = Table('books', metadata, autoload_with=engine)

with engine.connect() as conn:
    query = select([books.c.title]).order_by(books.c.title)
    results = conn.execute(query)
    for result in results:
        print(result[0])