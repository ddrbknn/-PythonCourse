#E3
# Установка дополнительных пакетов
import sys
!{sys.executable} -m pip install matplotlib sklearn pandas requests seaborn --user

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib as mpl

# загружаем датасет
boston = datasets.load_boston()
boston_df = pd.DataFrame(boston['data'], columns=boston['feature_names'])

#добавляем столбец со стоимостью
boston_df['PRICE'] = boston.target
# смотрим, какие данные у нас есть
print ("Columns: " + " ".join (boston_df.columns))

y = boston_df['PRICE']
x = boston_df['AGE']
x2 = boston_df['INDUS']


plt.plot (sorted(x2), [x for _,x in sorted(zip(x2, y))])
plt.xlabel ("INDUS")
plt.ylabel ("PRICE")
plt.title ("Цены на жильё")
plt.show ()


plt.scatter (sorted(x), [x for _,x in sorted(zip(x, y))])
x = x.values
y = y.values
x = x.reshape(506, 1)
y = y.reshape(506, 1)
model = LinearRegression()
model.fit(x, y)
r_sq = model.score(x, y)
plt.plot(x, model.predict(x), label = u'Линейная регрессия',color = 'red')
plt.xlabel ("AGE")
plt.ylabel ("PRICE")
plt.title ("Цены на жильё")
plt.legend() 
plt.show ()
#print('Регрессия')
#print('coefficiet of determination:', r_sq)
#print('intercept:', model.intercept_)
#print('slope:', model.coef_)
