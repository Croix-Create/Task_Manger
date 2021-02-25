### Task_Manger
A simple task manager application that essentially allows a user to manage and create tasks. This application was coded in Python.
User login:
username: admin
password: adm1n

## The Objective
The objective of this capstone project was to create a functional task manager application. The requirements of the project included effectively creating functions that make use of I/O operations.
This means displaying information for the user in an easy to read manner as well as creating tasks and user IDs that are stored in a file and read by the program in response to certain user inputs.

## The How

# Functions

# reg_user

The function reg_user is called when the user selects the register user option in the main menu. It is designed to request a password and username form the user, after the initial
inputs are recieved by the program the user will be asked to confirm the username and password. If the usernames and passwords match the username and password will be written to "user.txt".
If they do not match an error messagee will be displayed. If the confirmation is a success a message will be displayed in the console saying it was a success.

# add_task

The program will request data from the user and save the data by creating a task entry in a txt file called tasks.

# view_all

view_all iterates through the "tasks.txt" where the index lines are split by ", " and dispalys the appropriate information in the terminal.

# edit_task

edit_task declares a list, and requests inputs from the user. The list edit_list is assigned the value of stripped and split (, ) data read from the "tasks.txt" file.
This allows for the replacement of specific indexes of data.
If 1 is entered the program will change the user who is assigned to that specific task.
If 2 is entered this will tick the selected task off as completed. If 3 is entered this will will changed the date to the newly requested date.

##  Main Loop
The program runs with a while loop that continously asks for login details, if the login is correct login = True and the program will present the user with a menu.
There are options for:
  * registering users
  * adding tasks
  * viewing tasks
  * viewing user specific tasks
  * generating reports in text files
  * displaying statistics in the terminal
