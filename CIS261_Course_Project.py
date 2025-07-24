#Michael Santayana
#CIS261
#Course Project Phase 1

def EnterEmployeeName(): # Function to enter employee name
    name = input("Please enter the employee's Name with no Spaces: ")
    print(f"Employee name entered: {name}") #initial input
    # Validate the name input ----------------------------------------------------------
    if not name.strip():
        print("Name cannot be empty. Please enter a valid name.")
        return EnterEmployeeName()
    if not name.isalpha():
        print("Name must contain only alphabetic characters. Please enter a valid name.")
        return EnterEmployeeName()
    else:  
        return name

def TotalHours(): # Function to enter total hours worked
    hours = input("Please enter the total hours worked in a week: ") #initial input
    # Validate the name input ----------------------------------------------------------
    # check if it is a valid interger value
    while not hours.strip():
        print("Input cannot be empty. Please enter the total hours worked.")
        hours = input("Please enter the total hours worked: ")
    if not hours.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter a numeric value for hours.")
        return TotalHours()
    if float(hours) <= 0:
        print("Hours cannot be negative. Please enter a valid number of hours.")
        return TotalHours()
    if float(hours) > 168:
        print("Hours cannot exceed 168 in a week. Please enter a valid number of hours.")
        return TotalHours()
    # check if it is even a interger value at all
    try:
        hours = float(hours)
        print(f"Total hours worked: {hours}")
        return hours
    except ValueError:
        print("Invalid input. Please enter a numeric value for hours.")
        return TotalHours()

def inputHourlyRate(): #function to enter hourly rate
    rate = input("Please enter the hourly rate: ")
    print(f"Hourly rate entered: {rate}") #initial input
    # Validate the hourly rate input ----------------------------------------------------------
    while not rate.strip():
        print("Input cannot be empty. Please enter the hourly rate.")
        rate = input("Please enter the hourly rate: ")
        return inputHourlyRate()
    if not rate.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter a numeric value for the hourly rate.")
        return inputHourlyRate()
    if float(rate) <= 0:
        print("Hourly rate cannot be negative or zero. Please enter a valid hourly rate.")
        return inputHourlyRate()    
    if float(rate) > 1000:
        print("Hourly rate cannot exceed $1000. Please enter a valid hourly rate.")
        return inputHourlyRate()
    
    try:
        rate = float(rate)
        print(f"Hourly rate confirmed: ${rate:.2f}")
        return rate
    except ValueError:
        print("Invalid input. Please enter a numeric value for the hourly rate.")

def InputIncomeTaxRate(): # Function to enter income tax rate
    tax_rate = input("Please enter the income tax rate (as a percentage): ")
    print(f"Income tax rate entered: {tax_rate}") #initial input
    # Validate the income tax rate input ----------------------------------------------------------
    while not tax_rate.strip():
        print("Input cannot be empty. Please enter the income tax rate.")
        tax_rate = input("Please enter the income tax rate (as a percentage): ")
    if not tax_rate.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter a numeric value for the income tax rate.")
    if float(tax_rate) < 0:
        print("Income tax rate cannot be negative. Please enter a valid income tax rate.")
    if float(tax_rate) >= 101:
        print("Income tax rate cannot exceed 100%. Please enter a valid income tax rate.")
    
    try:
        tax_rate = float(tax_rate) / 100  # Convert percentage to decimal
        print(f"Income tax rate confirmed: {tax_rate:.2%}")
        return tax_rate
    except ValueError:
        print("Invalid input. Please enter a numeric value for the income tax rate.")
        return InputIncomeTaxRate()

def calculateGrossPay(hours, rate):
    gross_pay = hours * rate 
    print(f"Gross pay calculated: {gross_pay}")
    return gross_pay

def calculateNetPay(gross_pay, tax_rate):
    net_pay = gross_pay * (1 - tax_rate)
    print(f"Net pay calculated: {net_pay}")
    return net_pay

def displayPayDetails(name, hours, rate, gross_pay, net_pay):
    print("\n--- Pay Details ---")
    print(f"Employee Name: {name}")
    print(f"Total Hours Worked: {hours}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Net Pay (after tax): ${net_pay:.2f}")

def NumberOfEmployees():
    while True:
        try:
            num_employees = int(input("Please enter the number of employees: "))
            if num_employees <= 0:
                print("Number of employees must be a positive integer. Please try again.")
            else:
                return num_employees
        except ValueError:
            print("Invalid input. Please enter a valid integer for the number of employees.")

def main():
    print("Welcome to the CIS261 Course Project Phase 1!")
    print("$$$$$$$$$$$$$$$$$$$MONEY$$$$$$$$$$$$$$$$$$$$$$$$")
    print("This program will help you calculate employee pay details.\n")
    print("$$$$$$$$$$$$$$$$$$$MONEY$$$$$$$$$$$$$$$$$$$$$$$$")
    employees = []  # List to store employee data
    num_employees = NumberOfEmployees()  # Get the number of employees to process
    print(f"Number of employees to process: {num_employees}\n")
    while len(employees) < num_employees:
        try:
            print(f"\nProcessing employee #{len(employees) + 1} of {num_employees}...")
            if input("Type 'END' to terminate the program or press Enter to continue inserting employees: ").strip().lower() == 'end':
                print("Exiting the program as per user request.")
                break
            else:
                print("Continuing with the inserting employees...")  # Call the functions to get employee details and calculate pay
                E = EnterEmployeeName()
                H = TotalHours()
                R = inputHourlyRate()
                T = InputIncomeTaxRate()
                G = calculateGrossPay(H, R)
                N = calculateNetPay(G, T)
                
            employee_data = {  # Store employee data in a dictionary
                'Name': E,'Hours': H,'Rate': R,'TaxRate': T,'GrossPay': G,'NetPay': N }
            
            employees.append(employee_data)
        
            print("\nAll employee entries complete. Summary:") # Display summary of all employees
            for i, emp in enumerate(employees, start=1):
                print(f"\nEmployee #{i}:")
                displayPayDetails(emp['Name'], emp['Hours'], emp['Rate'], emp['GrossPay'], emp['NetPay'])
                
            print("\nAll employee entries complete. Summary:") # Display summary of all employees
            print(f"Total number of employees processed: {len(employees)}")

        except Exception as e:   # Catch any unexpected errors
            print(f"An error occurred: {e}")
            print("An error occurred. Please try again.")
            print("if this error persists, please contact me at blblbas@email.com for support.")
            print("include the error message in your email.")
            continue

main()