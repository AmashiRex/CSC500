# Name: J. Lewis

from Module4_PM import ItemToPurchase as NewItem


class ShoppingCart:
    """
    Initializes a ShoppingCart object with the following attributes:
    Args:
        customer_name (str): The name of the customer to whom the cart/order belongs
        current_date (str): The date the order is created
        cart_items (list): A list of items to purchase
    """
    def __init__(self, customer_name="None", current_date="January 1, 2020", cart_items=None):
        if cart_items is None:
            cart_items = []
        self.cart_items = cart_items
        self.customer_name = customer_name
        self.current_date = current_date
        self.greeting()

    def greeting(self):
        """
        Prints a message on successful creation of a new shopping cart object.
        """
        print(f"Customer Name: {self.customer_name}\n Today's Date: {self.current_date}")

    def add_item(self):
        """
        If the item is already in the cart (same name and price), the quantity is altered
        Otherwise, the item is new and the user is prompted to add a description
        The item is then added to the cart
        """
        item_input = input("Please enter an item name, that item's price ($), and the quantity (format - 'Soda,2,6'): ")
        item_name, price, quantity = item_input.split(",")
        item_to_add = NewItem(item_name, float(price), int(quantity))

        for item in self.cart_items:
            if item.item_name == name and item.item_price == price:
                self.modify_item(item, quantity)
        else:
            item_description = input("Please enter a short description for the item: ")
            item_to_add.item_description = item_description
            self.cart_items.append(item_to_add)

    def remove_item(self):
        """
        Checks to see if the item is in the cart
        If the item is in the cart, the user is given the option of deleting the item
        The user can also reduce the quantity of the item instead
        """
        modify = True
        item_input = input("Please enter an item name to remove: ")
        for item in self.cart_items:
            if item.item_name == item_input:
                while modify:
                    confirmation = input("Would you like to remove the following item, or reduce it's quantity?\n"
                                         f"Name: {item.item_name}\n"
                                         f"Price: {item.item_price}\n"
                                         f"Quantity: {item.item_quantity}\n"
                                         "Enter your Response: y/n/r\n").lower()
                    match confirmation:
                        case "y":
                            self.cart_items.remove(item)
                            modify = False
                        case "n":
                            modify = False
                        case "r":
                            num_to_remove = int(input("Enter the number of items would you like to remove: "))
                            self.modify_item(item, -num_to_remove)
                            modify = False
                        case _:
                            print("Your selection was invalid, please try again.")

    def modify_item(self, item=None, change=0):
        """
        If given an item/quantity, change the quantity of the item
        Else, search for an item in the cart by name. If the item is found, display the item
        Prompt the user to modify the quantity of the displayed item
        :param item: A shopping cart item
        :param change: The quantity of the item to modify
        """
        modified_item = item
        change_amount = change

        if not modified_item:
            modify = True
            item_input = input("Please enter an item name to modify: ")
            for item in self.cart_items:
                if item.item_name == item_input:
                    while modify:
                        confirmation = input("Would you like to modify the following item?\n"
                                             f"Name: {item.item_name}\n"
                                             f"Price: {item.item_price}\n"
                                             f"Quantity: {item.item_quantity}\n"
                                             "Enter your Response: y/n\n").lower()
                        match confirmation:
                            case "y":
                                modified_item = item
                                change_amount = int(input("Enter the number of items would you like to add: "))
                                modify = False
                            case "n":
                                modify = False
                            case _:
                                print("Your selection was invalid, please try again.")

        modified_item.item_quantity += change_amount
        print(f"You now have {modified_item.item_quantity} {modified_item.item_name} in the cart.")

    def get_num_items(self):
        """
        Calculates the number of items in the shopping cart
        :return: An integer representing the number of items in the cart
        """
        return len(self.cart_items)

    def get_cart_cost(self):
        """
        Calculates the total cost of the items stored in the cart
        :return:  An integer representing the total cost of the items in the cart
        """
        cost_sum = 0
        for item in self.cart_items:
            cost_sum += item.item_cost()  # item_cost() is imported from the module 4 assignment
        return cost_sum

    def print_total(self):
        """
        Creates a display representing cart owner, date, item names, quantities, costs, and a subtotal
        """
        if not self.cart_items:
            print("There are no items in this shopping cart.")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\nNumber of Items: {self.get_num_items()}")
            for item in self.cart_items:
                print(item.item_subtotal())  # item_subtotal() is imported from the module 4 assignment
            print(f"Subtotal: ${self.get_cart_cost()}, plus tax.")

    def print_descriptions(self):
        """
        Creates a display providing a detailed description of the items stored in the cart
        """
        if not self.cart_items:
            print("There are no items in this shopping cart.")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\nNumber of Items: {self.get_num_items()}\nItem Descriptions")
            for item in self.cart_items:
                print(f"{item.item_name}: {item.item_description}.")


def print_menu(shopping_cart):
    """
    Creates a text-based menu for modifying and viewing a customer shopping order
    :param shopping_cart: A ShoppingCart object, representing a customer's order details
    """
    selection = ""
    print(f"Hello {shopping_cart.customer_name}, please select a valid entry from the menu:\n")

    while selection != "q":
        print("""
        MENU:\n
        a - Add item to cart\n
        r - Remove item from cart\n
        m - Modify item\n
        i - Output item description\n
        o - Output shopping cart\n
        q - Quit\n
        """)

        selection = input("Enter your selection: ").lower()

        match selection:
            case "q":
                break
            case "a":
                shopping_cart.add_item()
            case "r":
                cart.remove_item()
            case "m":
                shopping_cart.modify_item()
            case "i":
                cart.print_descriptions()
            case "o":
                shopping_cart.print_total()
            case _:
                print("Your selection was invalid, please try again.")

    print("\nGoodbye")


if __name__ == '__main__':

    name = input("Please enter your name: ")
    date = input("Please enter today's date (ex: January 1, 2020): ")
    cart = ShoppingCart(name, date)

    print_menu(cart)
