import datetime

    # This function will register new users for the task_manager program!
def reg_user():
        # The username and passowords have to match, else the program will tell them the  new_user1, new_passw1 didn't match with new_user2 and new_passw2
        new_user1 = input("Please enter a new username:\n")
        new_passw1 = input("Please enter a new password:\n")
        user_file = open("user.txt", 'r+')
        for line in user_file:
            linestrings = line.split(', ')
            # This code will insure that if a username is taken the user of the program will be requested to choose a different username.
            if new_user1 in linestrings[0]:
                while new_user1 in linestrings[0]:
                    new_user1 = input("This user is taken. Please select a new username: \n")
        new_user2 = input("Please confirm your username: \n")
        new_passw2 = input("Please confirm your password: \n")
        # User 1 is equal to new_user1 + ', ' + new_passw1.
        user_pass1 = new_user1 + ', ' + new_passw1
        # User 2 is equal to new_user2 + ', ' + new_passw2.
        user_pass2 = new_user2 + ', ' + new_passw2
        if user_pass1 == user_pass2:
            user_write = open('user.txt', 'a+')
            # Write the new user and password to user.txt.
            user_write.write(f"\n{user_pass2}")
            user_write.seek(0)
            user_write.close()
            print("Success: You've created a new user!")
        else:
            print("Usernames or passowrds don't match!")


def add_task():
    assigned_to = input("Enter the name of the user responsible for the task:")
    task_title = input("Enter the name of the task:")
    descript = input("Please enter a description of the task:")
    start_date = input("Enter the start date:")
    end_date = input("Enter the end date e.g D/M/Y")
    completed = input("Is the task completed? Yes or No?")
    with open('tasks.txt', 'a+') as task_file:
    # Once the variables have been assigned with the apropriate data, the programme will write the data to the tasks.txt file
        task_file.write(f"\n{assigned_to}, {task_title}, {descript}, {start_date}, {end_date}, {completed}")
        task_file.close()


def view_all():
    # Displays the information from all tassks to the user in an easy to read manner
    task_file = open("tasks.txt", 'r')
    for line in task_file:
        # For line  in task_file strip "\n" from line
        line = line.strip("\n")
        # print_line equals every line split apart by ", "
        print_line = line.split(", ")
        # Print this in an easy to ready manner so it's user-friendly
        print(f'''Assigned to: {print_line[0]}
Task: {print_line[1]}
Description: {print_line[2]}
Start date: {print_line[3]}
End date: {print_line[4]}''')

    # This function is designed to edit the tasks viewed in the view_mine function
def edit_task():
    edit_list = []
    num_choice = int(input("Enter the task number of a task to edit existing tasks OR enter -1 to go back to menu:"))
    num_choice -= 1

    if num_choice != -1:

        change_status = input("Enter 1 to change user, enter 2 to tick the task completed and 3 to change the deadline.")
        if (change_status == "1"):
            with open('tasks.txt', 'r+') as task_file:
                # For every line in edit_list the line will be stripped and split and the data from the tasks.txt will be read into memory.
                edit_list = [i.strip().split(", ")for i in task_file.readlines()]

                # If the task is complete the user will get a error message that the task must be marked incomplete in orcer to edit the file
                if edit_list[num_choice][5] == "Yes":
                    print("The task has to be marked incomplete.")

                # If the task is incomplete a new username will be requested.
                elif edit_list[num_choice][5] == "No":
                    new_username = input("Enter a new username: ")
                    old_username = edit_list[num_choice][0]
                    # The new username is assigned the positon of the old username.
                    edit_list[num_choice][0] = new_username
                    with open('tasks.txt', 'w') as task_file:
                        # In order to write the new username to the file we must join the stripped and split data.
                        task_file.write("\n".join((', '.join(str(x) for x in item)) for item in edit_list))
                        print("User changed!")

        # If change status == 2 the user will be able to mark a task complete.
        if (change_status == "2"):
            with open('tasks.txt', 'r+') as task_file:
                edit_list = [i.strip().split(", ")for i in task_file.readlines()]

                # If the task is already complete the program will inform them.
                if edit_list[num_choice][5] == "Yes":
                    print("The task is already complete.")

                # This will change the "No" in edit_list to a "Yes" thus marking the task complete.
                elif edit_list[num_choice][5] == "No":
                    complete_str = "Yes"
                    incomplete_str = edit_list[num_choice][5]
                    # "Yes" is assigned to "No's" old position.
                    edit_list[num_choice][5] = complete_str
                    with open('tasks.txt', 'w') as task_file:
                        # The data is then joined back together again.
                        task_file.write("\n".join((', '.join(str(x) for x in item)) for item in edit_list))
                        print("The task has been ticked complete.")

        # If change status == 3 the user will be able to edit the deadline of the task.
        if (change_status == "3"):
            with open('tasks.txt', 'r+') as task_file:
                edit_list = [i.strip().split(", ")for i in task_file.readlines()]

                if edit_list[num_choice][5] == "Yes":
                    print("The task is already complete.")

                # The program will request a new dat efrom the user.
                elif edit_list[num_choice][5] == "No":
                    new_date = input("Please enter a new date e.g D/M/Y: ")
                    old_date = edit_list[num_choice][4]
                    # The old date's postion is swapped with the new date and the deadline is updated.
                    edit_list[num_choice][4] = new_date
                    with open("tasks.txt", 'w') as task_file:
                        # Write the data to the file after joining the data back together.
                        task_file.write("\n".join((', '.join(str(x) for x in item)) for item in edit_list))
                        print("Deadline updated.")
        # If the task number that is equal to num_choice doesn't exist in the file the user will recieve an error message.
        if num_choice > len(edit_list):
            print("This task does not exist!")

    # This function spawns all the task file data specific to the user, through the function edit_task() one can edit this data.
def view_mine():
    task_list = []
    counter = 0
    task_file = open("tasks.txt", 'r+')
    for line in task_file:
        counter += 1
        line = line.strip("\n")
        print_line = line.split(", ")
        if username == print_line[0]:
            task_list.append(line)
            print(f''' Task number: {counter}
            Assigned to: {print_line[0]}
            Task: {print_line[1]}
            Description: {print_line[2]}
            Start date: {print_line[3]}
            End date: {print_line[4]}
            Completed: {print_line[5]}''')
    edit_task()


    
    
    # Opens user_file so that the program can read the lines of the file.
user_file = open("user.txt", 'r+', encoding="utf-8")
login = False
    # While login credentials are incorrect the programme will ask for a username and password.
while login == False:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

        # This loop creates the variables valid_user and valid_passowrd and takes the data before and after the comma in the file as thier values. 
    for line in user_file:
        valid_user, valid_password = line.strip().split(", ")
            # If the user and password are matched up with variables valid_user and valid_password login will be True
        if username == valid_user and password == valid_password:
            login = True
        # Resets the offset in the file back to the beginning
    user_file.seek(0)
    if login == False:
        print("Incorrect details! Please enter a valid user and password.")

        # While login is true a menu will show up for the user to select options.
while login == True:

        # If the user is an admin an extra option (s - statistics) will be available.
    task_file = open("tasks.txt", "a")
    if username == "admin" and password == "adm1n":
        choice = input('''
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks
    gr - generate reports
    ds - display statistics
    e - exit                                                                                          
    ''')
    else:
        choice = input('''
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
        ''')

        # If the user is an admin he or she will be able to create a new user.
    if choice == "r" and username == "admin" and password == "adm1n":
          reg_user()

        # If choice == "a" the programme will request the admin to enter in the necessary task data
    elif choice == "a":
        add_task()

        # If the user selects va the programme will read from task_file and present data in an easy to read manner.
    elif choice == "va":
        view_all()
 
        # Displays the information from the currently logged in user's tasks in an easy to read manner
    if choice == "vm":
        view_mine()

        # If the admin selects s, special statistics will be printed for them
    if choice == "ds":
        task_file = open("tasks.txt", 'r')
        count = 0
            # For every line in task_file the programme will add one to count
        for task in task_file:
            count += 1
            # Printing an f-string that has a dynamic count of the amount of tasks
        print(f"The amount of tasks: {count}")
        user_file = open("user.txt", 'r')
        i = 0
            # For every line in task_file the programme will add one to count
        for line in user_file:
            i += 1
            # Printing an f-string that has a dynamic count of the amount of tasks
        print(f"The amount of users: {i}")
        # If the user selects e the prgoramme will close both files and break from the loop
        task_file.close()

        # gr will generate reports for the user's progress and information about the status of tasks overall.
    if choice == "gr":
        complete_counter = 0
        incomplete_counter = 0
        task_counter = 0
        overdue_counter = 0
        username_counter = 0
        incomplete_user_task = 0
        incomplete_overdue = 0
        complete_user_task = 0

        with open("tasks.txt", 'r') as task_file:
            task_lines = task_file.readlines()


        for task in task_lines:
            task_counter += 1

        # This loop will count different aspects of the file 'tasks.txt' and use these counts to generate percentages and figures.
        for line in task_lines:
            indexes = line.strip().lower().split(', ')
            if indexes[5] == "yes" or indexes[5] == "yes\n":
                complete_counter += 1
        
            if indexes[5] == "no" or indexes[5] == "no\n":
                incomplete_counter += 1

            # assigning the date from the tasks file to date_string.
            date_string = indexes[4]

            # This represents the deadline for the tasks in the file.
            completion_date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
            
            # so as to compare the deadline with the current date date_today is assigned with the present date.
            date_today = datetime.datetime.today()
           
            # This counts wether or not a task is overdue and adds 1 for every task that is overdue
            if date_today > completion_date and indexes[5] == "no":
                overdue_counter += 1

                # This calculation works out the percentage of overdue tasks in the task file.
            percentage_overdue = float(overdue_counter / task_counter * 100)
                
                # This works out the percentage of incomplete tasks.
            perctenage_incomplete = float(incomplete_counter / task_counter * 100)
                
                # This counter adds one for every task assigned to the currently logged in user
            if username == indexes[0]:
                username_counter += 1
               
                # This counter adds one whenever a user's task is incomplete.
            if username == indexes[0] and indexes[5] == "no":
                incomplete_user_task += 1
               
                # This counter adds one whenever a user's task is complete.
            if username == indexes[0] and indexes[5] == "yes":
                complete_user_task += 1
               
                # This counter adds one whenever a user's task is incomplete and overdue.
            if username == indexes[0] and indexes[5] == "no" and date_today > completion_date:
                incomplete_overdue += 1
            
            # This tabulates the percentage of tasks assigned to the user
            percentage_user = float(username_counter / task_counter * 100)
           
            # This calculates the percentage of incomplete tasks of the user
            incompleted_percentage = float(incomplete_user_task / username_counter * 100)
            
            # This calculates the percentage of incomplete and overdue tasks for the user
            percent_incomplete_overdue = float( 100 / username_counter * incomplete_overdue)
            
            # This calculates the total tasks that completed by the user
            percent_complete = float(complete_user_task / username_counter  * 100)
        
        # Writing the results to the file task_overview.
        task_over = open("task_overview.txt", "a+", encoding="utf-8")
        
        task_over.write(f'''The total number of tasks: {task_counter}
The total number of completed tasks: {complete_counter}
The total number of incomplete tasks: {incomplete_counter}
The total number of tasks that are incomplete and that are overdue: {overdue_counter}
The percentage of tasks that are incomplete: {perctenage_incomplete}%
The percentage of tasks that are overdue:{percentage_overdue}%
        ''')
        task_over.close()

        # Writing the results to the file user_overview
        user_over = open("user_overview.txt", "a+")

        user_over.write(f'''The total number of tasks assigned to {username}: {username_counter}
The percetange of tasks assigned to {username}: {percentage_user}%
The percentage of tasks completed by {username}: {percent_complete}%
The percentage of tasks assigned to {username} that are incomplete: {incompleted_percentage}%
The percentage of tasks pending completion and are overdue: {percent_incomplete_overdue}%
        ''')
        user_over.close()
        print("Reports generated!")
#The End
