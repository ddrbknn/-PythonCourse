import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

a = np.random.pareto(500, 1000)

sns.distplot (a,label = "Распределение Паретто", rug=True,  color="y")
#sns.distplot (a,label = "uniform" )

plt.legend ()
plt.show ()
