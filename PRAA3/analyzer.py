import csv, datetime, os, time

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
    def departmentsalary(department=None):
        allsal = [int(i) for i in [row['Salaris_bruto'] for row in Functions().file if row['Functie'] == department]] # list comprehension
        return(sum(allsal)/len(allsal))
    @staticmethod
    def retireAlert():
        return [row['Voornaam'] for row in Functions().file if datetime.datetime.strptime(row['Geboortedatum'], '%d-%m-%Y').year + 65 < datetime.datetime.now()]
    @staticmethod
    def DEV():
        while True:
            v = input("Analyzer.py ('EXIT' to QUIT )>>> ")
            exec(v) if v != "EXIT" else exit()
class Menu:
    def __init__(self):
        self.menu = {
            '1': 'Average salary',
            '2': 'Average salary per department',
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
            dep = input('Enter department: \n')
            print('Average salary for department:', Functions.departmentsalary(dep))
        elif choice == '3':
            print("No. of employees retiring within 2 years:", len(Functions.retireAlert()))
        elif choice == '7':
            exit()
        elif choice == '8':
            Functions.DEV()
        else:
            print('Not implemented yet')
if __name__ == '__main__':
    [print(f'{k}: {v}') for k, v in Menu().menu.items()]
    choice = input('\nChoose an option: \n')
    Menu.eventHandler(choice) if choice.isdigit() and int(choice) <= 8 else print('Invalid input')
