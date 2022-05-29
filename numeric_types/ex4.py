def hex_output():
    n_hex = input("Enter a hex number to convert to decimal: ")
    return sum(int(d, 16)*16**p for p, d in enumerate(reversed(n_hex)))


# Beyond the exercise
def hex_output_robust():
    n_hex = input("Enter a hex number to convert to decimal: ")
    decimal = 0
    for power, digit in enumerate(reversed(n_hex)):
        if 47 < (unicode := ord(digit.upper())) < 58:
            # Code point is from "0" up to, and including, "9"
            decimal += (unicode - 48) * 16**power
        elif 64 < unicode < 71:
            # Code point is from "A" up to, and including, "F"
            decimal += (unicode - 55) * 16**power
        else:
            # Code point does not match any hex character
            return "Not a valid hex number!"
    return decimal


def name_triangle():
    name = input("What is your name? ")
    for i in range(len(name)):
        print(name[:i+1])


if __name__ == "__main__":
    print(hex_output())
    print("\nBeyond the exercise\n")
    print(hex_output_robust())
    name_triangle()
