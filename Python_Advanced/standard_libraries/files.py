from pathlib import Path
import shutil

path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
print(path.stat())

# Reading a file
with open("__init__.py", "r") as file:
    pass

path.read_bytes()
path.read_text(encoding="utf-8")

# Writing
path.write_text(".....")
# path.write_bytes()

# Copying
target = Path("Some path")

shutil.copy(path, target)

