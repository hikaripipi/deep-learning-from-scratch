# coding: utf-8
class dog:
    def __init__(self, namae):
        self.namae = namae 
        print("Initilized!")

    def bark(self):
        print(self.namae + " wanwan")

m = dog("Hi-Chan")
m.bark()