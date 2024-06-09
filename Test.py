class Cookies:
    def __init__(self, batches=1):
        self.batches = batches
        self.cup_flour = 3 * batches
        self.cup_white_sugar = 1 * batches
        self.cup_brown_sugar = 1 * batches
        self.cup_butter = 1 * batches
        self.egg = 2 * batches
        self.tsp_vanilla = 2 * batches
        self.tsp_baking_soda = 1 * batches
        self.tsp_salt = 0.5 * batches
        self.cup_choc_chips = 2 * batches
        self.cup_walnuts = 1 * batches

    def nut_allergy(self):
        # Adds an extra cup of chocolate chips per batch, and removes all walnuts
        self.cup_choc_chips += self.batches
        self.cup_walnuts = 0

    def __str__(self):
        # This, if fully completed, might print out ingredients and instructions
        if self.cup_walnuts:
            return (f"This recipe creates {self.batches} batches of cookies with nuts, which will require "
                    f"{self.cup_choc_chips} cups of chocolate chips and...")
        else:
            return (f"This recipe creates {self.batches} batches of cookies without nuts, which will require "
                    f"{self.cup_choc_chips} cups of chocolate chips and...")


my_batch = Cookies(2)
print(my_batch)
my_batch.nut_allergy()
print(my_batch)
