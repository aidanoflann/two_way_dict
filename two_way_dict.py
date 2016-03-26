class Mapping:

    def __init__(self, input_dict=None):
        if input_dict:
            self.rdict = dict(zip(input_dict.values(), input_dict.keys()))
            self.dict = input_dict
        else:
            self.dict = {}
            self.rdict = {}

    def set(self, key, value):
        if key not in self.dict.keys() and value not in self.rdict.keys():
            self.dict[key] = value
            self.rdict[value] = key
        elif key not in self.dict.keys() and value in self.rdict.keys():
            self.dict.pop(self.rdict[value])
            self.dict[key] = value
            self.rdict[value] = key
        elif key in self.dict.keys() and value not in self.rdict.keys():
            self.rdict.pop(self.dict[key])
            self.dict[key] = value
            self.rdict[value] = key
        else:
            raise ValueError("Key and value both exist.")

    def remove_by_key(self, key):
        del self.rdict[self.dict.pop(key)]

    def remove_by_value(self, value):
        del self.dict[self.rdict.pop(value)]

    def get_by_key(self, key):
        return self.dict[key]

    def get_by_value(self, value):
        return self.rdict[value]

    def count(self):
        return len(self.rdict)
