from dice import Dice

def main():
    # Create two dice objects
    die1 = Dice()
    die2 = Dice()

    # Roll both dice
    die1.roll()
    die2.roll()

    # Get the face values after rolling
    num1 = die1.getFaceValue()
    num2 = die2.getFaceValue()

    # Add the two face values together
    total = num1 + num2

    # Display the result
    print(f"Die 1 rolled: {num1}")
    print(f"Die 2 rolled: {num2}")
    print(f"Total of both dice: {total}")

# Call the main function
main()
