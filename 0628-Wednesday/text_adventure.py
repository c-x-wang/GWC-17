start = '''
You and your family are heading on a road trip across the country.
Your family has 4 people and each has packed a suitcase full of their belongings.
Your family is very indecisive, so your are the one in change of making all the
decisions. Keep in mind that each decision has its own consequences...
'''
print(start)

in_game = True
while in_game:
    print("The first decision you must make is which car to take: your family has an SUV and a sports car.")
    print("Which car would you like to take?")
    user_input = input()
    if user_input == "SUV":
        #in_game = False
        while True:
            print("You decide to take the SUV. After driving for an hour, you see an off-road trail that looks pretty interesting.")
            print("Would you like to take this trail?")
            user_input = input()
            if user_input == "yes":
                print("It gets dark quickly, and there are no streetlights on this trail.")
                print("Now you are lost, and you are forced to stop.")
                break
            elif user_input == "no":
                print("The drive was very smooth and you reached your destination safely! :)")
                break
            print("Try again, you didn't select a valid choice.")
    elif user_input == "sports car":
        #in_game = False
        while True:
            print("You choose to take the sports car. However, you failed to consider the weight limit of the sports car.")
            print("The total weight of your luggage exceeds the weight limit of the car, so you'll have to throw out a few suitcases to be able to drive safely.")
            print("Would you like to throw out a couple suitcases?")
            user_input = input()
            if user_input == "yes":
                print("Uh oh! You realized too late that your phone charger was in one of the suitcases that you had thrown out.")
                print("Your phone battery dies quickly and you lose all connection to the outside world.")
                break
            elif user_input == "no":
                print("Because your luggage exceeded the weight limit of the sports car, the car malfunctions.")
                print("You get a flat tire, and now you are stranded on the side of the road.")
                break
            print("Try again, you didn't select a valid choice.")
    print("Try again, you didn't select a valid choice.")
