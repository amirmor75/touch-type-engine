import sqlite3
import uuid

paragraphs = [
    "Machine learning is a method of data analysis that automates analytical model building.",
    "It is a branch of artificial intelligence based on the idea that systems can learn from data."
]

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS paragraphs (
    id TEXT PRIMARY KEY,
    text TEXT,
    topic TEXT
)
''')

for text in paragraphs:
    cursor.execute(
        "INSERT INTO paragraphs (id, text, topic) VALUES (?, ?, ?)",
        (str(uuid.uuid4()), text.strip(), "ml")
    )

conn.commit()
conn.close()
