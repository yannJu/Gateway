class Bridge:
    def __init__(self):
        self.counter = 0
        self.name = "O"
        self.address = "X"
        
    def across(self, name, address):
        self.counter += 1
        self.name = name
        self.address = address
        self.check()
        
    def toString(self):
        return "이름 : {}, 출신 : {},  도전횟수 : {}".format(self.name, self.address, self.counter)
    
    def check(self):
        if self.name[0] != self.address[0]: print("문제 발생 !!!" + self.toString())