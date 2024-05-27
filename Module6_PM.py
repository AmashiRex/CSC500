# Name: J. Lewis

import Module4_PM as new_item


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

    def add_item(self):
        # Step 8 of Module 8's assignment
        pass

    def remove_item(self):
        # Step 9 of Module 8's assignment
        pass

    def modify_item(self):
        # Step 10 of Module 8's assignment
        pass

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
        return cost_sum / len(self.cart_items)

    def print_total(self):
        """
        Creates a display representing cart owner, date, item names, quantities, costs, and a subtotal
        """
        if not self.cart_items:
            print("There are no items in this shopping cart.")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\nNumber of Items: {self.get_num_items}")
            for item in self.cart_items:
                print(item.item_subtotal)  # item_subtotal() is imported from the module 4 assignment
            print(self.get_cart_cost())

    def print_descriptions(self):
        """
        Creates a display providing a detailed description of the items stored in the cart
        """
        if not self.cart_items:
            print("There are no items in this shopping cart.")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\nNumber of Items: {self.get_num_items}\nItem Descriptions")
            for item in self.cart_items:
                print(f"{item.item_name} : {item.item_description}")


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

    # This code is part of Module 8's assignment, although I feel it is required for Module 6's assignment.
    name = input("Please enter your name: ")
    date = input("Please enter today's date (ex: January 1, 2020): ")
    cart = ShoppingCart(name, date)

    print_menu(cart)
