#Задача 44: 
#В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
#Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
#print(data)

one_hot_list = []
for i in lst:
    if i == 'robot':
        one_hot_list.append(1)
    if i == 'human':
        one_hot_list.append(0)
#print(one_hot_list)

one_hot_data = pd.DataFrame({'one_hot_list':one_hot_list})
print(one_hot_data)


