
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):

       return self.cost

    def get_quantity(self):

       return self.quantity

    def __str__(self):

        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"



#=============Shoe list===========

#The list will be used to store a list of objects of shoes.
shoe_list = []

#temp list used to store data from file
shoes_file =[]

#==========Functions outside the class==============

#read_shoes function to read text file using try - except error handling, data from text file is appended to shoes_list

def read_shoes_data():

 file = ""
while True:
    try:
     file = open("inventory.txt", "r")
     break
    except FileNotFoundError:
     print("File does not exsit try again")
    break

user = file.read()
shoes_file = user.split("\n")
shoes_file.pop(0)

shoe_list = shoes_file

file.close()

# Function that allows a user to capture data about a shoe and use data to create a shoe object
def capture_shoes():
    country = input("What country is the shoe from: ")
    code = input("What code does the shoe have: ")
    product = input("What input does the shoe have: ")
    cost = input("What cost does the shoe have: ")
    quantity = input("How many shoes are there")

    new_shoe = Shoe(country,code,product,cost,quantity)
    shoe_list.append(new_shoe)
    return

#prints details of all shoes in list
def view_all():
    for i in shoe_list:
        print(i)

#find shoe object with the lowest quantity,#finish this isn't calculating just quantity
def re_stock():
    file = open("inventory.txt", "r")
    user = file.read()
    shoes_file = user.split("\n")
    shoes_file.pop(0)
    print("Object with lowest quantity is ",min(shoes_file))
    file.close()
    choice = input("Do you want to add more of this shoe enter 'y' or 'n' ?")
    if choice == "y":
        shoe_stock = min(shoes_file).split(",")
        new_stock = input("Enter new value for stock: ")
        shoe_stock[4] = new_stock
        new_correct_stock = " ".join(shoe_stock)
        file = open("inventory.txt", "a+")
        file.write(f"\n{new_correct_stock}")
        file.close()


#search shoe function
def seach_shoe():
    file = open("inventory.txt", "r")
    user = file.read()
    shoes_file = user.split("\n")
    shoes_file.pop(0)

    x = len(shoes_file)
    print()
    search = input("Enter the code of the shoe: ")

    for i in range(x):
        if shoes_file[i].find(search) != -1:
            print(shoes_file[i])

    file.close()

#code to find out the value per item, it i s required to enter individual code of shoe before price is shown
def value_per_item():
    file = open("inventory.txt", "r")
    user = file.read()
    shoes_file = user.split("\n")
    shoes_file.pop(0)

    x = len(shoes_file)
    print()
    search = input("Enter the code of the shoe: ")

    for i in range(x):
        if shoes_file[i].find(search) != -1:
            temp = shoes_file[i]
            temp1 = temp.split(",")
            value = int(temp1[3]) * int(temp1[4])
            print(f"Value of this item is {value}")

    file.close()

# it is required to enter indvidual code of shoe before price is shown
def highest_qty():
    file = open("inventory.txt", "r")
    user = file.read()
    shoes_file = user.split("\n")
    shoes_file.pop(0)

    temp = max(shoes_file).split(",")
    temp1 = max(shoes_file)
    print(f"{temp1}")
    print(f"{temp[2]} is now on sale!")


#==========Main Menu=============

userchoice = ""

while userchoice != "quit":
    userchoice = input("\nPlease enter one of the following options view shoes/search shoe/check stock/add shoe/cost of shoe: ")

    if userchoice == "view shoes":
        read_shoes_data()
        view_all()

    elif userchoice =="search shoe":
        seach_shoe()

    elif userchoice =="check stock":
         userchoice_1 = input("Enter 'max' to look at the shoe with the most stock or 'min' to look at the shoe with the least stock: ")
         if userchoice_1 == "max":
          highest_qty()
          #see if you can figure out how to remove line from txt file
         if userchoice_1 == "min":
          re_stock()

    elif userchoice == "add shoe":
         capture_shoes()

    elif userchoice =="cost of shoe":
        value_per_item()

    else:
        print("That isn't an option try again !")
