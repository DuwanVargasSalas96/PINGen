# -*- coding: UTF-8 -*-

# Import
from pin_generator import pin_generator
from utils import clean_terminal


# Main function
def main():
    # Loop
    while True:
        # Clean terminal
        clean_terminal()

        # Print menu
        print("PINGen\n")
        print("1. Generar PIN.")
        print("2. Salir.")

        # Caught option
        option = str(input("Su opción es: "))

        if option == "1":
            # Clean terminal
            clean_terminal()

            # Print
            print("PINGen\n")
            print("Indique la longitud del PIN.")

            # Caught pin length
            pin_length = int(input("Su opción es: "))

            # Conditional to check pin length
            if pin_length >= 4:
                # Generate pin
                pin = pin_generator(pin_length)

                # Clean terminal
                clean_terminal()

                # Print
                print("PINGen\n")
                print(f"Su nuevo PIN es: {pin}\n")
            else:
                # Clean terminal
                clean_terminal()

                # Print
                print("PINGen\n")
                print("La longitud del PIN debe ser mayor a igual a 4.\n")

            # KeyGen
            input("Presione la tecla Enter regresar al menú.")

            # Return
            main()
        elif option == "2":
            # Clean terminal
            clean_terminal()

            # Exit
            quit()
        else:
            # Print
            input("Opción incorrecta! Intente nuevamente.")


# Execute main function
main()
