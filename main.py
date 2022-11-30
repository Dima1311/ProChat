import pandas as pd
from importlib import reload
import MyClasses
reload(MyClasses)


##Подгружаем операторов и таблицу предсказания времени
operator_base = pd.read_csv(r'C:\Users\dmivadivanov\Documents\ProChat\Data\Operators.csv', sep = ';')
operators_time_predict = pd.read_csv(r'C:\Users\dmivadivanov\Documents\ProChat\Data\Operators_time_predict.csv', sep = ';', index_col='id', header = 0)


#Загоняем операторов в класс
#и проверяем, что мы умеем доставать одного конкретного
#оператора и делать для него предикт по времени
Operator_base = OperatorsBase(operator_base)
Operator_base.get(2, operators_time_predict)['v']['w4']
Operator_base

#Теперь загоняем клиентов и готовность к ожиданию
customer_base = pd.read_csv(r'C:\Users\dmivadivanov\Documents\ProChat\Data\Customers.csv', sep = ';')
customer_time_to_wait = pd.read_csv(r'C:\Users\dmivadivanov\Documents\ProChat\Data\Customer_time_to_wait.csv', sep = ';', index_col = 'day_part', header = 0)

#Считываем одного конкретного клиента
#И умеем делать для него предрасчёт по времени ожидания
Customer_base = CustomersBase(customer_base)
Customer_base.get(2, customer_time_to_wait)

psi_matrix = pd.read_csv(r'C:\Users\dmivadivanov\Documents\ProChat\Data\Psi_Matrix.csv', sep = ';', index_col = 'psi')

type(psi_matrix.iloc[1,2])

Lam = [1,1,1]

#pd.to_datetime('9:00:00', format='h:mm:ss', errors='ignore') = pd.to_datetime('10:00:00', format='h:mm:ss', errors='ignore') 


