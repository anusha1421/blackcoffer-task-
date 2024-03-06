import sqlite3
import json

# Create a database
conn = sqlite3.connect('dashboard.db')
c = conn.cursor()

# Create a table for the json data
c.execute('''CREATE TABLE IF NOT EXISTS insights
             (id INTEGER PRIMARY KEY,
             end_year TEXT,
             intensity INTEGER,
             likelihood INTEGER,
             relevance INTEGER,
             sector TEXT,
             topic TEXT,
             region TEXT,
             country TEXT,
             source TEXT,
             title TEXT,
             url TEXT,
             added TEXT,
             published TEXT)''')

# Load the json data
with open('jsondata.json') as f:
    data = json.load(f)

# Insert the json data into the database
for item in data:
    c.execute("INSERT INTO insights VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (item['id'],
                 item['end_year'],
                 item['intensity'],
                 item['likelihood'],
                 item['relevance'],
                 item['sector'],
                 item['topic'],
                 item['region'],
                 item['country'],
                 item['source'],
                 item['title'],
                 item['url'],
                 item['added'],
                 item['published']))

# Commit the changes and close the connection
conn.commit()
conn.close()