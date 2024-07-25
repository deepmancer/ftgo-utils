import addict

class Dict(addict.Dict):
    UNKNOWN_ERROR = "UNKNOWN_ERROR"
    
    def __getattr__(self, name):
        return self.get(name, self.UNKNOWN_ERROR)
    
    def __getitem__(self, key):
        return self.get(key, self.UNKNOWN_ERROR)
    
    def get(self, key, default=UNKNOWN_ERROR):
        return super().get(key, default)
