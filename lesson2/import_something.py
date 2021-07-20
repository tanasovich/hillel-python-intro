import re
from re import search

string: str = "My name is Ludovic XVI"
print(search(r"ludovic", string, re.I).group(0))
