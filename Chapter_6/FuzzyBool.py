class FuzzyBool:
    
    def __init__(self, value=0.0):
        self.__value = value if 0.0 <= value <= 1.0 else 0.0
    
    def __invert__(self):
        return FuzzyBool(1.0 - self.__value)
    
    def __and__(self, other):
        return FuzzyBool(min(self.__value, other.__value))
    
    def __iand__(self, other):
        self.__value = min(self.__value, other.__value)
        return self
    
    def __repr__(self):
        return ("{0}({1})".format(self.__class__.__name__, self.__value))
    
    def __str__(self):
        return str(self.__value)
    
    def __bool__(self):
        return self.__value > 0.5
    
    def __int__(self):
        return round(self.__value)
    
    def float__(self):
        return self.__value
    
    def __lt__(self, other):
        return self.__value < other.__value
    
    def __eq__(self, other):
        return self.__value == other.__value
    
    def __hash__(self):
        return hash(id(self))
    
    def __format__(self, format_spec):
        return format(self.__value, format_spec)
    
    @staticmethod
    def conjunction(*fuzzies):
        return FuzzyBool(min([float(x) for x in fuzzies]))
    
    
    
