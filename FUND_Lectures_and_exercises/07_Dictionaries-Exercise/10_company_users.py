def add_employee(company_dict, company_name, employee_id):
    if employee_id not in company_dict.keys():
        company_dict[company_name] = []


company = dict()
while True:
    input_info = input()
    if input_info == "End":
        break
    name, number = input_info.split(" ->")
    company = add_employee(company, name, number)