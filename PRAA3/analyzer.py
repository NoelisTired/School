import csv, datetime, time, os
class Functions:
    def __init__(self):
        self.file = csv.DictReader(open('VW.csv', 'r'), delimiter=';')
        pass
    

    """
        It takes the file, and then it takes the column 'Salaris_bruto' and puts it in a list. Then it sums
        all the values in the list and divides it by the length of the list
        :return: The average salary of all employees.
    """
    @staticmethod
    def avgsalary():
        allsal = [int(i) for i in [row['Salaris_bruto'] for row in Functions().file]] # list comprehension
        sal = sum(allsal) / len(allsal)
        return("Gross Income:",f"${sal}","With Taxes", f"${sal/79}")
    
    """
        It returns a list of all the first names of the people in the department that is passed as an
        argument
        
        :param department: The department you want to get the members of
        :return: A list of all the first names of the people who work in the department that is given as an
        argument.
    """
    @staticmethod
    def departmentMembers(department):
        return [row['Voornaam'] for row in Functions().file if row['Functie'] == department]

    """
        It returns a list of first names of people who have a job that matches the job parameter and are in
        one of the departments in the departments parameter
        
        :param departmens: a list of departments
        :param job: the job title
        :return: A list of names of people who have the job and are in the department.
    """
    @staticmethod
    def advDepartmentFunctions(departmens, job):
        return [row['Voornaam'] for row in Functions().file if row['Functie'] == job and row['Afdeling'] in departmens]

    """
        It takes a department name as an argument, and returns the average salary of that department
        
        :param department: the department you want to get the average salary of
        :return: The average salary of the department.
    """
    @staticmethod
    def departmentsalary(department=None):
        allsal = [int(i) for i in [row['Salaris_bruto'] for row in Functions().file if row['Functie'] == department]] # list comprehension
        sal = sum(allsal) / len(allsal)
        return("Gross Income:",f"${sal}","With Taxes", f"${sal/79}")

    """
        It returns a list of all the first names of people who are 68 or older
        :return: A list of names of people who are 68 or older.
    """
    @staticmethod
    def retireAlert():
        #! Ervanuitgaand dat je op je 70e met pensioen mag en dus met 68 rekent
        return [row['Voornaam'] for row in Functions().file if Functions.age(datetime.datetime.strptime(row['Geboortedatum'], "%d-%m-%Y")) >= 68]
    
    """
        If the current date is less than the birthday, subtract 1 from the age
        
        :param born: The date of birth of the person
        :return: The age of the person.
    """
    @staticmethod
    def age(born):
        today = datetime.date.today()
        return(today.year - born.year - (\
            (today.month, today.day) < (born.month, born.day)\
            )\
        )
    """
        It takes the data from the csv file, sorts it by date, and returns a list of tuples with the index,
        name, and date of the employee. Ranking them based of their employment date.
        
        :param limit: The amount of employees you want to show
        :return: A list of tuples.
    """
    @staticmethod
    def leaderboard(limit=None):
        print("Employee Leaderboard (Top 10)")
        x = [[row['Datum_in_dienst,'].replace(",",""), row['Voornaam']] for row in Functions().file]
        x.sort(key=lambda date: datetime.datetime.strptime(date[0], "%d-%m-%Y"))
        return [(f"[{i}]","Employee:",v[1],"Has been working Since", v[0]) for i,v in enumerate(x, start=1) if i <= limit]
        

    """
        It's a static method that allows you to execute python code in the terminal for development and testing purposes.
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
            '7': 'Exit',
            '8': 'Developer Console'
        }
    @staticmethod
    def eventHandler(choice):
        if choice == '1':
            print('Average salary:\n', Functions.avgsalary())
        elif choice == '2':
            dep = input('Enter Function: \n')
            print('Average salary for Function:\n', Functions.departmentsalary(dep))
        elif choice == '3':
            # ! Development! \ \ > print(Functions.retireAlert())
            print("No. of employees retiring within 2 years:\n", len(Functions.retireAlert()))
        elif choice == '4':
            print('No. of employees with function "Chaffeur":\n', len(Functions.departmentMembers('Chauffeur')))
        elif choice == '5':
            Functions.leaderboard(10)
        elif choice == '6':
            dep = input('Enter department: \n')
            job = input('Enter job: \n')
            print("People per department with function:\n")
            [print(i,v) for i,v in enumerate(Functions.advDepartmentFunctions(dep, job), start=1)]
        elif choice == '7':
            exit()
        elif choice == '8':
            Functions.DEV()
        else:
            print('Not implemented yet')
            
if __name__ == '__main__':
    while True:
        os.system('cls') if os.name == 'nt' else os.system('clear')
        print(f"\t[Welcome to the Employee Analyzer]\n")
        [print(f'{k}: {v}') for k, v in Menu().menu.items()]
        choice = input('\nChoose an option: \n')
        Menu.eventHandler(choice) if choice.isdigit() and int(choice) <= 8 else print('Invalid input')
        time.sleep(3)
