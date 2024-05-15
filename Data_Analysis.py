"""
Contributers: InterWorldKid

This module implements a Command Line Interface (CLI) tool for data analysis. The tool guides users through a sequence of stages for
managing and analyzing CSV data, including data loading, cleaning, analysis, and visualization.

The CLI tool is designed to:
1- Load data from CSV files, prompting the user to select a valid numerical column for analysis.
2- Clean and prepare data by replacing empty or invalid entries based on user preference for
  filling such gaps (minimum, maximum, or average values of the column).
3- Analyze the cleaned data through sorting mechanisms, offering ascending or descending order options.
4- Visualize the sorted data by displaying a star representation for each entry, providing a simple
  visual summary of the data values.

"""


import csv #import csv module to process the csv file data
from math import ceil #import ceil to use it in visualize function

def open_file():
    """
    Prompts the user to enter a file path and attempts to open and read a CSV 
    file from that path. Continuously prompts until a valid file path is provided.
    The function reads the file, prints its headers, and lines, and then allows 
    the user to select a column.

    Returns: A list of the csv file data and the header content
    """
    data_list = []
    while True:
        try:
            file_path = input("Please enter path to the csv file: ") #get path from user
            with open(file_path, "r") as file: #open the file
                print("File exists.") #let the user know that the file exists and that it loaded successfully
                print("Loading file… ")
                print("File successfully loaded!")
                print("") #for spacing
                data = csv.reader(file) #read the csv content as lists
                header = next(data) #save the header and skip it
                print(header) #just display header to let the user know the names of columns
                for line in data: #display file data (as rows)
                    data_list.append(line) #add the rows to the data list to perform operations on it later
                    print(line) #show it to the user
                print("")
                print("Choose column from selection below to clear and prepare data: ")
                for i in range(0, len(header)): #display header columns names
                    print(" /" , header[i] , end="") #print each header with a slash prefix
                return data_list, header #return the collected data and headers.
        except FileNotFoundError: #handle the error for a wrong file path
            print("")
            file_path = print("Wrong input. ", end = "") #return a message if file is not found

def check_column(header):
    """
    Prompts the user to select a column from the provided header list.
    Continues to ask for input until the user provides a valid column name.

    Parameters:
        The input parameter is the header list of strings representing the header 
        names of a CSV file.

    Returns:
        The index of the chosen column and the name of the column.
    """
    column_input = input("Please choose column: ") #ask the user to enter column name
    column_flag = True #set flag to true
    while column_flag:
        for column in range(0, len(header)): #check if the input header matches any header 
            if column_input == header[column].strip():
                return column, header[column] #return the column of the header and its index
        column_input = input("Column doesn't exist, Please try again: ") #if not found keep asking the user to enter the column name

def collect_column_values(data_list, column_index, header):
    """
    Collects and validates that all entries in a specified column are numeric. If non-numeric entries are found,
    prompts the user to select a different column.

    Parameters:
        data_list (list of list): The dataset from which to collect column values.
        column_index (int): The index of the column to collect values from.
        header (list of str): The header names of the dataset.

    Returns:
        list: A list of numeric values from the specified column.
    """
    numeric_flag = True
    column_values = [] #create an empty list to store the numerical column
    while numeric_flag:
        try:
            for item in data_list: #loop in the column data 
                if (item[column_index].strip() == "") or float(item[column_index].strip()): #if the element is either an empty string or a number add it to the list
                    #print("pass")
                    column_values.append(item[column_index])
                    continue
            numeric_flag = False
        except ValueError: #if an error occured (no empty or numerical value then handel the exeption and reprompt the user)
            column_values = [] #clear the column values list and reprompt user
            print("Non-numerical column try again. " ,end="") #reprompt the user
            column_index, column_name = check_column(header) #recheck if column exists
    return column_values #if found and numerical or with empty strings return that column

def clean_choice():
    """
    This function is responsible for checking the choice input for the cleaning stage
    or clean function
    """
    clean_choice = input("Enter your choice: ") #ask user about the cleaning choice (max, min or avg)
    while True:
        if clean_choice == "1" or clean_choice == "2" or clean_choice == "3": # if the choice is 1, 2 or 3 then break from loop
            break
        else:
            clean_choice = input("Invalid choice. Enter again: ") #if not valid reprompt
    return clean_choice #return the choice from the user

def get_max(column_values):
    """
    Calculate the maximum numeric value from a list of strings. Ignores empty strings.

    Args:
    column_values (list of str): A list of strings, where each string is expected to represent a numeric value.

    Returns:
    float or None: The maximum value found, or empty string if no valid numeric value exists.
    """
    max_num = "" #set max to an empty string if no number is found
    for i in column_values:
        if i.strip(): #this will be False for empty or whitespace only strings
            current_num = float(i) #convert this string to float
            if max_num == "" or current_num > max_num: #if the current value is bigger than than the max then this is bigger hence it is the max
                max_num = current_num #if condition met set the max num as current num
    return max_num

def get_min(column_values):
    """
    Calculate the minimum numeric value from a list of strings. Ignores empty strings.

    Args:
    column_values (list of str): A list of strings, where each string is expected to represent a numeric value.

    Returns:
    float or None: The minimum value found, or empty string if no valid numeric value exists.
    """
    min_num = "" #set max to an empty string if no number is found
    for i in column_values:
        if i.strip(): #this will be False for empty or whitespace only strings
            current_num = float(i) #convert this string to float
            if min_num == "" or current_num < min_num: #if the current value is smaller than than the minimum then this is bigger hence it is the minimum
                min_num = current_num #if condition met set the min num as current num
    return min_num

def get_avrg(column_values):
    """
    Calculate the average of numeric values in a list of strings, ignoring empty strings.
    Empty strings are skipped. Returns the average rounded to two decimal places.

    Args:
        column_values (list of str): List of strings to calculate the average from.

    Returns:
        float or empty: The average of the numeric values, or None if no numbers are present.
    """
    number_of_elements = 0
    sum = 0
    try:
        for item in column_values: #loop through the items in the column
            if item.strip() == "":  #if the element is empty skip it
                continue
            number_of_elements += 1 #increase counter by 1 if number is found
            sum += int(item.strip()) #add the number to the total sum
        return round(sum/number_of_elements, 2) #return the rounded average
    except ZeroDivisionError:
        return None #if no elements are present it means that this is an empty list

def replace_empty_values(column_values, empty_cell_value):
    """
    Replace empty strings in a list of column values with a specified value.

    Args:
        column_values (list of str): List of column values (strings) to process.
        empty_cell_value (any): Value to replace empty strings with, will be converted to string.

    Returns:
        None: The function modifies the list in place.
    """
    for element in range(0, len(column_values)): #loop in the column
        if column_values[element].strip() == "": #if empty replace it with the empty cell value (max, min or avg)
            column_values[element] = str(empty_cell_value)

def insertion_sort(cleaned_column_values):
    """
    Sorts a list of strings that represent numeric values in ascending order using the insertion sort algorithm.

    Args:
        cleaned_column_values (list of str): The list of strings to sort.
    """
    for idx in range(1, len(cleaned_column_values)): #iterate through each element in the list starting from the second element.
        key = float(cleaned_column_values[idx].strip()) #convert the current element to a float after stripping any whitespace.

        j = idx - 1 #initialize the position for comparing 'key' with the sorted part of the list.
        while j>=0 and key<float(cleaned_column_values[j].strip()): # Continue moving elements one position to the right as long as 'key' is less than elements in the sorted part.
            cleaned_column_values[j+1]=cleaned_column_values[j] #move the element at index 'j' to the right to make space for 'key'.
            j=j-1 #decrement 'j' to compare 'key' with the next element on the left.
        cleaned_column_values[j+1] = str(key) #insert 'key' in its correct position in the sorted part of the list.
    cleaned_column_values[0] = str(float(cleaned_column_values[0].strip())) #convert the first element to a string

def reverse_insertion_sort(cleaned_column_values):
    """
    Sorts a list of strings that represent numeric values in descending order using the insertion sort algorithm.
    Same as insertion sort algorithm but to sort in a descending order key>data_array[j]
    Args:
        cleaned_column_values (list of str): The list of strings to sort.
    """
    for idx in range(1, len(cleaned_column_values)): #iterate through each element in the list starting from the second element.
        key = float(cleaned_column_values[idx].strip()) #convert the current element to a float after stripping any whitespace.

        j = idx - 1 #initialize the position for comparing 'key' with the sorted part of the list
        while j>=0 and key>float(cleaned_column_values[j].strip()): #to sort in a descending order key>data_array[j]
            cleaned_column_values[j+1]=cleaned_column_values[j] #move the element at index 'j' to the right to make space for 'key'.
            j=j-1 #decrement 'j' to compare 'key' with the next element on the left.
        cleaned_column_values[j+1] = str(key) #insert 'key' in its correct position in the sorted part of the list.
    cleaned_column_values[-1] = str(float(cleaned_column_values[-1].strip())) #convert the first element to a string


def check_sorting_choice(sorting_choice):
    """
    Validates the user's input for a sorting choice. Continues to prompt until a valid choice ("1" or "2") is entered.

    Args:
        sorting_choice (str): The initial user input for the sorting choice.

    Returns:
        str: The valid sorting choice input by the user.
    """
    while True:
        if sorting_choice.strip() == "1" or sorting_choice.strip() == "2": #if the input matches the choices 1 and 2 then return the user input
            return sorting_choice
        sorting_choice = input("Invalid choice. Please enter your choice again: ") #otherwise keep asking for the correct available choice
    
#Main program functions are below

def welcome():
    """
    Displays a welcome message and a menu of options for a data analysis CLI tool.
    
    This function prints a series of statements that serve as the main menu for the application,
    guiding the user through the available actions such as loading data, cleaning/preparing data,
    analyzing data, and visualizing results.
    """
    print("----------------------------")
    print("Welcome to Data Analysis CLI")
    print("----------------------------")
    print("1. Load Data")
    print("2. Clean and Prepare Data")
    print("3. Analyse Data")
    print("4. Visualize Data")

def load():
    """
    This function handles:
    1- opening the file
    2- check the column to process if valid
    3- gets the values of the numerical column with empty strings
    4- returns the column values and the column name
    """
    print("\nStage 1: Load Data")
    data_list, header = open_file() #get data list and header name using open file function
    print("")
    column_index, column_name = check_column(header)
    #print(data_list) #For testing the output of our csv data list
    column_values = collect_column_values(data_list, column_index, header)
    #print(column_values) #For displaying the content of a numeric column
    print("\nData Loaded Successfully")
    #print(type(column_values[0]))
    return column_values, column_name

def clean(column_values):
    """
    The clean function takes the numerical column values from the load data function
    then it prpompts the user to input the choice of filling the empty values with
    inside the column with checking if the choice is valid or not. After replacing
    empty values with wanted choice it gets displayed after the update then returned
    to be used in analyzing data section.
    """
    print("Stage 2: Clear and prepare data") #display cleaning options
    print("Would you like to replace empty cells from column with:")
    print("1. Maximum value from column")
    print("2. Minimum value from column")
    print("3. Average value from column")
    choice = clean_choice() #validate choice

    if choice == "1": #make the empty cells value equal to max, min or average based on the input choice
        operation = "maximum"
        empty_cell_value = get_max(column_values)
    elif choice == "2":
        operation = "minimum"
        empty_cell_value = get_min(column_values)
    else:
        operation = "average"
        empty_cell_value = get_avrg(column_values)
    
    #print(column_values) #To see before replacing the empty values
    print("")
    replace_empty_values(column_values, empty_cell_value) #perform the replacement
    print(f"All empty values are replaced with {operation} values!")
    print(column_values) #print the column after replacement is done
    return column_values

def analyze(cleaned_column_values):
    """
    This function is responsible for sorting the cleaned column data in acsending or 
    descending order based on the user input. This function uses insertion sort for 
    ascending order and reverse of the insertion sort for the descending order.
    """
    print("\nStage 3: Analyse data")
    print("Please choose if you want to sort column in:")
    print("1. Ascending order")
    print("2. Descending order")
    sorting_choice = input("Please enter your choice: ") #ask user about the option
    sorting_choice_checked = check_sorting_choice(sorting_choice) #check the input and validate it
    if sorting_choice_checked.strip() == "1": #if the choice is 1 perform isertion sort
        insertion_sort(cleaned_column_values)
        print("Column values are sorted in ascending order!")
    else:
        reverse_insertion_sort(cleaned_column_values) #if the choice is 2 perform inverse of insertion sort
        print("Column values are sorted in descending order!")
    print(cleaned_column_values) #print the sorted column
    return cleaned_column_values #return the sorted column to be used in the vizualizing stage

def visualize(sorted_column_values, column_name):
    """
    The visualize function takes the sorted column values and displays each number
    in the list with the correct number of stars (for each 5 items there is a star 
    equivalent in the graph).
    """
    print("Stage 4: Visualise Data")
    print(f"Column: {column_name}")
    print("Legend: each ‘*’ represents 5 units\n")
    for element in sorted_column_values: #loop in the sorted list
        if float(element.strip()) < 100.0: #if the number is less than 100 represent every 5 items as a star
            stars_count = ceil(float(element.strip())/5) #divide the number of items by 5 and round the number to the closest upper integer
            if stars_count == 0: #if there are no items then it gets represented as a star only
                stars_count = 1 #set star count to 1
        else:
            stars_count = 20 #if the items number is bigger than 100 then we represent the number of items by 20 equivalent stars
        print(stars_count*"*") #multiply the number of star counts by the star string and print it for each element in the list

def main():
    """
    The main function handles the operations of the Data Analysis Command Line Interface (CLI).

    This function coordinates the flow of the entire application, ensuring that data is loaded,
    cleaned, analyzed, and visualized in a sequential manner. It acts as the central controlling
    routine that calls other functions responsible for specific tasks:

    1. Displays the main menu and welcomes the user.
    2. Loads data from a specified source.
    3. Cleans and prepares the data for analysis, handling any necessary preprocessing.
    4. Analyzes the cleaned data, such as sorting or performing calculations.
    5. Visualizes the analyzed data, presenting it in a user friendly format.

    Each step is executed in order, and the outputs from one step are passed as inputs to the next,
    a typical data processing pipeline in a CLI environment.
    """
    #Display main program menu
    welcome() 
    #Load Data
    column_values, column_name = load()
    #Clean and prepare 
    cleaned_column_values = clean(column_values) #pass column values from load data to be cleaned and return the clean column values
    #Analyze
    sorted_column_values = analyze(cleaned_column_values) #pass the cleaned column values to sort them and return the sorted list
    #Visualize
    visualize(sorted_column_values, column_name) #pass the sorted column values to visualize the data for better understanding

if __name__ == "__main__":
    main()
