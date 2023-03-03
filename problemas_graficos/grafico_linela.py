import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\pedos.csv")

# Creando el gráfico
sns.lineplot(x="fecha", y="pedos", data=df)

# Creando un punto en el momento de más pedos
plt.plot("01-13", 23, "o")

# Mostrando el gráfico
plt.show()
