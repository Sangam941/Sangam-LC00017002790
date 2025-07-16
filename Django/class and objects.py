class Animal():
    def move(self):
        print("Animal function involved")

class Dog(Animal):
    def speak(self):
        super().move()
        print("Dog class fucntion involved")

d = Dog()
d.speak()
# print(d.speak())