class Phone: # base class / parent class
    def _init_(self, brand,model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price= max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}....."

class Smartphone(Phone):#derived / child class
    def _init_(self, brand,model_name, price, ram, internal_memory, rear_camera):
        #two ways
            # phone._init_(self,brand,model_name, price) #uncommon way
            super()._init_(brand,model_name, price)
            self.ram = ram
            self.internal_memory = internal_memory
            self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}....."

phone = Phone('nokia', '1100', 100)
smartphone = Smartphone('oneplus', '5', 30000, '6 GB', '20 MP')
print(phone.full_name())
print(smartphone.full_name())