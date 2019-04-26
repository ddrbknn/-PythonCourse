import time
import random
class A:
    def __init__(self, name=None, hp=None):
        self._name = name
        self._hp =  hp
        
    def _say(self, text):
        print(text)
        
    def say(self):
        self._say(f" {self._name},{self._hp}")
    
    def get_hp(self): 
        return self._hp
        
                
    def set_hp(self):
        hp_in = random.randint(0, 20)
        print("Сила атаки", hp_in)
        self._hp = self._hp - hp_in
        print(f"Остаток здоровья {self._name}", self._hp)
        if self._hp <= 0:
            print(f"Погиб {self._name}")


        
class Survivor(A):
    def __init__(self, name, hp):
        super().__init__(name, hp)
    
        
        
class Zomb(A):
    def __init__(self, name, hp):
        super().__init__(name,hp)
 
    
     
A = [
    Survivor('Выживший_1', 100),
    Zomb('Сосиска',100), 
]

y = Survivor(name = 'Выживший_1', hp = 100)
x = Survivor(name = 'Сосиска',hp = 100)

hpx = x.get_hp()
hpy = y.get_hp()


y.say()
x.say()
print('_____')

while hpx > 0 and hpy > 0:
    x.set_hp()
    hpx = x.get_hp()
    time.sleep(0.1)
    y.set_hp()
    hpy = y.get_hp()



 
