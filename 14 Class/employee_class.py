#Create a class that contains
#information about employees of a company and
#define methods to get/set employee name, job title, and start date.
class Employee(object):
    '''Employees which can be hired (aggregated) by a company'''

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

#methods to get the employee info
    def get_employee_name(self):
        return self.name

    def get_employee_title(self):
        return self.title

    def getget_employee_start_date(self):
        return self.start_date

#class Company
class Company(object):

    """This represents a company in which people work"""

    def __init__(self, name):
        self.name = name
        self.employees = set()

    def get_name(self):
        '''Returns the name of the company'''
        return self.name

    def get_employees(self):
        '''returns employees'''
        return self.employees

#Consider the concept of aggregation,
#and modify the Company class so that you assign employees to a company.


#Create a company, and three employees,
#and then assign the employees to the company.

#create company
nss = Company('nss')

#create employees
casey = Employee('casey','janitor','4.20.17')
miriam = Employee('miriam','teacher','4.20.17')
dara = Employee('dara','teacher','4.20.17')

nss.employees.add(casey)
nss.employees.add(miriam)
nss.employees.add(dara)

employee_summary = nss.get_employees()


for employee in employee_summary:
    print('{} is a {} at {} '.format(employee.get_employee_name(), employee.get_employee_title(), nss.get_name()))
