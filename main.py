from application.salary import calculate_salary
from application.db.people import get_employees

from colorama import Fore, Style
from datetime import datetime

if __name__ == "__main__":
    print(Fore.BLUE + f'current date: {datetime.now().date()}' + Style.RESET_ALL)
    
    employees = get_employees()
    salaries = calculate_salary(employees)
    
    print(Fore.LIGHTCYAN_EX + f"{employees}")
    print(f"{salaries}" + Style.RESET_ALL)