# Import
from random import randint as rnd


# Function to count items in array
def count_number(pin, number):
    # Declare variables
    count = 0

    # Loop to check every pin number
    for n in pin:
        # Conditional to compare number
        if number == n:
            count += 1

    # Return
    return count


# Function to create PIN
def pin_generator(pin_length):
    # Define variables
    limit = pin_length / 10
    pin = []

    # Loop to create PIN
    while len(pin) < pin_length:
        # Create random number
        random_number = rnd(0, 9)

        # Conditional to insert random numbers
        if len(pin) == 0:
            # Insert first random number
            pin.append(random_number)

        elif pin_length <= 10:
            # Conditional to avoid repetitive numbers
            if random_number not in pin:
                # Insert random number
                pin.append(random_number)

        elif pin_length > 10:
            # Conditional to avoid sequential numbers
            if (
                pin[len(pin) - 1] != random_number
                and pin[len(pin) - 1] < random_number - 1
                and count_number(pin, random_number) <= limit
            ):
                # Insert random number
                pin.append(random_number)

            elif (
                pin[len(pin) - 1] != random_number
                and pin[len(pin) - 1] > random_number + 1
                and count_number(pin, random_number) <= limit
            ):
                # Insert random number
                pin.append(random_number)

    # Return
    return pin
