from pathlib import Path

path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# Iterating over a path

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.glob('*.py')]
print(py_files)