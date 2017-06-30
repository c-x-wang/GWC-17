#lists
grocery = ["apples", "bananas", "carrots", "doughnuts", "eggs"]

for i in grocery:
    print (i)

item_name = "bananas"
def loopTheList(list = []):
    for item in list:
        if item == item_name:
            return True
    return False

print (loopTheList(grocery))
