from mypackage.teves import fake_profile
from mypackage.bataller import generate_random_integers

fake_profile()

def display_statistics(count, low, high):
    """
    Display a set of random integers and their
    statistical values: mean, median, and standard deviation.
    """
    numbers, mean, median, stddev = generate_random_integers(count, low, high)

    print(f"Generated Numbers: {numbers}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {stddev}")

display_statistics(10, 1, 100)