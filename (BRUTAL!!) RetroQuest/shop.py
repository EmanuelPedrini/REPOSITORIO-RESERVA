from Items import *

class Shop:

    def __init__(self):

        self.items = {
            1: potion,
            2: mana_potion,
            3: old_ring,
            4: mana_pendant,
            5: lucky_charm
        }

    def open_shop(self, player):

        while True:

            print("\nSHOP")
            print(f"cents: {player.cents}\n")

            for number, item in self.items.items():
                print(f"{number} - {item.name} | {item.price} cents")

            print("0 - Exit")

            choice = input("\nChoose an item: ")

            if choice == "0":
                print("You left the shop.")
                break

            if not choice.isdigit():
                print("Invalid choice.")
                continue

            choice = int(choice)

            if choice not in self.items:
                print("Item not found.")
                continue

            selected_item = self.items[choice]

            if player.cents >= selected_item.price:

                player.cents -= selected_item.price
                player.inventory.append(selected_item)

                print(f"\nYou bought {selected_item.name}!")

            else:
                print("Not enough cents.")