# Name: J. Lewis

# import datetime
def meal_calculator(meal_price, sales_tax, gratuity):
    """
    Calculates the full price of a meal, including tax and tip.
    :param meal_price: The price of the meal.
    :param sales_tax: The sales tax, as a percentage.
    :param gratuity: The tip, as a percentage.
    :return: The full price of a meal, including tax and tip.
    """
    return meal_price * (1.0 + sales_tax) * (1.0 + gratuity)


def naive_alarm(time, delay):
    """
    Calculates the new time, after a delay, in a 24-hour format.
    :param time: An integer representing the current time
    :param delay: The amount of time between the present and the alarm.
    :return: Returns the new time, after a delay, in a 24-hour format and the number of elapsed days.
    """
    return (time + delay) % 24, delay // 24


if __name__ == '__main__':
    raw_meal_price = float(input('Enter meal price: $'))
    local_sales_tax = float(input('Enter sales tax, as a fractional percentage: '))
    desired_gratuity = float(input('Enter tip, as a fractional percentage: '))

    total_meal_cost = meal_calculator(raw_meal_price, local_sales_tax, desired_gratuity)
    print(f"The total cost of your meal is ${total_meal_cost:.2f}. Please come again!\n")

    # current_time = datetime.datetime.now()
    current_hour = int(input('Enter the current hour (24-hour time), as an integer: '))
    desired_delay = int(input('Enter the duration of the alarm in hours, as an integer: '))

    alarm_hour, elapsed_days = naive_alarm(current_hour, desired_delay)
    print(f"The alarm will go off at {alarm_hour:02d}:00 hours, in {elapsed_days} days.")
