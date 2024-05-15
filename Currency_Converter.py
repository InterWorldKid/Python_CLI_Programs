"""
Module Name: group5-activity2

Contributors: InterWorldKid

Module description: 

The main purpose of this module is to do currency conversion operations from AED to GBP, DOLLARS, EURO
and from GBP, DOLLARS, EURO to AED. The program starts by asking the user about the conversion direction 
so the program know if the user wants to convert from AED to other currencies or from other currencies to
AED or Exit the program. After choosing any of those 3 the program will start asking about the amount of 
money to be converted and the specific currency conversion operation after displaying the results the program
prompts the user and asks whether he would like to do another conversion (repeat the program) or not.


"""
# All those constants are created to ease the edit of exchange rates

AED_to_GBP_conversion_rate = 0.215648 # 1GBP = 4.64 AED 
AED_to_EUR_conversion_rate = 0.251774 # 1EUR = 3.97 AED
AED_to_DOLLAR_conversion_rate = 0.272257 # 1USD = 3.67 AED

def aed_to_euro(money):
    """This function takes money as an argument and converts the entered AEDs to EURO """

    euro_from_AED = money*AED_to_EUR_conversion_rate # Since 1EUR = 3.97 AED -> 1AED = EUR/3.97
    print(f"{money} AED is equal to {euro_from_AED:.2f} EUR") # Print the AED amount and its EUROs equivalent

def aed_to_british_pound(money):
    """This function takes money as an argument and converts the entered AEDs to GBP """

    british_pound_from_AED = money*AED_to_GBP_conversion_rate # Since 1GBP = 4.64 AED -> 1AED = GBP/4.64
    print(f"{money} AED is equal to {british_pound_from_AED:.2f} GBP") # Print the AED amount and its GBPs equivalent

def aed_to_dollar(money):
    """This function takes money as an argument and converts the entered AEDs to DOLLAR """

    dollar_from_AED = money*AED_to_DOLLAR_conversion_rate # Since 1USD = 3.67 AED -> 1AED = USD/3.67
    print(f"{money} AED is equal to {dollar_from_AED:.2f} Dollars") # Print the AED amount and its USD equivalent

def dollar_to_aed(amount):
    """This function takes money as an argument and converts the entered DOLLARS to AED """

    AED_from_dollar = amount/AED_to_DOLLAR_conversion_rate # Since 1USD = 3.67 AED
    print(f"{amount} Dollars is equal to {AED_from_dollar:.2f} AED") # Print the USD amount and its AED equivalent

def british_pound_to_aed(amount):
    """This function takes money as an argument and converts the entered GBP to AED """

    AED_from_british_pound = amount/AED_to_GBP_conversion_rate # Since 1GBP = 4.64 AED
    print(f"{amount} GBP is equal to {AED_from_british_pound:.2f} AED") # Print the GBP amount and its AED equivalent

def euro_to_aed(amount):
    """This function takes money as an argument and converts the entered EUROs to AED """

    AED_from_euro = amount/AED_to_EUR_conversion_rate # Since 1EUR = 3.97 AED
    print(f"{amount} Euro is equal to {AED_from_euro:.2f} AED") # Print the EUR amount and its AED equivalent

def welcome_banner():
    """The welcome banner only prints the introduction text of the program"""

    print("---------------------------------")
    print('"           Main Menu           "')
    print("   Welcome to Currency Converter   ")
    print("---------------------------------\n\n")

def menu_options():
    """The menu_options function prints the program main conversion direction"""

    print("1. AED to other currencies") 
    print("2. Other currencies to AED")
    print("3. Exit\n")

def AED_to_other_options():
    """The AED_to_other_options function prints the main AED to GBP/USD/EUR conversion operations"""

    print("1. AED to Euro (EUR)")
    print("2. AED to British Pound (GBP)")
    print("3. AED to US Dollar\n")

def Other_to_AED_options():
    """The Other_to_AED_options function prints the main GBP/USD/EUR to AED conversion operations"""

    print("1. Euro (EUR) to AED")
    print("2. British Pound (GBP) to AED")
    print("3. US Dollar to AED\n")

def main():
    """
    The main function consits of a forever while loop which includes all prompts for the user and currency
    conversions operations. After the user input a choice the program if the input is valid or not then perform
    the operation accordingly. 

    1- we display the menu
    2- we display conversion direction options
    3- we ask about the amount to be converted
    4- ask about the currency to convert to from the conversion direction
    5- display the amount entered and its converted corresponding currency
    6- ask user if he wants to reuse the program
    """
    continue_conversion = True

    while continue_conversion: # loop forever 
        welcome_banner() #print the welcome and the program intro text
        menu_options() #print data conversion direction options
        conversion_direction = input("Enter the conversion direction - choice (1/2/3): ") #ask the user about the conversion direction
        print("") #provide spacing for better organization

        #if the enter number is not 1 or 2 or 3 then reprompt the user to enter one of the available options
        while conversion_direction != "1" and conversion_direction != "2" and conversion_direction != "3":
                print("Invalid conversion direction")
                print("")
                menu_options()
                conversion_direction = input("Enter the conversion direction - choice (1/2/3): ") #prompt the user to input a valid option
        if conversion_direction == "3": #if the entered choice of conversion direction was 3 (Exit) then we break out from the forever while loop
            print("Bye!")
            break
        if conversion_direction == "2": #if the entered choice of conversion direction was 2 the program will start to prompt the user to chose a currency (GBP/EUR/USD) to convert to AED
            while True:
                try:
                    amount = float(input("Enter the amount you want to convert to AED: "))
                    if amount < 0:
                        print("Entered negative amount. Please enter a positive amount.")
                    else:
                        break  # Exit the loop if the input is valid
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
                    print("")  # Provide spacing for readability
            Other_to_AED_options() #provide conversion from other currencies to AED options
            traget_currency = input("Enter the target currency from the above menu - choice (1/2/3): ") #prompt the user to enter the currency to be converted to AED
            while traget_currency != "1" and traget_currency != "2" and traget_currency != "3": #check if the target currency option is valid
                print("Invalid target currency input")
                traget_currency = input("Enter the target currency from the above menu - choice (1/2/3): ")
            if traget_currency == "1": #if 1 is entered then the amount of euros will be converted to AED
                euro_to_aed(amount)
            elif traget_currency == "2": #if 2 is entered then the amount of british pound will be converted to AED
                british_pound_to_aed(amount)
            elif traget_currency == "3": #if 3 is entered then the amount of dollars will be converted to AED
                dollar_to_aed(amount)

        elif conversion_direction == "1": #if the data direction chosen option is 1 then we will convert the AED to the other 3 currencies
            while True:
                try:
                    money = float(input("Enter the amount of AED you want to convert: "))
                    if money < 0:
                        print("Please enter a positive amount.") #reprompt the user to enter a positive amount
                    else:
                        break  #exit the loop if the input is valid and positive
                except ValueError:
                    print("Please enter a numeric value.") #reprompt the user to enter a numeric value
                print("")  #provide spacing for readability

            AED_to_other_options() #display AED to other currencies options
            traget_currency = input("Enter the target currency from the above menu - choice (1/2/3): ") #ask user to enter one of the options
            while traget_currency != "1" and traget_currency != "2" and traget_currency != "3": #check if the entered option is available
                print("Invalid target currency input")
                traget_currency = input("Enter the target currency from the above menu - choice (1/2/3): ") #reprompt the user to enter one of the available options
            if traget_currency == "1":
                aed_to_euro(money) #if 1 is entered then AED will be converted to EUROs
            elif traget_currency == "2":
                aed_to_british_pound(money) #if 2 is entered then AED will be converted to GBP
            elif traget_currency == "3":
                aed_to_dollar(money) #if 3 is entered then AED will be converted to USD

        ask_user = input("Do you want to do another conversion (y/n): ") #after performing operations and conversions we will ask the user if he would like to reuse the program
        while ask_user != "y" and ask_user != "n": #check if the entered option is valid or not
            print("Invalid response")
            ask_user = input("Do you want to do another conversion (y/n): ") #reprompt the user to input either y for yes or n for no
        if ask_user == "n": #if the entered letter is n then break from the forever loop and end program
            print("")
            print("Bye!")
            break
        else:
            continue #if y is entered then we continue and start the program again
        
if __name__ == "__main__":
    main()
