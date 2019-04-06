import seaborn as sns

a = np.random.poisson(10, 10000)

sns.distplot (a,label = "Распределение Пуассона")
#sns.distplot (a,label = "uniform" )
plt.legend ()
plt.show ()
