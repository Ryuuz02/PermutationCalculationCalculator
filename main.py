# Import statements
from math import factorial


# Simple function that converts a string input to a yes or no question. The response of the user then determines if it
# returns true or false
def question_true_false(question):
    answer = input(question + "? Y/N\n").lower()
    if answer == "y":
        return True
    else:
        return False


# Function that returns the value of the combination formula using both the total number of items and chosen items
def combination_calculation(total_items, chosen_items):
    return int((factorial(total_items)) / (factorial(chosen_items) * factorial(total_items - chosen_items)))


# Function that returns the value of the permutation formula using both the total number of items and chosen items
def permutation_calculation(total_items, chosen_items):
    return int((factorial(total_items)) / factorial(total_items - chosen_items))


# This one is interesting, I was not aware of this combination possiblity before writing this. the multichoose formula
# is used when the order does not matter and you're not removing items, it is typically written as # choose #, like 7
# choose 3
def multichoose_calculation(total_items, chosen_items):
    bars = total_items - 1
    return int((factorial(bars + chosen_items)) / (factorial(bars) * factorial(chosen_items)))


# The function that we use to figure out which function to actually use along with gathering the data to find the
# possible combinations
def choose_calculation_type():
    # We assign a baseline value for the combinations variable at 0. Theoretically this value should never be used as
    # it is later reassigned using the calculations later, but just in case it is needed.
    combinations = 0
    # Finding out if the order is relevant
    order_matters = question_true_false("Does the order matter")
    # Finding out if we are removing items from the list as we go
    removing_items = question_true_false("Are you removing items after they are chosen")
    # How many total items we are choosing from
    total_items = int(input("How many items are you picking from?\n"))
    # How many items are we choosing in total
    chosen_items = int(input("How many items are you picking?\n"))
    # This series of if statements is the different possible combinations of order mattering and removing or keeping
    # items
    if order_matters and removing_items:
        combinations = permutation_calculation(total_items, chosen_items)
    elif order_matters and not removing_items:
        combinations = total_items ** chosen_items
    elif not order_matters and removing_items:
        combinations = combination_calculation(total_items, chosen_items)
    else:
        combinations = multichoose_calculation(total_items, chosen_items)
    # prints the total possible combinations given the conditions and items
    print("There are " + str(combinations) + " total possible combinations")


choose_calculation_type()
