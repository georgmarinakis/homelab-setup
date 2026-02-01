class Dog:
    animal = "dog"

    def __init__(self, breed):    
        self.breed = breed

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
roger = Dog("Tsopanoskylo")

print(roger.animal)

roger.setColor("red")
color = roger.getColor()
print(color)
print(roger.breed)

