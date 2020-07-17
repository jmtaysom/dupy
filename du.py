from pathlib import Path
from os.path import getsize

path = Path('.')
for f in path.iterdir():
    print(f'{getsize(f):<10} {f.absolute()}')

