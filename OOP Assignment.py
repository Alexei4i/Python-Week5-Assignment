# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def turn_on(self):
        return f"{self.brand} {self.model} is now ON."
    
    def turn_off(self):
        return f"{self.brand} {self.model} is now OFF."


# Inherited class
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # call parent constructor
        self.os = os
        self.storage = storage
    
    def take_photo(self):
        return f"{self.brand} {self.model} takes a photo 📸."
    
    def install_app(self, app_name):
        return f"{app_name} has been installed on {self.brand} {self.model}."
    
    # Polymorphism (method overriding)
    def turn_on(self):
        return f"{self.brand} {self.model} running {self.os} is booting up... 🔋"


# Another child class
class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size
    
    def draw_sketch(self):
        return f"{self.brand} {self.model} with {self.screen_size}\" screen is great for sketching 🎨."


# Create objects
phone1 = Smartphone("Apple", "iPhone 15", "iOS", "256GB")
phone2 = Smartphone("Samsung", "Galaxy S24", "Android", "512GB")
tablet1 = Tablet("Microsoft", "Surface Pro 9", 13)

# Test methods
print(phone1.turn_on())       # Polymorphism in action
print(phone1.take_photo())    
print(phone2.install_app("WhatsApp"))
print(tablet1.draw_sketch())
print(tablet1.turn_off())     # Inherited method
