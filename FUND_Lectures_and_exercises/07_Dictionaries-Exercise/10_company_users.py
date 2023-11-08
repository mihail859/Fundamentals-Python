def add_employee(company_dict, company_name, employee_id):
    if company_name not in company_dict.keys():
        company_dict[company_name] = []
    company_dict[company_name].append(employee_id)
    return company_dict


company = dict()
while True:
    input_info = input()
    if input_info == "End":
        break
    name, number = input_info.split(" ->")
    company = add_employee(company, name, number)

for key, value in company.items():
    print(f"{key}")
    for id_employee in value:
        print("--{}".format(id_employee))