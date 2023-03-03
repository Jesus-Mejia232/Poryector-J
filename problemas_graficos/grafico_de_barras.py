import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\\cofla_ingresos.csv")

# Creando el gráfico
sns.barplot(x="fuente", y="ingresos", data=df)

# Creando un punto en el momento de más pedos
# plt.plot("01-13", 23, "o")

total_ingresos = df["ingresos"].sum()

# Mostranto el total de ingresos
print(f"Total ingresos: ${total_ingresos}")

# Mostrando el gráfico
plt.show()
