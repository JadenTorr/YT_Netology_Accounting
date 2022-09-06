from application import salary as s
from application.db import people as p
from datetime import datetime

if __name__ == '__main__':
   s.calculate_salary()
   p.get_employees()
   print(f"Текущая дата: {datetime.today().strftime('%d %B %Y')} \nНастоящее время: {datetime.today().strftime('%H:%M:%S')}")
