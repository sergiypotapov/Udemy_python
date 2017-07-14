
class Programm():
    def __init__(self, *args, **kwargs):
        self.lang = "Ukr"
        self.items = 128

p1 = Programm()
print(p1.items)
p1.items = 222

print(p1.items)
