import csv


class Employee():
    name_emploer = 'иван'
    surname = 'иванович'
    job_title = 'сторож'
    salary = 500

    def __int__(self, name, surname, job_title, salary):
        self.name_emploer = name
        self.surname = surname
        self.job_title = job_title
        self.salary = salary

    def change_name_employee(self, changename):
        self.name_emploer = changename
        return self.name_emploer

    def change_surname_employee(self, changesurname):
        self.surname = changesurname
        return self.surname

    def change_job_title_employee(self, changegettitle):
        self.job_title = changegettitle
        return self.job_title

    def change_salary_employee(self, changesalary):
        self.salary = changesalary
        return self.salary

    def printemployee(self):
        print(self.name_emploer, self.surname, self.job_title, self.salary)

    def change_salary_by_count(self):
        change_salary1 = float(input('how many change salary:'))
        self.salary = self.salary + change_salary1
        name_file = self.name_emploer
        listtowrite=[]
        listtowrite.append(self.salary)
        with open(f'{name_file}.csv', 'w', newline="") as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow(listtowrite)
        return self.salary

    def change_salary_by_percent(self):
        percent_change_salary = float(input('how many percent change salary'))
        change_salary_per = self.salary / 100 * percent_change_salary
        self.salary = self.salary + change_salary_per
        name_file = self.name_emploer
        listtowrite = []
        listtowrite.append(self.salary)
        with open(f'{name_file}.csv', 'w', newline="") as csvfile:
            filewriter = csv.writer(csvfile)
            filewriter.writerow(listtowrite)
        return self.salary

    def comparison_salary_employee(self, secondsalary):
        if self.salary > secondsalary:
            print("У первого  работника зарплата больше")
        else:
            print("у второго зарплата больше")


employ1 = Employee()
employ2 = Employee()

employ1.change_name_employee("Anton")
employ1.change_surname_employee("Ivanov")
employ1.change_job_title_employee("worker")
employ1.change_salary_employee(750)
print(employ1.salary)
employ1.comparison_salary_employee(employ2.salary)
employ1.change_salary_by_percent()
employ1.printemployee()
