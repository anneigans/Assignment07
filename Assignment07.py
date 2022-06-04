# ---------------------------------------------------------------------------- #
# Title:
# Description: Creating a new script that demonstrates how Pickling and Structured error handling work.
#ChangeLog:
# achristnovich,20220530,Created script
# Data on a to-do list and priority;
# User inputs a task and ranks it from 1-4, 1 being urgent;
# Program prints back list to user;
# User should see error message for non-1-4 answer.

# ---------------------------------------------------------------------------- #

import pickle

#data ---------------------------------------------------------------------------- #
file_name = "ToDoList.txt"
table_lst = [] #lstCustomer from Lab 7-1
choice_str = "" #User's
task = None
priority = None

# Processing  --------------------------------------------------------------- #
class Processor:

    @staticmethod
    def read_data_from_file(file_name):
        file = open(file_name, "rb") #open file, read binary
        list_of_rows = pickle.load(file) #passes file into load
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        row = {"task": str(task).strip(), "priority": int(priority)} #int(priority?)
        list_of_rows.append(row)  # adds data to memory
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        file = open(file_name, "wb") #write in binary
        pickle.dump(list_of_rows, file) #converts Python object hierarchy
        file.close()
        #return list_of_rows

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    @staticmethod
    #input a task and catch any input that isn't 1-4 integer
    def input_new_task_and_priority():
        task = str(input("Enter a task: "))
        valid = False # boolean logic False means input defaults to "False" and only passes when 1-4 is entered.
        priority = None # allows variable to be defined and pass into loop
        while not valid: # While the statement is True (and Valid = False, so it's saying True means False)
            try:
                priority = int(input("Give the task a 1-4 priority, 1 being urgent, 4 being not at all urgent: ")) #assign type
                if int(priority) > 4: # If the input is greater than 4
                    raise TypeError("Please enter a number less than 5.") #raise custom ValueError
                if int(priority) < 1:
                    raise TypeError("Please enter a number greater than 1") #raise custom ValueError
                valid = True
            except ValueError:
                print("That was not a number. Please give priority between 1-4.")
            except Exception as e:
                print(type(e))
                print(e)
        print()
        return task, priority

# Main Body of Script  ------------------------------------------------------ #
# Step 1 - When the program starts, Load data from ToDoFile.txt.
try:
    table_lst = Processor.read_data_from_file( file_name)  # read file data
except:
    print("No pickle for you.")
while (True):
    task, priority = IO.input_new_task_and_priority() # calls function for user input
    Processor.add_data_to_list(task, priority, table_lst) # adds user input data to list in memory
    Processor.write_data_to_file( file_name, table_lst) # writes the data to pickled file
    print(table_lst)
    choice_str = input("Enter to continue or type 'exit' to quit!")
    if choice_str.strip() == "exit":
        print("data saved, goodbye!")
        break
