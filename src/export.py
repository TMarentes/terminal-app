import csv
from employee import Employee

class Export:
    def __init__ (self):
        pass

    def export_all_csv():

        with open('export.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Email", "Department", "Salary"])
            for i in range(len(Employee.employees)):
                writer.writerow([Employee.employees[i].name , Employee.employees[i].email, Employee.employees[i].department, Employee.employees[i].salary])
        print("CSV Created 'export.csv'")


    def export_search_csv(data):
        with open('export.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Email", "Department", "Salary"])
            for i in range(len(data)):
                list_data = []
                for j in range(0,4):
                    list_data.append(data[i][j])
                writer.writerow(list_data)
        print("CSV Created 'export.csv'")




