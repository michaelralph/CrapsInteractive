
from dice import *
from math import *


def craps():

    print("Welcome to interactive craps!")
    c = "Y"
    
    # bank is used to keep track of winnings

    bank = 0

    # if Y or y is typed into the program at the end, it will continue the program
    # if anything else is typed in, the program will stop

    while c == "y" or c == "Y":
        x = int(input("Enter your bet: ", ))
        y = Dice()
        # runs through the Dice class
        y.roll()
        y.totaldice()
        t = y.show()
        print()
        print("First roll: ", t[0])
        print()
        print("Second roll: ", t[1])
        print()
        y.doubles()
        print("You're total for this turn is: ", y.totaldice())

        # checks to see if a natural is rolled on the first roll
        
        if y.totaldice() == 7 or y.totaldice() == 11:
            print("You won!")
            print()
            bank += x

            if bank < 0:
                print("You owe the bank $" + str(abs(bank))+"!")

            if bank == 0:
                print("You're currently even with the bank!")

            if bank > 0:
                print("Your current winnings are $" + str(bank)+"!")

        # checks to see if a 2, 3, or 12 is rolled on the first roll
                
        elif y.totaldice() == 3 or y.totaldice() == 2 or y.totaldice() == 12:
            print("You crapped out!")
            print()
            bank -= x

            if bank < 0:
                print("You owe the bank $"+ str(abs(bank))+"!")

            if bank == 0:
                print("You're currently even with the bank!")

            if bank > 0:
                print("Your current winnings are $"+ str(bank)+"!")

        # establishes a box point if the above conditions are not met
                
        else:
            print("Your box point is", y.totaldice(), ". You need to roll that again.")
            setpoint = y.totaldice()
            value = 0

            while value == 0:
                z = Dice()
                z.roll()
                z.totaldice()
                u = z.show()
                print()
                print("First roll: ", u[0])
                print()
                print("Second roll: ", u[1])
                print()

                # if a 7 is rolled before the box point, the user craps out
                
                if z.totaldice() == 7:
                    print("You lose!")
                    print()
                    bank -= x

                    if bank < 0:
                        print("You owe the bank $"+ str(abs(bank))+"!")

                    elif bank == 0:
                       print("You're currently even with the bank!")

                    elif bank > 0:
                       print("Your current winnings are $"+ str(bank)+"!")

                    value += 1

                    # if the boxpoint is reached first, the user wins
                     
                elif z.totaldice() == setpoint:
                        print("You win!")
                        bank += x

                        if bank < 0:
                            print("You owe the bank $"+ str(abs(bank))+"!")

                        if bank == 0:
                            print("You're currently even with the bank!")

                        if bank > 0:
                            print("Your current winnings are $"+ str(bank)+"!")

                        value += 1

                # if neither condition is met, the program cycles through
                # again until either the 7 or the box point is reached
                        
                else:
                    value = 0

        # asks the user if they want to play again
                    
        c = input("No time to stop now! Would you like to play again? Y/N: ", )

# call the function to play the game


craps()