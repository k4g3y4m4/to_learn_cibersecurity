import pandas as pd
import numpy as np
import sys

#read value of command line argument
examn = sys.argv[1]

#read csv file
df = pd.read_csv('plan.csv')
df["Dificultad"] = np.where(df["Dificultad"] == "Fácil", 1, np.where(df["Dificultad"] == "Media", 2, 3))
df = df.loc[df['Like'].str.contains(str(examn))][["Máquina","Dificultad","Técnicas Vistas"]].sort_values(by=['Dificultad'], ascending=True)
#output a csv file with the results
df.to_csv('tolearn_%s.csv' % examn, index=False)
