import csv, datetime, time, os

class Functions:
    def __init__(self):
        self.file = csv.DictReader(open('VW.csv', 'r'), delimiter=';')
        pass
    
    """
        Opens the csv file and returns a list of lists, iterates thru every row and makes a list of all salaries,
        divides it by the amount of salaries
        returning the average salary.
    """
    @staticmethod
    def avgsalary():
        allsal = [int(i) for i in [row['Salaris_bruto'] for row in Functions().file]] # list comprehension
        return(sum(allsal)/len(allsal))
    @staticmethod
    def departmentMembers(department):
        return [row['Voornaam'] for row in Functions().file if row['Functie'] == department]

    @staticmethod
    def advDepartmentFunctions(departmens, job):
        return [row['Voornaam'] for row in Functions().file if row['Functie'] == job and row['Afdeling'] in departmens]

    @staticmethod
    def departmentsalary(department=None):
        allsal = [int(i) for i in [row['Salaris_bruto'] for row in Functions().file if row['Functie'] == department]] # list comprehension
        return(sum(allsal)/len(allsal))

    @staticmethod
    def retireAlert():
        #! Ervanuitgaand dat je op je 70e met pensioen mag en dus met 68 rekent
        return [row['Voornaam'] for row in Functions().file if Functions.age(datetime.datetime.strptime(row['Geboortedatum'], "%d-%m-%Y")) >= 68]
    
    @staticmethod
    def age(born):
        today = datetime.date.today()
        return(today.year - born.year - (\
            (today.month, today.day) < (born.month, born.day)\
            )\
        )
    @staticmethod
    def leaderboard(limit=None):
        print("Employee Leaderboard (Top 10)")
        x = [[row['Datum_in_dienst,'].replace(",",""), row['Voornaam']] for row in Functions().file]
        x.sort(key=lambda date: datetime.datetime.strptime(date[0], "%d-%m-%Y"))
        return [(f"[{i}]","Employee:",v[1],"Has been working Since", v[0]) for i,v in enumerate(x, start=1) if i <= limit]
        

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
            print('Average salary:', Functions.avgsalary())
        elif choice == '2':
            dep = input('Enter Function: \n')
            print('Average salary for Function:\n$', Functions.departmentsalary(dep))
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
