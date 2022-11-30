import pandas as pd
from dataclasses import dataclass



class OperatorsBase:
    data: pd.core.frame.DataFrame  # type: ignore
    def __init__(self, df):
        self.data = df

    def test_meth(self):
        print('woooooooooooooooooooooooooooooooooooooork')

    def get(self, num, operators_time_predict):
        ex = self.data.iloc[num, :]
        ex['v'] = operators_time_predict.loc[num,:]
        return ex


class Operator:
    id: int
    h_lvl: float
    psi: int
    v: list

    def __init__(self, id, h_lvl, psi, v) -> None:
        self.id = id
        self.h_lvl = h_lvl
        self.psi = psi
        self.v = v

@dataclass
class CustomersBase:
    data: pd.core.frame.DataFrame  # type: ignore
    def __init__(self, df):
        self.data = df

    def get(self, num, customer_time_to_wait):
        cust = self.data.iloc[num, :]
        if pd.to_datetime(self.data.iloc[1, :]['call_start_time'], format='%X') <= pd.to_datetime('12:00:00', format='%X'): day_part = 'morning'
        elif (pd.to_datetime(self.data.iloc[1, :]['call_start_time'], format='h:mm:ss') >  pd.to_datetime('12:00:00', format='h:mm:ss')) & (pd.to_datetime(self.data.iloc[1, :]['call_start_time'], format='h:mm:ss') <=  pd.to_datetime('17:00:00', format='h:mm:ss')) : day_part = 'lanch'
        elif pd.to_datetime(self.data.iloc[1, :]['call_start_time'], format='h:mm:ss') > pd.to_datetime('17:00:00', format='h:mm:ss'): day_part = 'evening'
        cust['ready_time_to_wait'] = customer_time_to_wait.loc[day_part, cust['task_type']]
        return cust

class Customer:
    id: int
    psi: int
    def __init__(self, id, h_lvl, psi, v) -> None:
        self.id = id
        self.h_lvl = h_lvl
        self.psi = psi
        self.v = v

print('ALL MODULES ARE IMPORTED')

def Get_g:(Lam, now_time, Oper, Cust):
    k = 

