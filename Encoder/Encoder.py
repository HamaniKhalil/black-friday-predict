# -*- coding: UTF-8 -*-
#!/anaconda3/bin/python

# -----------------------------------------------------------------------------------------------------------------------
# |                                                 Encoder Class                                                       |
# -----------------------------------------------------------------------------------------------------------------------

class Encoder:
    def __init__(self, count=1):
        self.data_to_index = {}
        self.index_to_data = {}
        self.count = count

    def set_data_to_index(self, data_to_index):
        self.data_to_index = data_to_index
        self.index_to_data = {v: k for k, v in list(data_to_index.items())}
        self.count = max(list(self.data_to_index.values()))

    def encode_data(self, new_data): # encode la nouvelle donnée si elle n'est pas déjà encodé, sinon retourn son code
        if isinstance(new_data, str):
            new_data = [new_data]
        
        res = []

        for data in new_data:
            if data not in self.data_to_index:
                self.data_to_index[data] = self.count
                self.index_to_data[self.count] = data
                self.count += 1
            res.append(self.data_to_index[data])
        return res

    def set_code(self, data, code): # assigne un code a la donnée "data"
        if data not in self.data_to_index:
            self.index_to_data[code] = data
            self.data_to_index[data] = code
            return code
        else:
            return self.data_to_index[data]

    def get_code(self, data): # donne le code correspondant a data sinon 0 si n exsite pas
        for i in self.data_to_index:  
            if i == data:
                return self.data_to_index[i]
        return 0


    def get_data(self, code): # donne la donnée correspondante a code sinon 0
        return self.index_to_data.get(code, 0)