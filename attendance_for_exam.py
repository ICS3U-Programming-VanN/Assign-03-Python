#!/usr/bin/env python3
# Created by: Van Nguyen
# Created on: October 12, 2022
# This program asks the user to input the number of classes they attended and
# the number of classes held and then displays whether or not they can write the final exam

# This function returns the percentage (of attendance, from the user)
def calculate_percentage(numerator, denominator):
    # Calculates the exact percentage (with decimals)
    decimal_of_percentage = numerator / denominator * 100

    # Rounds the percentage
    percentage = float("{:.2f}".format(decimal_of_percentage))

    # Returns the percentage
    return percentage


def main():
    # Initialize Variables to run the program again
    keep_running = True
    run_again = ""

    # Keeps running program until user ends
    while keep_running:

        # Displays Title of Program
        print("ATTENDANCE REQUIREMENT FOR EXAM CALCULATOR\n")

        # Asks user for number of classes held and the number they attended (as a string)
        num_classes_string = input("Enter the number of classes held: ")
        num_classes_attended_string = input(
            "Enter the number of classes you attended: "
        )

        # Checks for exceptions
        try:

            # Tries to cast user input into an integer
            num_classes = int(num_classes_string)
            num_classes_attended = int(num_classes_attended_string)

            # Calls calculate_percentage() function to calculate the attendance rate
            attendance_percentage = calculate_percentage(
                num_classes_attended, num_classes
            )

            # IF the user entered numbers/classes above zero
            if num_classes >= 0 and num_classes_attended >= 0:

                # IF the user inputted that they attended more classes than the number of classes held
                if attendance_percentage > 100:
                    print("You cannot have more classes attended than classes held!")

                # IF the user can attend the exam (Attendance rate = 75% or higher)
                elif attendance_percentage >= 75:
                    print(f"\nYour attendance percentage is {attendance_percentage}%")
                    print(
                        "You may attended the exam, as your attendance is equal to or over 75%"
                    )

                # IF the user cannot attend the exam (Attendance rate = below 75%)
                else:
                    print(f"\nYour attendance percentage is {attendance_percentage}%")
                    print(
                        "You may NOT attend the exam, as your attendance is under 75%"
                    )

            # IF the user inputted negative numbers for the numbers of classes
            else:
                print("Please enter numbers above zero!")

            # Asks the user if they want to run the program again
            run_again = input(
                "Do you want to run the program again? ('y' for yes 'n' for no): "
            )

            # IF the user wants to end the program
            if run_again == "n":
                keep_running = False

        # In the event of an exception (such as letters being inputted)
        except Exception:
            print("\nPlease enter whole numbers above zero!")


if __name__ == "__main__":
    main()
