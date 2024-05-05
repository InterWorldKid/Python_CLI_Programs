"""
Contributers: InterWorldKid

Contributions: The whole program

This Python module simulates a shopping cart system designed for a retail environment.
It supports functionalities such as adding and removing products from the cart, 
displaying the cart's contents, and checking out with automatic VAT and discount 
calculations. The system reads inventory data from a CSV file, which populates an 
INVENTORY dictionary with product details such as name, quantity available, and price.

"""
import csv #import csv file

INVENTORY = {} #create a global dictionary for the inventory
VAT_RATE = 0.07 #7% overall VAT
DISCOUNT_RATE = 0.1 #10% discount on+ 3 items or more for a product

def read_data(file_path):
    """
    Each line in the CSV file represents a product with its corresponding
    quantity and price. The function updates the global INVENTORY dictionary
    with product names as keys and tuples containing the quantity as int
    and price as float as values
    """
    with open(file_path, "r") as file: #open file
        data = csv.reader(file) #read data from file
        next(data) #skip header
        for line in data: #print each row in that file
            INVENTORY[line[0]] = int(line[1]), float(line[2])

class Article:
    """
    A class to represent an article or product in an inventory.

    Attributes:
    __name: The name of the product, a string
    __price: The price of the product, a float
    __quantity (int): The available quantity of the product, an integer

    Methods:
    getName: Returns the name of the product.
    getPrice: Returns the price of the product.
    getQuantity: Returns the available quantity of the product.
    setQuantity: Sets the quantity of the product
    __str__: Returns a string representation of the product details
    """

    __slots__ = ["__name", "__price", "__quantity"]
    def __init__(self, name, price, quantity): #use __slots__ to explicitly declare data members
        """Constructs all the necessary attributes for the Article object"""
        # Initialize each attribute with the value passed to the constructor
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def getName(self):
        """Gets and retrieves the name for the object"""
        return self.__name #return the private name attribute
    
    def getPrice(self):
        """Gets and retrieves the price for the object"""
        return self.__price #return the private name attribute
    
    def getQuantity(self):
        """Gets and retrieves the quantity for the object"""
        return self.__quantity #return the private name attribute
    
    def setQuantity(self, quantity):
        """Sets and changes the value for the quantity of an object"""
        self.__quantity = quantity #set the private quantity attribute to a new value

    def __str__(self):
        """Displays the article's name, quantity, and price"""
        #return a formatted string that provides a comprehensive description of the product
        return f"Article: {self.getName()}, Quantity: {self.getQuantity()}, Price: {self.getPrice()}"

class Cart:
    """
    A class to manage a shopping cart in a retail environment.
    
    attributes: list_of_purchased (list): A list of Article objects representing items added to the cart
    
    methods: addProduct(name, quantity): Adds a product to the cart or updates its quantity if already present
        removeProduct(name, quantity): Removes a specified quantity of a product from the cart or removes it entirely if quantity exceeds or matches current
        displayCart(): Prints the contents of the cart
        checkout(): Calculates and displays the total cost of the cart, including discounts and VAT
        
    """
    def __init__(self):
        """
        Initialize a new instance of Cart with an empty list for storing purchased items
        """
        self.list_of_purchased = []

    def addProduct(self, name, quantity):
        """
        Adds a specified quantity of a product to the cart or increases the quantity if the product is already in the cart.

        Parameters:
            name: The name of the product to be added.
            quantity: The quantity to be added.

        If the product is not found in the INVENTORY, a message is printed.
        """
        if name in INVENTORY.keys(): #check if the input is in the choices
            stock_quantity, price = INVENTORY[name] #assign and get the quantity and price of a product
            if quantity > INVENTORY[name][0]: #if the wanted quantity is more than inventory put all available quantity
                quantity = stock_quantity

            #INVENTORY[name] = (stock_quantity - quantity, price)

            flag = False  #if the article exists then add to it the quantity
            for article in self.list_of_purchased:
                if article.getName() == name: #check if the input article name is there in cart
                    article.setQuantity(article.getQuantity() + quantity) #add the previous quantity with the new one
                    flag = True
                    break
            
            if flag == False: #if it is not present from before then add it as new itm
                self.list_of_purchased.append(Article(name, price, quantity))
            
            #else:
            INVENTORY[name] = (stock_quantity - quantity, price) #update the inventory

        else: #if item not in inventory then print this message
            print(f"Item {name} is not found in the inventory")

    def removeProduct(self, name, quantity):
        """
        Removes a specified quantity of a product from the cart, or removes the 
        product entirely if the specified quantity is equal to or greater than the 
        quantity in the cart.

        Parameters:
            name: The name of the product to remove.
            quantity: The quantity of the product to remove.
        """

        if name in INVENTORY.keys(): #check if item to be removed exist in the inventory
            for article in self.list_of_purchased:
                if article.getName() == name: #check availability in cart

                    current_quantity = article.getQuantity()
                    
                    if quantity >= current_quantity: #if specified quantity is bigger or more than the inventory then get max
                        self.list_of_purchased.remove(article) #remove the item
                        INVENTORY[name] = (INVENTORY[name][0] + current_quantity, INVENTORY[name][1]) #update inventory

                    else:
                        article.setQuantity(current_quantity - quantity) #remove the specified amount of items
                        INVENTORY[name] = (INVENTORY[name][0] + quantity, INVENTORY[name][1]) #update inventory
                    
                    print(f"Removed {quantity} of {name} from the cart.") #print removed item and its quantity
        else:
            print(f"Item {name} is not found in the cart") #if the article doesn't exist in cart

    def displayCart(self):
        """
        Display the content of a cart name, quantity and price 
        """
        articles = self.list_of_purchased #get list
        if self.list_of_purchased == []: #if empty then no items in cart
            print("Sorry the shopping cart is empty") 
            return None
        
        for article in range(len(articles)): #print the articles their name, quantity and price
                print(f"Article {article+1}-",articles[article])

    def checkout(self):
        """
        Checkout the cart, calculate the total where if an article has more than
        3 items apply discount to it. Apply then at end a total VAT to the amount.
        """
        if len(self.list_of_purchased) == 0: #if no elements then empty
            print("Cannot checkout, cart is empty!")
            return None

        #add items quantity and prices from cart
        shopping_price_quantity = [[article.getQuantity(), article.getPrice()] for article in self.list_of_purchased]
        discount = (1-DISCOUNT_RATE) #get discount percentage 
        vat = (1+VAT_RATE) #get vat percentage
        total_amount_no_vat = 0 #total amount initialized equal to 0

        for article in shopping_price_quantity:

            if article[0] > 3: #if article has more than 3 items then apply discount
                total_per_article = article[0] * article[1] * discount #apply discount

            else: #if less than or equal 3 don't apply
                total_per_article = article[0] * article[1]
            
            total_amount_no_vat += total_per_article #add the amount of each article to the total
        
        total_amount_with_vat = total_amount_no_vat * vat #total amount with VAT applied
        print(f"Your bill is {round(total_amount_with_vat, 2)}$")

def check_choice(customer_choice):
    """Check if the input is valid and exists"""
    if customer_choice in ["1", "2", "3", "4", "5", "6"]:
        return customer_choice #if the choice is in this list then it exists
    print("Invalid choice!")

def perform_operation(crt, choice, file_path):
    """
    This function is passed the cart object and the choice to perform 
    the specific act or operation i.e. remove, add and checkout
    """
    if choice == "1": #if 1 display inventory
        print(INVENTORY)
    elif choice == "2": #if 2 display cart items
        crt.displayCart()
    elif choice == "3": #if 3 add item
        item_add = input("Add item from our catalouge: ") #ask about item
        try:
            quantity_add = int(input(f"Add the quantity for {item_add}: ")) #quantity to add
            crt.addProduct(item_add, quantity_add) #add it
        except ValueError:
            print("Invalid item or quantity")
        # crt.addProduct(item_add, quantity_add) #add it
    elif choice == "4": #if 4 then remove item from cart
        item_remove = input("Remove item from our catalouge: ") #ask for item
        try:
            quantity_remove = int(input(f"Remove the quantity for {item_remove}: ")) #remove this quantity
            crt.removeProduct(item_remove, quantity_remove) #perform operation
        except ValueError:
            print("Invalid item or quantity")
        # crt.removeProduct(item_remove, quantity_remove) #perform operation
    elif choice == "5": #if 5 calculate total price
        crt.checkout()
    elif choice == "6": #exit program
        return False

def menu():
    """
    This function is responsible for printing cart and program operations to the user
    """
    print("1. List all items, inventory and price") 
    print("2. List cart shopping items")
    print("3. Add an item to the shopping cart")
    print("4. Remove an item from the shopping cart")
    print("5. Checkout")
    print("6. Exit")

def main():
    """
    The main function takes a file path to the csv file, then it creates an object for
    the cart. Then function read_data reads file content and saves it in the inventory
    then the program keeps looping and asking the user about the intended operation or
    act to perform on the cart.
    """
    file_path = "products.csv" #take file path
    crt = Cart() #create cart object
    read_data(file_path) #read and save file data in the inventory
    while True: #keep looping
        menu() #display menu
        print("")
        customer_choice = input("Enter your choice: ") #ask user about operation to be done
        print("")
        choice = check_choice(customer_choice) #get customer choice
        keep_operation = perform_operation(crt, choice, file_path) #perform the operatio and update operation activity status
        if keep_operation == False: #if option 6 then exit program
            print("Thanks for shopping with us, return soon!")
            break
        print("")
        continue_yes_no = input("Do you want to continue (y/n or any button)? ") #ask user if he wants to continue
        if continue_yes_no.lower() == "y": #if yes continue and keep looping
            continue
        else: #otherwise exit program and display message
            print("Thanks for shopping with us, return soon!")
            break
    

if __name__ == "__main__":
    main()
