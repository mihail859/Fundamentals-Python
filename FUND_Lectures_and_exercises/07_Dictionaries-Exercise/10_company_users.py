def add_employee(company_dict, company_name, employee_id):
    pass


company = dict()
while True:
    input_info = input()
    if input_info == "End":
        break
    name, number = input_info.split(" ->")
    company = add_employee(company, name, number)