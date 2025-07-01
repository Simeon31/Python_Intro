from pathlib import Path
from zipfile import ZipFile

# Writing zip files
with ZipFile("files.zip", "w") as zipFile:
    for path in Path("ecommerce").rglob("*.*"):
        zipFile.write(path)

# Reading zip files
with ZipFile("files.zip") as zipFile:
    print(zipFile.namelist())
