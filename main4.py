name = input("ice cream, carrots, cheese shulardan bitasini kirkizing: ")
class Person:
    def __init__(self, name, love, no_love, yes_love):
        self.name = name
        self.love = love
        self.no_love = no_love
        self.love2 = yes_love
    def good_food(self):
        return f"{self.name} eats the {self.love} and loves it!"
    def bad_food(self):
        return f"Sam eats the {self.name}"
    def bad_boy(self):
        return f"{self.name} eats the {self.no_love} and hates it!"
    def math(self):
        if name == self.love:
            print(obj.good_food())
        if name == self.no_love():
            print(obj.no_love())
        if name == self.love2():
            print(obj.love2())
obj = Person("Sam", "ice cream", "carrots", "cheese")
obj.math()

