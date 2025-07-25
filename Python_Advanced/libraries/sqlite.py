import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())
# print(movies)

# Writing data to a database
# with sqlite3.connect("movies.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES (?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

# Reading from a database
with sqlite3.connect("movies.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)