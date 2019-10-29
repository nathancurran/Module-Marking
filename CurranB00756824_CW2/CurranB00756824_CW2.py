# This function contains the main program
def main():
    # Set the value of the index
    index_num = 0

    # Display the menu
    print('-----------Menu-----------')
    print('1. Display number of records loaded.')
    print('2. Display employee list.')
    print('3. Display the total salary bill.')
    print('4. Display the average salary bill.')
    print('5. Add employee.')
    print('6. Display the number of employees sorted by position.')
    print('7. Show list of employees earning above a salary threshold.')
    print('8. Search the file.')
    print('9. Exit program.')
    print()

    # While loop to get user input for menu
    while index_num != 9:
        # Display number of records loaded
        if index_num == 1:
            # Output the result
            print('The number of records loaded was ', total_records, '.', sep='')
            print()

        # Display employee list
        elif index_num == 2:
            print('Employee List')
            print('-' * 40)

            # Call the display_emp function
            display_emp(employee_list)
            print()

        # Display the total salary bill
        elif index_num == 3:
            print('The total salary bill is £', format(total_sal, ',.2f'), sep='')
            print()

        # Display the average salary bill
        elif index_num == 4:
            # Outputs the average salary
            print('The average salary bill is £', average_salary(), sep='')
            print()

        # Add employee
        elif index_num == 5:
            # Call the add_emp function
            add_emp()
            print()

        # Display the number of employees sorted by position
        elif index_num == 6:
            # Call the count_by_pos function
            count_by_pos(employee_list)
            print()

        # Show list of employees earning above the entered salary
        elif index_num == 7:
            # Call the salary_threshold function
            salary_threshold(employee_list)
            print()

        elif index_num == 8:
            # Call the search_record function
            search_record(employee_list)
            print()

        # Exception handling for index
        try:
            # Get user input
            index_num = int(input('Select a number: '))
            # Integer input validation
            if index_num not in range(1, 10):
                print('Please enter a number between 1 and 9.')
                print()
        except ValueError:
            print('Error: Input must be integer.')
            print()


# Read the text-file and returns the data as a list
def read_file():
    try:
        # Open the text-file
        infile = open('CW2_EMP_DATASET.txt', 'r')
        file_contents = infile.readlines()
        infile.close()
    # Output error
    except IOError as error:
        print(error)
    # Output text from text-file
    return file_contents


# Save the list created in the read_file
# function as employee_list
employee_list = read_file()


# This function determines the start position for the
# program to read the data in the text-file
def search_header(emp_list):
    # Initialise the counter
    start_pos = 0

    # Counts the number of lines starting with a #
    # sets start_pos to skip the header(s)
    for element in emp_list:
        if element.startswith('#'):
            start_pos += 1

    # Return the start_pos to be called later
    return start_pos


# Sets the variable start equal to the start position
# for the program to read from within the text-file
start = search_header(employee_list)


# This function prints the data from the text-file
def display_emp(emp_list):
    # Loop through text-file ignoring the header
    for element in emp_list[start:]:
        print(element.strip())


# This function calculates the total salary of every
# employee
def sum_salary(emp_list):
    # Initialise a starting value for total_salary
    # variable
    total_salary = 0.00
    for element in emp_list[start:]:
        # Split the data
        emp_no, emp_name, age, position, salary, yrs_emp = element.strip().split(',')
        # Add the current salary to the total_salary
        total_salary += int(salary)
    return total_salary


# Set the total_sal variable equal to the total
# salary to be called later
total_sal = sum_salary(employee_list)


# This function calculates the average salary
def average_salary():
    # Call the total_salary value from the sum_salary
    # function and use it to calculate average salary
    avg_salary = total_sal / total_records
    # Outputs average salary formatted to 2dp
    return format(avg_salary, ',.2f')


# This function adds a new employee record
def add_emp():
    # Open the text-file to append
    outfile = open('CW2_EMP_DATASET.txt', 'a')

    # Generates the next employee number
    emp_no = '0' + str(total_records + 1)

    # Gets user first name
    first_name = str(input("Enter the employee's first name: "))

    # Validates first name
    while first_name.isalpha() is False:
        print("The employee's name must contain only characters.")
        first_name = str(input("Enter the employee's first name: "))

    # Gets user surname
    surname = str(input("Enter the employee's surname: "))

    # Validates surname
    while surname.isalpha() is False:
        print("The employee's name must contain only characters.")
        surname = str(input("Enter the employee's surname: "))

    # Joins first and last name
    emp_name = first_name + ' ' + surname

    # Gets employee's age
    age = input("Enter the employee's age: ")

    # Validates age is int
    while age.isdigit() is False:
        print('The employee age must be an integer.')
        age = input("Enter the employee's age: ")

    # Validates that the age is greater than 0
    # and less than 100
    age = int(age)
    while age <= 0 or age > 100:
        print('Please enter a valid age.')
        age = int(input("Enter the employee's age: "))

    # Gets employee's position
    position = str(input("Enter the employee's position: "))

    # Validation for position
    while position not in ['Developer', 'DevOps', 'Analyst', 'Tester']:
        print("The employee's position must be one of the following:")
        print('[Developer, DevOps, Analyst, Tester]')
        position = str(input("Enter the employee's position: "))

    # Gets employee's salary
    salary = input("Enter the employee's salary: £")

    # Validates salary is int
    while salary.isdigit() is False:
        print('The employee salary must be an integer.')
        salary = input("Enter the employee's salary: £")

    # Gets the number of years employed
    yrs_emp = input("Enter the number of years employed: ")

    # Validates yrs_emp is int
    while yrs_emp.isdigit() is False:
        print('The years employed must be an integer.')
        yrs_emp = input("Enter the number of years employed: ")

    # Write the data into the file
    outfile.write(emp_no + ', ' + emp_name + ', ' + str(age) + ', ' +
                  position + ', ' + str(salary) + ', ' + str(yrs_emp)
                  + '\n')
    # Confirmation message
    print('Employee has been added.')


# This function counts the employees by position
def count_by_pos(emp_list):
    # Initialise count variables
    developer_count = 0
    devops_count = 0
    tester_count = 0
    analyst_count = 0

    # Loop through text-file ignoring the header
    for element in emp_list[start:]:
        # Split the data in the line
        emp_no, emp_name, age, position, salary, yrs_emp = element.strip().split(', ')

        # Get position and adds 1 to corresponding counter
        if position == 'Developer':
            developer_count += 1
        elif position == 'DevOps':
            devops_count += 1
        elif position == 'Tester':
            tester_count += 1
        else:
            analyst_count += 1

    # Output the data
    print('Position\t No. of employees')
    print('-' * 30)
    print('Developer \t', developer_count)
    print('DevOps \t \t', devops_count)
    print('Tester \t \t', tester_count)
    print('Analyst \t', analyst_count)


# This function displays a list of employees earning above
# the inputted salary
def salary_threshold(emp_list):
    sal_thresh = int(input('Enter a salary threshold: £'))
    print('The employees shown below earn above £', sal_thresh, sep='')
    # Loop through text-file ignoring the header
    for element in emp_list[start:]:
        # Split the data in the line
        emp_no, emp_name, age, position, salary, yrs_emp = element.strip().split(', ')
        # Set parameters for output
        if int(salary) > sal_thresh:
            print(emp_name, ': £', salary, sep='')


def search_record(emp_list):
    # Get the search value
    search = str(input('Enter the data that you would like to search for: '))

    # Initialise the counter
    occ_found = 0

    # Counts the number of line starting with a #
    # sets start_pos to skip the header(s)
    for element in emp_list[start:]:
        # If the data is found, print the records
        # and add 1 to the counter variable
        if element.find(search) != -1:
            print(element.strip())
            occ_found += 1

    # Outputs the number of occurrences found
    print('\n', occ_found, ' occurrence(s) were found.', sep='')


# Saves the number of records as a variable
total_records = len(employee_list) - start

# Call the search_header function to find the start position
# when reading from the list
search_header(employee_list)

# Call the main function
main()
