import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\\bigotes.csv")
#Para leer archivos demasiado grandes, es mejor usar 
#red_csv_in_chunk("archivos_grandes")


# Creando el gráfico
sns.boxplot(x="categoria", y="valor", data=df)


# Mostrando el gráfico
plt.show()
