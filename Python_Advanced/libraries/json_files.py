import json
from pathlib import Path
movies = [
    { "id": 1, "title": "The Lord of the Rings", "year": 2008 },
    { "id": 2, "title": "Spider-Man", "year": 2009 },
]

data = json.dumps(movies)
Path("movies.json").write_text(data)

# Reading JSON file
data_to_read = Path("movies.json").read_text()
movies_to_read = json.loads(data_to_read)
print(movies_to_read)