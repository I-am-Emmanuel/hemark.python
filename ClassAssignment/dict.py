class Mydics(dict):

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Your key can only be string")
        super().__setitem__(key, value)


d = Mydics()
d[6] = 4
print(d)
