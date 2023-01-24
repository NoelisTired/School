import csv, datetime, time, os

class Functions:
    """
    ?    It takes the csv file and puts it in a list of dictionaries. It also creates a list of functions that can be used. Global variables but nicer.
    """
    def __init__(self):
        self.file = csv.DictReader(open('VW.csv', 'r', encoding="UTF-8"), delimiter=';')
        pass
    

    """
    ?    It takes the file, and then it takes the column 'Salaris_bruto' and puts it in a list. Then it sums
    ?    all the values in the list and divides it by the length of the list
    ?    :return: The average salary of all employees.
    """
    @staticmethod
    def avgsalary():
        allsal = [int(i) for i in [row['Salaris_bruto'] for row in Functions().file]] # list comprehension
        sal = sum(allsal) / len(allsal)
        return[f"${sal}", f"${sal*0.79}"]
    
    """
    ?    It returns a list of all the first names of the people in the department that is passed as an
    ?    argument
        
    ?    :param department: The department you want to get the members of
    ?    :return: A list of all the first names of the people who work in the department that is given as an
    ?    argument.
    """
    @staticmethod
    def departmentMembers(department):
        return [row['Voornaam'] for row in Functions().file if row['Functie'] == department]

    """
    ?    It returns a list of first names of people who have a job that matches the job parameter and are in
    ?    one of the departments in the departments parameter
        
    ?    :param departmens: a list of departments
    ?    :param job: the job title
    ?    :return: A list of names of people who have the job and are in the department.
    """
    @staticmethod
    def advDepartmentFunctions(departmens, job):
        return [row['Voornaam'] for row in Functions().file if row['Functie'] == job and row['Afdeling'] in departmens]

    """
    ?    It takes a department name as an argument, and returns the average salary of that department
        
    ?    :param department: the department you want to get the average salary of
    ?    :return: The average salary of the department.
    """
    @staticmethod
    def departmentsalary(department):
        allsal = [int(i) for i in [row['Salaris_bruto'] for row in Functions().file if row['Functie'] == department]] # list comprehension
        sal = sum(allsal) / len(allsal)
        return("Gross Income:",f"${sal}","With Taxes", f"${sal*0.79}")

    """
    ?    It returns a list of all the first names of people who are 68 or older
    ?    :return: A list of names of people who are 68 or older.
    """
    @staticmethod
    def retireAlert():
        #! Ervanuitgaand dat je op je 70e met pensioen mag en dus met 68 rekent
        return [row['Voornaam'] for row in Functions().file if Functions.age(datetime.datetime.strptime(row['Geboortedatum'], "%d-%m-%Y")) >= 68]
    
    """
    ?    If the current date is less than the birthday, subtract 1 from the age
        
    ?    :param born: The date of birth of the person
    ?    :return: The age of the person.
    """
    @staticmethod
    def age(born):
        today = datetime.date.today()
        return(today.year - born.year - (\
            (today.month, today.day) < (born.month, born.day)\
            )\
        )
    """
    ?    It takes the data from the csv file, sorts it by date, and returns a list of tuples with the index,
    ?    name, and date of the employee. Ranking them based of their employment date.
        
    ?    :param limit: The amount of employees you want to show
    ?    :return: A list of tuples.
    """
    @staticmethod
    def leaderboard(limit=None):
        print("Employee Leaderboard (Top 10)")
        x = [[row['Datum_in_dienst,'].replace(",",""), row['Voornaam']] for row in Functions().file]
        x.sort(key=lambda date: datetime.datetime.strptime(date[0], "%d-%m-%Y"))
        return [(f"[{i}]","Employee:",v[1],"Has been working Since", v[0]) for i,v in enumerate(x, start=1) if i <= limit]

    """
    ?    It writes the average salary, average salary after tax, number of employees retiring within 2 years,
    ?    top 10 employees, and number of employees with the function "Chauffeur" to a file called backup.txt.
    """
    @staticmethod
    def backup():
        with open('backup.txt', 'w') as file:
            file.write('Average Salary: %s\nAverage Salary (taxed): %s\n' % (Functions.avgsalary()[0], Functions.avgsalary()[1]))
            file.write('Employees retiring within 2 years: %s\n' % len(Functions.retireAlert()))
            [file.write("{} {} {} {} {}\n".format(x[0],x[1],x[2],x[3], x[4])) for x in Functions.leaderboard(10)]
            file.write('Employees with function "Chaffeur": %s\n' % len(Functions.departmentMembers('Chauffeur')))
        print("[+] Backup Complete")
        
    """
    ?    It gets all the jobs and departments from the file and puts them in a list.
    """
    @staticmethod
    def getjobs():
        global jobs; jobs = []
        global departments; departments = []
        [departments.append(row['Afdeling']) for row in Functions().file if row['Afdeling'] not in departments]
        [jobs.append(row['Functie']) for row in Functions().file if row['Functie'] not in jobs]

    """
    ?    It's a static method that allows you to execute python code in the terminal for development and testing purposes.
    """
    @staticmethod
    def DEV():
        while True:
            v = input("Analyzer.py ('EXIT' to QUIT )>>> ")
            exec(v) if v != "EXIT" else exit()
class Menu:
    def __init__(self):
        self.menu = {
            '1': 'Average salary',
            '2': 'Average salary for Function',
            '3': 'No. of employees retiring within 2 years',
            '4': 'No. of employees with function "Chaffeur"',
            '5': 'Top 10 longest employed employees',
            '6': 'People per department with function',
            '7': 'Back all results up to a csv file',
            '8': 'Exit',
            '9': 'Developer Console'
        }
    @staticmethod
    def eventHandler(choice):
        if choice == '1':
            print('Average salary:\n')
            print('Average Salary: %s\nAverage Salary (taxed): %s\n' % (Functions.avgsalary()[0], Functions.avgsalary()[1]))
        elif choice == '2':
            print("Availible Functions:\n\t "+"\n\t ".join(jobs))
            dep = input('Enter Function: \n')
            if dep not in jobs:
                print("Invalid Function")
                return
            print('Average salary for Function:\n')
            [print(x) for x in Functions.departmentsalary(dep)]
        elif choice == '3':
            print("No. of employees retiring within 2 years:", len(Functions.retireAlert()))
        elif choice == '4':
            print('No. of employees with function "Chaffeur":\n', len(Functions.departmentMembers('Chauffeur')))
        elif choice == '5':
            [print(x[0], x[1], x[2], x[3], x[4]) for x in Functions.leaderboard(10)]
        elif choice == '6':
            print("Availible Functions:\n\t "+"\n\t ".join(jobs))
            job = input('Enter Function: \n')
            print("Availible Departments:\n\t "+"\n\t ".join(departments))
            dep = input('Enter department: \n')
            if dep not in departments or job not in jobs:
                print("Invalid department or job")
                return
            print("People per department with function:\n")
            [print(i,v) for i,v in enumerate(Functions.advDepartmentFunctions(dep, job), start=1)]
        elif choice == '7':
            Functions.backup()
        elif choice == '8':
            exit()
        elif choice == '9':
            Functions.DEV()
        else:
            print('Not implemented yet')
            
if __name__ == '__main__':
    os.system('cls') if os.name == 'nt' else os.system('clear')
    print(f"Retrieving Functions from 'VW.csv'...\n")
    Functions.getjobs()
    print(f"Retrieved {len(jobs)} Functions from 'VW.csv'...\n")
    time.sleep(.50)
    print(f"Retrieved {len(departments)} Departments from 'VW.csv'...\n")
    time.sleep(.50)
    while True:
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print(f"\t[Welcome to the Employee Analyzer]\n")
        [print(f'{k}: {v}') for k, v in Menu().menu.items()]
        choice = input('\nChoose an option: \n')
        Menu.eventHandler(choice) if choice.isdigit() and int(choice) <= 8 else print('Invalid input')
        input('Press ENTER to continue...')