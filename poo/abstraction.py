"""
abstraction: 
    - Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of the object.
"""

from abc import ABC, abstractmethod # ABC: Abstract Base Class

class Payment(ABC):
    
    def __init__(self, amount):
        self.amount = amount
        
    @abstractmethod
    def pay(self, amount):
        pass
    
    @abstractmethod
    def get_payment_method(self):
        pass
    
    @abstractmethod
    def api_key(self):
        pass


class CreditCardPayment(Payment):
    
    def __init__(self, amount):
        super().__init__(amount)
        
    def get_amount(self):
        return self.amount    
    
    def pay(self, amount):
        print(f"Payment of {amount} made with credit card")
        
    def get_payment_method(self):
        return 'Credit Card'
    
    def api_key(self):
        return 'credit_card_api_key'   
    
    
payment = CreditCardPayment(100)
print(payment.get_amount())    


class CarGameVideo(ABC):
    
    def __init__(self, name):
        self.name = name
        
        
    @abstractmethod
    def play(self):
        pass
    
    
    @abstractmethod
    def stop(self):
        pass
    
    
    @abstractmethod
    def pause(self):
        pass
    
    @abstractmethod
    def set_wheel(self, wheel):
        pass
    
    @abstractmethod
    def set_gear(self, gear):
        pass
    
    @abstractmethod
    def set_speed(self, speed):
        pass
    

# decorateur: 

def check_speed(func):
    def wrapper(speed):
        if speed > 100:
            print('Speed limit exceeded')
        else:
            func(speed)
    return wrapper    

@check_speed
def set_speed(speed):
    print(f"Speed set to {speed}")
    
