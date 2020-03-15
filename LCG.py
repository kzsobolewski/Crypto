class LCG:

    def __init__(self, seed, mod, multiplier, addends):
        self.__seed = seed
        self.__multiplier = multiplier
        self.__addends = addends
        self.__mod = mod

    def run(self):
        self.__seed = (self.__multiplier * self.__seed + self.__addends) % self.__mod
        return self.__seed
