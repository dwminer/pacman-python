class mirror (): 
    def __init__(self, obj):
        self.__dict__['obj'] = obj 

    def recursive_mirror(self, ret):
        if isinstance(ret, (int, str, bool, float, tuple)):
            return ret
        elif isinstance(ret, (dict, list)):
            return [mirror(x) if not isinstance(x, (int, str, bool, float, tuple)) else x for x in ret]
        else:
            return mirror(ret)
        
    def __getattr__(self, name):
        return self.recursive_mirror(getattr(self.__dict__['obj'], name))
    
    def __getitem__(self, name):
        return self.recursive_mirror(self.__obj[name])
