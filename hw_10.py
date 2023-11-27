"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид.
Сможете ли вы это сделать без get_dummies?
"""

import pandas as pd
import random


def one_hot(data, col):
    data_set = set(data[col])
    for el in data_set:
        data[el] = 0
        data.loc[data[col] == el, el] = 1
    data.pop(col)
    return data


lst = ["robot"] * 10
lst += ["human"] * 10
random.shuffle(lst)
data = pd.DataFrame({"whoAmI": lst})
data.head()

# Обработка методом get_dummies, для сравнения
print(pd.get_dummies(data["whoAmI"]))
print()

# Решение задачи методом реализующим one hot вид
data = one_hot(data, "whoAmI")

print(data)

# Порядок столбцов в методах one_hot и get_dummies может отличаться
# Метод one_hot может выводить логические значения True и False, как метод get_dummies,
# при подстановке их в 15 и 14 строках соответственно, вместо числовых значений 1 и 0.
