from ex2 import avg
from decimal import Decimal


def run_timing():
    runs = []
    while (choice := input("How long did your 10km run take? ")):
        try:
            runs.append(float(choice))
        except ValueError:
            print("Not a number, try again!")
    if not runs:
        return "No runs recorded!"
    average_run_time = avg(runs)
    return f"Average of {average_run_time:.1f}, over {len(runs)} runs."


# Beyond the exercise
def before_after(decimal_number, before, after):
    float_string = str(decimal_number)
    before_decimal, after_decimal = float_string.split(".")
    return f"{before_decimal[-before:]}.{after_decimal[:after]}"


def decimal_sum(decimal_1, decimal_2):
    return sum([Decimal(decimal_1), Decimal(decimal_2)])


if __name__ == "__main__":
    print(run_timing())
    print("\nBeyond the exercise\n")
    print(f"Before, after: 1234.56789, 2, 3: {before_after(1234.56789, 2, 3)}")
    print(f"0.1 + 0.2 = {decimal_sum('0.1', '0.2')}")
