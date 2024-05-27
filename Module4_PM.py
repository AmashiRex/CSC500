# Name: J. Lewis

class ItemToPurchase:
    """
    Initializes an ItemToPurchase object with the following attributes:
    Args:
        item_name (str): The name of a shopping cart item
        item_price (float): The price of the shopping cart item
        item_quantity (int): The quantity of the shopping cart item
        item_description (str): A description of the shopping cart item
    """
    def __init__(self, item_name="None", item_price=0, item_quantity=0, item_description=""):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def item_cost(self):
        """
        Calculates the total cost of the shopping cart item
        :return: The product of the item cost with the quantity of items
        """
        return self.item_price * self.item_quantity

    def item_subtotal(self):
        """
       Produces a subtotal line for the item
       :return: A string representing the item's name, the desired quantity, to price per item, and the total item cost.
       """
        return f'{self.item_name} x{self.item_quantity} @ ${self.item_price:.2f} = ${self.item_cost():.2f}'

    def __add__(self, other):
        """
        Adds together the costs of shopping cart items
        :param other: A second shopping cart item instance
        :return: A float representing the addition of two shopping cart items
        """
        return self.item_cost() + other.item_cost()


if __name__ == '__main__':
    item_1 = input('Please enter an item name, that item\'s price ($), and the quantity (format - "Soda,2,6"): ')
    item_2 = input('Please enter another item name, that item\'s price ($), and the quantity (format - "Soda,2,6"): ')

    name, price, quantity = item_1.split(",")
    item_1 = ItemToPurchase(name, float(price), int(quantity))

    name, price, quantity = item_2.split(",")
    item_2 = ItemToPurchase(name, float(price), int(quantity))

    print(f'\nTOTAL COST\n'
          f'{item_1.item_subtotal()}\n'
          f'{item_2.item_subtotal()}\n'
          f'Total: ${(item_1 + item_2):.2f}')
