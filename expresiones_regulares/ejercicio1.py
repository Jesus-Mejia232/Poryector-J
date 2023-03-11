import re

texto = "The quick brown fox jumps over the lazy dog"

x = re.search("^The.*dog$", texto)

if x:
    print("si")
else:
    print("No")
