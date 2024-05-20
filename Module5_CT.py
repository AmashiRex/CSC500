# Name: J. Lewis

def rainfall_calculation(monthly_rainfall_list):
    """
    Calculates the total rainfall, average monthly rainfall, and the length of data collection.
    :param monthly_rainfall_list: Rainfall values, represented as a list of floats.
    :return: The length of data collection, the total rainfall, and the average monthly rainfall.
    """
    time_span = len(monthly_rainfall_list)
    total_rainfall = sum(monthly_rainfall_list)
    average_rainfall = total_rainfall / time_span
    return time_span, total_rainfall, average_rainfall


def calculate_rewards(total_book_purchases):
    """
    Calculates the monthly book purchase reward for a bookstore.
    :param total_book_purchases: The (integer) number of books purchased during a single month.
    :return: The total number of rewards points (integer) earned for that month.
    """
    if total_book_purchases >= 8:
        return 60
    elif total_book_purchases >= 6:
        return 30
    elif total_book_purchases >= 4:
        return 15
    elif total_book_purchases >= 2:
        return 5
    else:
        return 0


if __name__ == '__main__':
    print("Part 1:")
    num_months = int(input('How many years of rainfall data do you have? ')) * 12
    rainfall = [float(input(f'How much rain (inches) fell in month {month + 1}? ')) for month in range(num_months)]
    total_months, total_precip, average_precip = rainfall_calculation(rainfall)
    print(f"Over {total_months} months, {total_precip} inches of rain fell, an average of {average_precip:.1f} inches "
          f"per month.")

    print("\nPart 2:")
    book_purchases = int(input('How many books did you purchase from the bookstore this month? '))
    point_total = calculate_rewards(book_purchases)
    print(f"You earned {point_total} points this month for purchasing {book_purchases} books!")
