class User:
    def __init__(self, loginName, passwd, enable = True) -> None:
        self.__loginName = loginName
        self.__password = passwd
        self.__enable = enable
    
    def getloginName(self):
        return self.__loginName
    
    def getPassword(self):
        return self.__password
    
    def getEnable(self):
        return self.__enable
    
    def setloginName(self, loginName) -> None:
        self.__loginName = loginName
    
    def setPassword(self, passwd) -> None:
        self.__password = passwd
    
    def setEnable(self, enable) -> None:
        self.__enable = enable

    def __repr__(self) -> str:
        return f"Login Name: {self.getloginName()}, Password: {self.getPassword()}, Enable: {self.getEnable()}"

class Player(User):
    def __init__(self, loginName, passwd, level, enable=True) -> None:
        super().__init__(loginName, passwd, enable=enable)
        self.__level = level
    
    def getLevel(self):
        return self.__level
    
    def setLevel(self, level) -> None:
        self.__level = level
    
    def __repr__(self) -> str:
        return super().__repr__() + f" Level: {self.getLevel()}"
    

if __name__ == '__main__':
    a = User("Sky Tsai", "hwjfgwe")
    print(a)
    b = Player("Leo", "dfhjwegv", "C")
    print(b)