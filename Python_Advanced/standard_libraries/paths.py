from pathlib import Path

path = Path(r"C:\ecommerce\__init__.py")

# Combining paths
Path() / "ecommerce.ini"

# Get home directory
Path().home()

path.exists()
path.is_file()
path.is_dir()

print(path.name)
print(path.stem) # path without extension
print(path.suffix) # extension
print(path.parent)

# Changing paths
path = path.with_name("file.txt")
path = path.with_suffix(".txt")
print(path)