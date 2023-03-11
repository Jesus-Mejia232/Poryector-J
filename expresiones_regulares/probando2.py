import re

texto = "123 45 6789 12345 123456"

resultado = re.findall(r"\d{2,4}", texto)

print(resultado)
