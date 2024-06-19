"""ry to recreate the class explained below:
We have a class called Door that has an attribute of is_opened declared when an instance is initiated.
We can create a class called BlockedDoor that inherits from the base class Door.
We jut override the parent class's functions of open_door() and close_door() with our own BlockedDoor version of those functions, which simply raises an Error that a blocked door cannot be opened or closed."""

class Door():
    def __init__(self, is_opened=True):
        self.is_opened=is_opened
    def open_door(self):
        self.is_opened=True
        print('door is opened')
    def close_door(self):
        self.is_opened=True
        print('door is  closed')   
class BlockedDoor(Door):
    def open_door(self):
        raise Exception("a blocked door")
    def close_door(self):
        raise Exception("a blocked door")

door1=Door()
door1.close_door()
print(door1.is_opened)