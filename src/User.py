import pickle
import pandas as pd
import os
from datetime import datetime

class User:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.values = []
        self.maxs = []
        self.flags = []
    

    def save(self):
        
        try:
            users = User.load_all()
            #print(f'users: {users}')
            users.append(self)

            with open('user.pickle', 'wb') as f:
                pickle.dump(users, f)

        except:
            with open('user.pickle', 'wb') as f:
                pickle.dump([self], f)
        

        
    
    def save_excel(self):
        
        ##save main data to excel
        df = pd.DataFrame({'Nombre': [self.name], 'Descripcion': [self.description], 'Maximos': [self.maxs], 'Fecha': [datetime.now()]})

        if not os.path.isfile('resumen.xlsx'):    
            df.to_excel('resumen.xlsx', index=False)
        
        else:
            reader = pd.read_excel('resumen.xlsx')
            writer = pd.ExcelWriter('resumen.xlsx', engine='openpyxl', mode='a', if_sheet_exists="overlay")
            df.to_excel(writer, index=False, header=False, startrow=len(reader)+1)
            writer.close()

    @staticmethod
    def load_all():

        with open('user.pickle', 'rb') as f:

            load_users = pickle.load(f)


        return load_users