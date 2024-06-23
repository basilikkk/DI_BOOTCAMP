
import random

class Game:
    def get_user_item(self):
        items = ["rock", "paper", "scissors"]
        user_item = ""
        while user_item not in items:
            user_item = input("Select an item (rock, paper, scissors): ").lower()
            if user_item not in items:
                print("Invalid choice. Please select again.")
        return user_item

    def get_computer_item(self):
        items = ["rock", "paper", "scissors"]
        computer_item = random.choice(items)
        return computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "paper" and computer_item == "rock") or \
             (user_item == "scissors" and computer_item == "paper"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You selected {user_item}. The computer selected {computer_item}. You {result}.")
        return result
