from random import *
#import random

# Generating a menu from random lists of dishes
appetizers = ["Buffalo Chicken Dip", "Pepper Poppers", "Homemade Guacamole", "Glazed Chicken Wings", "Cucumber-Stuffed Cherry Tomatoes"]
main_courses = ["Beef Enchiladas", "Coconut Shrimp", "Crab Cakes", "Meatloaf", "General Tso's Chicken"]
sides = ["Potato, Squash & Goat Cheese Gratin", "Pearl Couscous Salad with Cherries & Arugula", "Garlicky Roasted Broccoli", "Super-Crispy Oven-Baked Asparagus Fries", "Hasselback Tater Tots"]
desserts = ["Cheesecake", "Brownies", "Creme Brulee", "Apple Pie", "Flan"]
drinks = ["Coffee", "Tea", "Lemonade", "Soda", "Orange Juice"]
print ("Your menu is: ")
print (appetizers[randint(0, len(appetizers)-1)], end=", ")
print (main_courses[randint(0, len(main_courses)-1)], end=", ")
print (sides[randint(0, len(sides)-1)], end=", ")
print (desserts[randint(0, len(desserts)-1)], end=", ")
print (drinks[randint(0, len(drinks)-1)])
print ()

# Generating a haiku from lists of lines. Syllable structure: 5-7-5
syllable5 = ["I like to eat food.", "You have a nice hat", "There lies a big dog."]
syllable7 = ["I don't like aggressive dogs.", "Your hat has a nice flower.", "I try to choose healthy food."]
print ("Your haiku is: ")
print (syllable5[randint(0, len(syllable5)-1)])
print (syllable7[randint(0, len(syllable7)-1)])
print (syllable5[randint(0, len(syllable5)-1)])
print ()
