# Name: Joshua Lewis
def addition(summand_a, summand_b):
    """
    addition adds two numbers together;
    non-numeric values are not checked for

    :param summand_a: A number to be added
    :param summand_b: A number to be added
    :return: The sum of two numbers
    """
    return summand_a + summand_b


def subtraction(minuend, subtrahend):
    """
    subtraction subtracts two numbers together;
    non-numeric values are not checked for

    :param minuend: A number to be subtracted
    :param subtrahend: A number to be subtracted
    :return: The difference of two numbers
    """
    return minuend - subtrahend


def multiplication(multiplier, multiplicand):
    """
    multiplication multiplies two numbers together;
    non-numeric values are not checked for

    :param multiplier: A number to be multiplied
    :param multiplicand: A number to be multiplied
    :return: The product of two numbers
    """
    return multiplier * multiplicand


def division(dividend, divisor):
    """
    division divides two numbers together;
    non-numeric values are not checked for;
    a zero divisor is not checked for

    :param dividend: A number to be divided - numerator
    :param divisor:  A number to be divided - denominator
    :return: The quotient and remainder of two numbers
    """
    return dividend / divisor


if __name__ == '__main__':
    term_a = int(input('Enter a numeric term: '))
    term_b = int(input('Enter a nonzero numeric term: '))
    print(addition(term_a, term_b))
    print(subtraction(term_a, term_b))
    print(multiplication(term_a, term_b))
    print(division(term_a, term_b))
