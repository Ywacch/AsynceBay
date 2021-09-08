class Config:
    """
    class containing a dictionary of request parameters such as request header information
    """
    def __init__(self, config_dict=None):
        self.values = dict()
        if config_dict:
            for key, value in config_dict.items():
                self.set(key, value)

    def set(self, key, val):
        self.values.update({key: val})

    def get(self, key):
        return self.values.get(key)

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return self.__str__()

