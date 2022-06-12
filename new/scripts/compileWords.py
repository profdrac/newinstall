import textwrap
from pathlib import Path
from prettytable import PrettyTable

t = PrettyTable(['Word','Meaning'])
t.align['Word'] = 'l'
t.align['Meaning'] = 'l'
for child in Path('/home/ashu/Documents/words').iterdir():
    if child.is_file():
        t.add_row([child.name,'\n'.join(textwrap.wrap(child.read_text(),70))+'\n'])
print(t)
