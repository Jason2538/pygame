class Hello():
    def __init__(self,name):
        self.name = name
    def greeting(self):
        print(self.name + ": 안녕 아로야")
    def goodbye(self):
        print(self.name + ": 잘가 아로야")


a = Hello('김정은')
a.greeting()
a.goodbye()
b= Hello('윤석열')
b.greeting()
b.goodbye()
c=Hello('이재명')
c.greeting()
c.goodbye()