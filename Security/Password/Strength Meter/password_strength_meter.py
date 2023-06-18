from zxcvbn import zxcvbn

class strength_meter():
    
    def __init__(self, password):
        self.password = password

    def strength_meter(self):
        result = zxcvbn(self.password)
        return result.get("score")
    
strength = strength_meter(";%9RVpkO&xCU`:K$,9D")
print(strength.strength_meter())

    