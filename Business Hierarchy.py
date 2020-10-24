#!/usr/bin/python

import os
import sys
import time
import getpass

"""
Initializing all of the variables to be used
"""

hourly_example = None
salary_example = None
manager_example = None
executive_example = None
accounts = {}
salary_worker = {}
hourly_worker = {}
manager = {}
executive = {}
raise_value = 1.10
username = ""
template = "{0:13}{1:13}{2:15}${3:1}"

"""
Initializing the main employee class. Defaults the 3 main methods: 
give_raise, fire_employee and hire_employee if the worker does not
have that method in their class.
"""


class Employee:

    """
    Creates an instance when employee class is called and saves
    employee's name, position and username
    """

    def __init__(self, first, last, position, user):
        self.first = first.upper()
        self.last = last.upper()
        self.position = position.upper()
        self.user = user

    """
    Returns information on the employee's name, position, pay and username
    """

    def getinfo(self):
        return self.first, self.last, self.position, self.user

    """
    Returns that the user does not have permission to run the following functions
    below
    """

    def give_raise(self):
        print("you are not allowed to give a raise")

    def fire_employee(self):
        print("you are not allowed to fire anyone")

    def hire_employee(self):
        print("you are not allowed to hire anyone")
        

"""
Initializes the hourly employee class. Takes its super class from
the employee class. No functions are being given to this class aside
from viewing employees
"""


class HourlyEmployee(Employee):

    """
    Creates an instance when HourlyEmployee class is called and saves
    employee's hourly pay. Gets the other information from its super
    class Employee. Creates an entry in the dictionary object hourly_worker
    to save the information in running memory.
    """

    def __init__(self, first, last, position, user, hourly):
        super().__init__(first, last, position, user)
        self.hourly = hourly
        hourly_worker[first.upper() + " " + last.upper()] = (position, hourly, user)

    """
    Returns information on the employee's name, position, pay and username
    """

    def getinfo(self):
        return self.first, self.last, self.position, self.hourly, self.user


"""
Initializes the salary employee class. Takes its super class from
the employee class. No functions are being given to this class aside
from viewing employees
"""


class SalaryEmployee(Employee):

    """
    Creates an instance when SalaryEmployee class is called and saves
    employee's salary. Gets the other information from its super
    class Employee. Creates an entry in the dictionary object salary_worker
    to save the information in running memory.
    """

    def __init__(self, first, last, position, user, salary):
        super().__init__(first, last, position, user)
        self.salary = salary
        salary_worker[first.upper() + " " + last.upper()] = (position, salary, user)

    """
    Returns information on the employee's name, position, pay and username
    """

    def getinfo(self):
        return self.first, self.last, self.position, self.salary, self.user


"""
Initializes the manager class. Takes its super class from
the employee class. It has the 3 main methods mentioned above
and are able to hire, fire and give raises to salary and hourly
employees only. 
"""


class Manager(Employee):

    """
    Creates an instance when Manager class is called and saves
    employee's salary. Gets the other information from its super
    class Employee. Creates an entry in the dictionary object manager
    to save the information in running memory.
    """

    def __init__(self, first, last, position, user, salary):
        super().__init__(first, last, position, user)
        self.salary = salary
        manager[first.upper() + " " + last.upper()] = (position, salary, user)

    """
    Returns information on the employee's name, position, pay and username
    """

    def getinfo(self):
        return self.first, self.last, self.position, self.salary, self.user

    """
    Function to give an employee a raise
    """

    def give_raise(self):

        """
        Initializes the variables and clears the screen
        """

        os.system('cls')
        new_pay = 0
        counter = 1

        """
        Asks if the user is an hourly or salary employee
        """

        type_of_pay = input("Is this employee salary or hourly?: ").lower()

        """
        Based on the answer above, will show all the employees in that title
        """

        while True:
            print("\n")
            if type_of_pay == "hourly":
                for names in hourly_worker.keys():
                    if names != "FIRSTNAME LASTNAME":
                        print(names)
                break
            elif type_of_pay == "salary":
                for names in salary_worker.keys():
                    if names != "FIRSTNAME LASTNAME":
                        print(names)
                break
            else:
                type_of_pay = input("incorrect entry. Please type salary or hourly: ")

        """
        Asks which person you would like to give a raise to and confirms it before
        continuing
        """

        name = input("\nWhich employee would you like to give a raise to?: ").upper()

        confirm = input("Are you sure? (yes/no)")

        if confirm == "no":
            main_menu(username)

        """
        Will take the pay of the employee and multiply it by the raise value, initialized 
        as a global variable. It will then recreate the dictionary value to reflect that
        and print the new pay. Catches if the name is incorrect
        """

        try:
            if type_of_pay == "salary":
                for i in salary_worker[name]:
                    if counter == 1:
                        temp_position = i
                    elif counter == 2:
                        new_pay = i * raise_value
                    counter += 1
                salary_worker[name] = (temp_position, new_pay)
                print("{} has successfully been given a raise to {} an hour!".format(name, new_pay))
            elif type_of_pay == "hourly":
                for i in hourly_worker[name]:
                    if counter == 1:
                        temp_position = i
                    elif counter == 2:
                        new_pay = i * raise_value
                    counter += 1
                hourly_worker[name] = (temp_position, new_pay)
                print("{} has successfully been given a raise to {} an hour!".format(name, new_pay))
        except KeyError:
            print("This employee does not exist")

        """
        Takes the user back to the main menu once they press any button
        """

        input("\n\nPress any button to go back to the main menu...")
        main_menu(username)

    """
    Function to fire an employee
    """

    def fire_employee(self):

        """
        Clears the screen
        """

        os.system('cls')

        """
        Asks if the employee is hourly or salary
        """

        type_of_pay = input("Is this employee salary or hourly?: ")

        """
        Based on the answer above, will show all the employees in that title
        """

        while True:
            print("\n")
            if type_of_pay == "hourly":
                for names in hourly_worker.keys():
                    if names != "FIRSTNAME LASTNAME":
                        print(names)
                break
            elif type_of_pay == "salary":
                for names in salary_worker.keys():
                    if names != "FIRSTNAME LASTNAME":
                        print(names)
                break
            else:
                type_of_pay = input("incorrect entry. Please type salary or hourly: ")

        """
        Asks which person you would like to fire and confirms it before
        continuing
        """

        name = input("\nEnter the employee you would like to fire: ").upper()
        confirm = input("Are you sure? (yes/no)")

        if confirm == "no":
            main_menu(username)

        """
        Will find the user in the accounts and titled position dictionaries
        and remove them from the list. Will update the accounts file when
        the user exists the program.
        """

        try:
            if type_of_pay == "salary":
                try:
                    for key, value in salary_worker.items():
                        if key == name:
                            del accounts[value[2]]
                    del salary_worker[name]
                except KeyError:
                    print("That employee does not exist")
                else:
                    print(name + " has been removed")
            elif type_of_pay == "hourly":
                try:
                    for key, value in hourly_worker.items():
                        if key == name:
                            del accounts[value[2]]
                    del hourly_worker[name]
                except KeyError:
                    print("That employee does not exist")
                else:
                    print(name + " has been removed")
        except KeyError:
            print("This employee does not exist")

        """
        Takes the user back to the main menu once they press any button
        """

        input("\n\nPress any button to go back to the main menu...")
        main_menu(username)

    """
    Function to hire an employee
    """

    def hire_employee(self):

        """
        Clears the screen
        """
        os.system('cls')

        """
        Asks for the new hire's information and confirming with the user
        """

        user = input("Please enter the new employee's username: ")
        password = getpass.getpass("Please enter the new employee's password: ")
        title = input("Please enter the new employee's role: (Hourly, Salary, Manager)")
        name = input("Please enter his/her full name: ").upper()
        position = input("Please enter his/her position: ")
        pay = input("Please enter the employee's pay rate: ")
        full_name = name.split(" ")

        confirm = input("Are you sure? (yes/no)")

        if confirm == "no":
            main_menu(username)

        """
        Will create the user with the information above in the running memory
        """

        if title.capitalize() == "Salary":
            SalaryEmployee(full_name[0], full_name[1], position, user, int(pay))
            print(name.upper() + " has been successfully added!")
        elif title.capitalize() == "Hourly":
            HourlyEmployee(full_name[0], full_name[1], position, user, int(pay))
            print(name.upper() + " has been successfully added!")
        else:
            print("invalid entry, please try again...")
            main_menu(username)

        """
        Will add the user to the accounts dictionary, which is used to add it to 
        the accounts text file
        """

        accounts[user] = (password, title.capitalize(), full_name[0], full_name[1], position, int(pay))

        """
        Takes the user back to the main menu once they press any button
        """

        input("\n\nPress any button to go back to the main menu...")
        main_menu(username)


class Executive(Employee):

    """
    Creates an instance when Executive class is called and saves
    employee's salary. Gets the other information from its super
    class Employee. Creates an entry in the dictionary object Executive
    to save the information in running memory.
    """

    def __init__(self, first, last, position, user, salary):
        super().__init__(first, last, position, user)
        self.salary = salary
        executive[first.upper() + " " + last.upper()] = (position, salary, user)

    """
    Returns information on the employee's name, position, pay and username
    """

    def getinfo(self):
        return self.first, self.last, self.position, self.salary, self.user

    """
    Function to give employee a raise
    """

    def give_raise(self):

        """
        Initializes the variables and clears the screen
        """

        os.system('cls')
        new_pay = 0
        counter = 1

        """
        Asks if the user is an hourly, salary or manager employee
        """

        type_of_pay = input("Is this employee hourly, salary or a manager?: ").lower()

        """
        Based on the answer above, will show all the employees in that title
        """

        while True:
            print("\n")
            if type_of_pay == "hourly":
                for names in hourly_worker.keys():
                    if names != "FIRSTNAME LASTNAME":
                        print(names)
                break
            elif type_of_pay == "salary":
                for names in salary_worker.keys():
                    if names != "FIRSTNAME LASTNAME":
                        print(names)
                break
            elif type_of_pay == "manager":
                for names in manager.keys():
                    if names != "FIRSTNAME LASTNAME":
                        print(names)
                break
            else:
                type_of_pay = input("incorrect entry. Please type hourly, salary or manager: ")

        """
        Asks which person you would like to give a raise to and confirms it before
        continuing
        """

        name = input("\nWhich employee would you like to give a raise to?: ").upper()

        confirm = input("Are you sure? (yes/no)")

        if confirm == "no":
            main_menu(username)

        """
        Will take the pay of the employee and multiply it by the raise value, initialized 
        as a global variable. It will then recreate the dictionary value to reflect that
        and print the new pay. Catches if the name is incorrect
        """

        try:
            if type_of_pay == "salary":
                for i in salary_worker[name]:
                    if counter == 1:
                        temp_position = i
                    elif counter == 2:
                        new_pay = i * raise_value
                    counter += 1
                salary_worker[name] = (temp_position, new_pay)
                print("{} has successfully been given a raise to {} an hour!".format(name, new_pay))
            elif type_of_pay == "hourly":
                for i in hourly_worker[name]:
                    if counter == 1:
                        temp_position = i
                    elif counter == 2:
                        new_pay = i * raise_value
                    counter += 1
                hourly_worker[name] = (temp_position, new_pay)
                print("{} has successfully been given a raise to {} an hour!".format(name, new_pay))
            elif type_of_pay == "manager":
                for i in manager[name]:
                    if counter == 1:
                        temp_position = i
                    elif counter == 2:
                        new_pay = i * raise_value
                    counter += 1
                manager[name] = (temp_position, new_pay)
                print("{} has successfully been given a raise to {} an hour!".format(name, new_pay))
        except KeyError:
            print("This employee does not exist")

        """
        Takes the user back to the main menu once they press any button
        """

        input("\n\nPress any button to go back to the main menu...")
        main_menu(username)

    """
    Function to fire an employee
    """

    def fire_employee(self):

        """
        Clears the screen
        """

        os.system('cls')

        """
        Asks if the employee is hourly, salary or a manager
        """

        type_of_pay = input("Is this employee hourly, salary or a manager?: ")

        """
        Based on the answer above, will show all the employees in that title
        """

        while True:
            print("\n")
            if type_of_pay == "hourly":
                for names in hourly_worker.keys():
                    if names != "FIRSTNAME LASTNAME":
                        print(names)
                break
            elif type_of_pay == "salary":
                for names in salary_worker.keys():
                    if names != "FIRSTNAME LASTNAME":
                        print(names)
                break
            elif type_of_pay == "manager":
                for names in manager.keys():
                    if names != "FIRSTNAME LASTNAME":
                        print(names)
                break
            else:
                type_of_pay = input("incorrect entry. Please type salary or hourly: ")

        """
        Asks which person you would like to fire and confirms it before
        continuing
        """

        name = input("\nEnter the employee you would like to fire: ").upper()
        confirm = input("Are you sure? (yes/no)")

        if confirm == "no":
            main_menu(username)

        """
        Will find the user in the accounts and titled position dictionaries
        and remove them from the list. Will update the accounts file when
        the user exists the program.
        """

        try:
            if type_of_pay == "salary":
                try:
                    for key, value in salary_worker.items():
                        if key == name:
                            del accounts[value[2]]
                    del salary_worker[name]
                except KeyError:
                    print("That employee does not exist")
                else:
                    print(name + " has been removed")
            elif type_of_pay == "hourly":
                try:
                    for key, value in hourly_worker.items():
                        if key == name:
                            del accounts[value[2]]
                    del hourly_worker[name]
                except KeyError:
                    print("That employee does not exist")
                else:
                    print(name + " has been removed")
            elif type_of_pay == "manager":
                try:
                    for key, value in manager.items():
                        if key == name:
                            del accounts[value[2]]
                    del manager[name]
                except KeyError:
                    print("That employee does not exist")
                else:
                    print(name + " has been removed")
        except KeyError:
            print("This employee does not exist")

        """
        Takes the user back to the main menu once they press any button
        """

        input("\n\nPress any button to go back to the main menu...")
        main_menu(username)

    """
    Function to hire an employee
    """

    def hire_employee(self):

        """
        Clears the screen
        """
        os.system('cls')

        """
        Asks for the new hire's information and confirming with the user
        """

        user = input("Please enter the new employee's username: ")
        password = getpass.getpass("Please enter the new employee's password: ")
        title = input("Please enter the new employee's role: (Hourly, Salary, Manager)")
        name = input("Please enter his/her full name: ").upper()
        position = input("Please enter his/her position: ")
        pay = input("Please enter the employee's pay rate: ")
        full_name = name.split(" ")

        confirm = input("Are you sure? (yes/no)")

        if confirm == "no":
            main_menu(username)

        """
        Will create the user with the information above in the running memory
        """

        if title.capitalize() == "Salary":
            SalaryEmployee(full_name[0], full_name[1], position, user, int(pay))
            print(name.upper() + " has been successfully added!")
        elif title.capitalize() == "Hourly":
            HourlyEmployee(full_name[0], full_name[1], position, user, int(pay))
            print(name.upper() + " has been successfully added!")
        elif title.capitalize() == "Manager":
            Manager(full_name[0], full_name[1], position, user, int(pay))
            print(name.upper() + " has been successfully added!")
        else:
            print("invalid entry, please try again...")
            main_menu(username)

        """
        Will add the user to the accounts dictionary, which is used to add it to 
        the accounts text file
        """

        accounts[user] = (password, title.capitalize(), full_name[0], full_name[1], position, int(pay))

        """
        Takes the user back to the main menu once they press any button
        """

        input("\n\nPress any button to go back to the main menu...")
        main_menu(username)


"""
Function to initialize the system variables and class objects
"""


def initialize_accounts():

    """
    Initializes the first entry in each class
    """
    global hourly_example, salary_example, manager_example, executive_example
    hourly_example = HourlyEmployee("firstname", "lastname", "position", "user", "Hourly")
    salary_example = SalaryEmployee("firstname", "lastname", "position", "user", "Salary")
    manager_example = Manager("firstname", "lastname", "position", "user", "Salary")
    executive_example = Executive("firstname", "lastname", "position", "user", "Salary")

    """
    Opens the accounts document to read through the lines and save the entries to 
    the running memory
    """

    f = open("accounts.txt", 'r')
    lines = f.readlines()
    f.close()

    """
    Goes through each line in the text file and saves each entry to the accounts dictionary.
    It then adds the class object depending on the title of the user
    """

    for i in lines:
        entry = i.split("/")
        accounts[entry[0]] = (entry[1], entry[2], entry[3], entry[4], entry[5], entry[6].strip("\n"))
        if entry[2] == "Executive":
            Executive(entry[3], entry[4], entry[5], entry[0], float(entry[6]))
        elif entry[2] == "Manager":
            Manager(entry[3], entry[4], entry[5], entry[0], float(entry[6]))
        elif entry[2] == "Hourly":
            HourlyEmployee(entry[3], entry[4], entry[5], entry[0], float(entry[6]))
        elif entry[2] == "Salary":
            SalaryEmployee(entry[3], entry[4], entry[5], entry[0], float(entry[6]))


"""
Function to save the current users in running memory to the accounts text file 
and exits the program
"""


def exit_program():
    f = open("accounts.txt", 'w')
    for key, values in accounts.items():
        f.write("{}/{}/{}/{}/{}/{}/{}\n".format(key, *values))
    f.close()
    print("Have a great day!")
    time.sleep(2)
    sys.exit()


"""
Function that defines the login sequence of the program
"""


def login():

    """
    Clears the screen and initializes variable
    """

    os.system('cls')
    global username
    counter = 0

    """
    Creates a loop that continues running until a correct combination is entered
    or too many incorrect attempts in which case the program will exit
    """

    while True:
        if counter > 2:
            print("You have entered too many incorrect attempts. Exiting...")
            exit_program()
            
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        """
        Will go through all the entries in the system and check if the username
        and password combination match. If so it will create an instance of 
        the employee object based on the title of the employee. If not it will
        inform the user the combination was wrong and add 1 "strike". After 3 
        strikes the user will be exited from the program.
        """

        for i in accounts:
            try:
                if password in accounts[username]:
                    if i[2] == "Executive":
                        Executive(i[3], i[4], i[5], i[0], i[6])
                    elif i[2] == "Manager":
                        Manager(i[3], i[4], i[5], i[0], i[6])
                    elif i[2] == "Salary":
                        SalaryEmployee(i[3], i[4], i[5], i[0], i[6])
                    elif i[2] == "Hourly":
                        HourlyEmployee(i[3], i[4], i[5], i[0], i[6])
                    return username
                else:    
                        print("Your username or password is incorrect. Please try again")
                        counter += 1
                        break
            except KeyError:
                print("Your username or password is incorrect. Please try again")
                counter += 1
                break


"""
Function for the main menu that is being shown for the user
"""


def main_menu(username):

    """
    Clears the screen and displays all the available options to the user
    """

    os.system('cls')
    print("******Bank Employee Manager******\n\n\n\n")
    print("1) View all employees")
    print("2) Hire new employee")
    print("3) Fire employee")
    print("4) Give employee raise")
    print("5) Exit")

    """
    Puts user in an endless loop to make a choice. Will call the specific
    function depending on the choice of the user. It will keep running until
    option 5 is selected (exit program) or user manually exits program. 
    """

    while True:
        choice = input("\nEnter your choice here: ")
        if choice == '1':
            view_employees()
        elif choice == '2':
            if 'Manager' in accounts[username]:
                manager_example.hire_employee()
            elif 'Executive' in accounts[username]:
                executive_example.hire_employee()
            else:
                hourly_example.hire_employee()
        elif choice == '3':
            if 'Manager' in accounts[username]:
                manager_example.fire_employee()
            elif 'Executive' in accounts[username]:
                executive_example.fire_employee()
            else:
                hourly_example.fire_employee()
        elif choice == '4':
            if 'Manager' in accounts[username]:
                manager_example.give_raise()
            elif 'Executive' in accounts[username]:
                executive_example.give_raise()
            else:
                hourly_example.give_raise()
        elif choice == '5':
            exit_program()
        else:
            print("invalid choice, please try again")


"""
Function that allows the user to view all the employees, their position
and their salary. 
"""


def view_employees():
    os.system('cls')

    print("*" * 16 + "Executives" + "*" * 16)
    for key, value in executive.items():
        name = key.split(" ")
        print(template.format(name[0], name[1], value[0], value[1]))
        
    print("\n" + "*" * 16 + "Managers" + "*" * 16)
    for key, value in manager.items():
        name = key.split(" ")
        print(template.format(name[0], name[1], value[0], value[1]))
        
    print("\n" + "*" * 16 + "Salary workers" + "*" * 16)
    for key, value in salary_worker.items():
        name = key.split(" ")
        print(template.format(name[0], name[1], value[0], value[1]))
        
    print("\n" + "*" * 16 + "Hourly workers" + "*" * 16)
    for key, value in hourly_worker.items():
        name = key.split(" ")
        print(template.format(name[0], name[1], value[0], value[1]))

    input("\n\nPress any button to go back to the main menu...")
    main_menu(username)


"""
Main running program that will call the initialization and main_menu functions
"""

if __name__ == '__main__':
    initialize_accounts()
    main_menu(login())
